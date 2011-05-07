# Copyright (c) 2008-2011, samurai-x.org
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the samurai-x.org nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY SAMURAI-X.ORG ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL SAMURAI-X.ORG  BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import ctypes
from contextlib import contextmanager
from weakref import WeakValueDictionary

from . import libxcb
from .protobj import Event, Error
from .eventsys import EventDispatcher
from .resource import XNone
from .atoms import AtomDict
from .keysyms import Keysyms

class Connection(EventDispatcher):
    """
        The ooxcb connection class is the main point of ooxcb. It is
        similar to libX11's `Display`.

        The Connection class is an event dispatcher, so you can register
        for events.

        The Connection instance has a `core` attribute that is the core
        extension instance, and it also sets the `xproto` attribute for
        the xproto extension.

        :todo: describe events
    """
    def __init__(self, core):
        """
            :param core: The core extension class.
        """
        EventDispatcher.__init__(self)

        self.core = core(self)
        setattr(self, core.header, self.core)

        # opaque libxcb connection
        self.conn = None
        self.events = {}
        self.errors = {}
        self.extcache = {}
        self._setup = None
        # check all events synchronously? for debugging.
        self.synchronous_check = False
        # helper
        self.keysyms = Keysyms(self)
        # helper
        self.atoms = AtomDict(self)
        # the X object cache. {X ID: Object, ...}
        self._cache = WeakValueDictionary()
        # add XNone to the cache ...
        self.add_to_cache(0, XNone)

    @property
    def pref_screen_object(self):
        """
            Return the preferred :class:`protocol.xproto.Screen` instance.
            Shortcut for ``conn.setup.roots[conn.pref_screen]``
        """
        return self.setup.roots[self.pref_screen]

    @contextmanager
    def bunch(self):
        """
            Use this in a `with` statement.
            Example:

            ::

                with conn.bunch():
                    for window in windows:
                        window.map()

            When the `with` statement is left,
            the connection will be flushed.

        """
        yield
        self.flush()

    def do_initial_setup(self):
        """
            loads the core events, the core errors and sets them up.

            :note: Internally called by :func:`ooxcb.connect`.
        """
        import ooxcb
        # load core ...
        ext = self.core
        events = ooxcb.CORE_EVENTS
        errors = ooxcb.CORE_ERRORS
        self.setup_helper(ext, events, errors)

        for key, events in ooxcb.EXT_EVENTS.iteritems():
            errors = ooxcb.EXT_ERRORS[key]
            ext = self.load_ext(key)

            if ext.present:
                self.setup_helper(ext, events, errors)

    def setup_helper(self, ext, events, errors):
        """
            gets all events and errors from *ext* and registers
            them.

            :note: Internal method.
        """
        for num, type in events.iteritems():
            opcode = ext.first_event + num
            self.events[opcode] = type
            # register all events to their target!
            type.event_target_class.register_event_type(type.event_name)

        for num, type in errors.iteritems():
            opcode = ext.first_error + num
            self.errors[opcode] = type

    def load_ext(self, key):
        """
            load an extension.

            :note: internally called
        """
        import ooxcb
        if key in self.extcache:
            return self.extcache[key]
        else:
            cls = ooxcb.EXTDICT[key]
            ext = cls(self, key)
            reply = libxcb.xcb_get_extension_data(self.conn, key.key).contents
            ext.present = reply.present
            ext.major_opcode = reply.major_opcode
            ext.first_event = reply.first_event
            ext.first_error = reply.first_error

            self.extcache[key] = ext
            setattr(self, cls.header, ext)

            return ext

    @property
    def alive(self):
        """
            True if the connection is valid, False if it
            is not (ie disconnected)
        """
        return self.conn is not None

    def check_conn(self):
        """
            checks *self.conn* and raises an :class:`IOError` if it's None.
        """
        if not self.alive:
            raise IOError("Connection is not valid anymore")

    def has_error(self):
        """
            returns True if the connection has encountered an error.
        """
        self.check_conn()
        return bool(libxcb.xcb_connection_has_error(self.conn))

    def get_file_descriptor(self):
        """
            get the unix file descriptor.
        """
        self.check_conn()
        return libxcb.xcb_get_file_descriptor(self.conn)

    def get_maximum_request_length(self):
        """
            return the connection's maxmimum request length.
        """
        self.check_conn()
        return libxcb.xcb_connection_get_maximum_request_length(self.conn)

    def prefetch_maximum_request_length(self):
        """
            prefetches the maximum request length without blocking.
        """
        self.check_conn()
        libxcb.xcb_prefetch_maximum_request_length(self.conn)

    def get_setup(self):
        """
            get the connection's setup and return it.
            The setup instance is cached.
        """
        self.check_conn()
        if self._setup is None:
            s = libxcb.xcb_get_setup(self.conn)
            addr = ctypes.addressof(s.contents)
            from . import SETUP
            self._setup = SETUP.create_from_address(self, addr)

        return self._setup

    setup = property(get_setup)

    def generate_id(self):
        """
            generates a new X ID and return it.
        """
        self.check_conn()
        xid = libxcb.xcb_generate_id(self.conn)
        # TODO: error checking ...
        return xid

    def wait_for_event(self):
        """
            waits for an event (blocking) and returns it.

            If an connection IO error encountered, it raises an `IOError`.
            This can also raise Xcb protocol errors.
        """
        data = libxcb.xcb_wait_for_event(self.conn)
        if not data:
            raise IOError("I/O error on X server connection.")
        if data.contents.response_type == 0:
            Error.set(self, ctypes.cast(data,
                ctypes.POINTER(libxcb.xcb_generic_error_t)))
            return
        return Event.create(self, data)

    def poll_for_event(self):
        """
            polls for an event (non-blocking) and returns it.
            If there was no event, None is returned.

            :see: *wait_for_event*
        """
        data = libxcb.xcb_poll_for_event(self.conn)
        if not data:
            return None

        if data.contents.response_type == 0:
            Error.set(self, ctypes.cast(data,
                ctypes.POINTER(libxcb.xcb_generic_error_t)))
            return
        return Event.create(self, data)

    def flush(self):
        """
            flushes the connection. All cached requests are sent.
        """
        self.check_conn()
        libxcb.xcb_flush(self.conn)

    def disconnect(self):
        """
            disconnect from the X server gracefully and set
            *self.conn* to None.
        """
        if self.conn:
            libxcb.xcb_disconnect(self.conn)
            self.conn = None

    def add_to_cache(self, xid, obj):
        """
            add the X object *obj* with the X ID *xid*
            to the internal X object cache.
        """
        self._cache[xid] = obj

    def get_from_cache_fallback(self, xid, cls):
        """
            If there is a resource using the xid *xid* in the cache,
            return it. If not, instantiate *cls*, add to cache
            and return the newly created object.
        """
        if xid in self._cache:
            return self._cache[xid]
        else:
            self._cache[xid] = ret = cls(self, xid)
            return ret

    def remove_from_cache(self, xid):
        """
            removes the object managing the X resource with the X id *xid*
            from the cache. Will raise a KeyError if there is no such
            resource in the cache.
        """
        del self._cache[xid]

    def remove_from_cache_safe(self, xid):
        """
            same as :meth:`remove_from_cache`, but does not raise a KeyError.
            Instead, it does nothing. It is safe.
        """
        try:
            self.remove_from_cache(xid)
        except KeyError:
            pass

