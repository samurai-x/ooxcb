# Copyright (c) 2008-2010, samurai-x.org
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

from . import libc
from .libxcb import xcb_generic_reply_t
from .util import cached_property
from .memstream import MemoryInputStream

class Protobj(object):
    """
        Base class for all protocol objects.

        .. data:: create_lazy

            None as default, but it can be a classmethod used
            to create a Protobj instance lazily for convenience.

            :see: :func:`ooxcb.builder.build_list`

        .. data:: pythonize_lazy

            None as default, but if it can be a method used to
            pythonize a protocol object lazily if it's inside
            a list.

            :see: :class:`ooxcb.list.List`

    """
    create_lazy = None # TODO: does it have to be defined here?
    pythonize_lazy = None

    def __init__(self, conn):
        self.conn = conn

    def read(self, stream):
        """
            Placeholder for subclasses.
            :param stream: an object providing a buffer interface. Read
                           myself from that stream!
        """
        raise NotImplementedError()

    def read_from_address(self, address):
        """
            parse the memory at *address*
        """
        return self.read(MemoryInputStream(address))

    @classmethod
    def create_from_address(cls, conn, address):
        """
            :type conn: :class:`ooxcb.conn.Connection`
            :param address: an int pointing to the data in the
                            memory
        """
        self = cls(conn)
        self.read_from_address(address)
        return self

    @classmethod
    def create_from_stream(cls, conn, stream):
        """
            :type conn: :class:`ooxcb.conn.Connection`
            :param stream: a stream-like object to read from.
        """
        self = cls(conn)
        self.read(stream)
        return self

class Struct(Protobj):
    """
        also just a subclass of :class:`protobj.Protobj`. Nothing special here.
    """
    pass

class Union(Protobj):
    """
        the baseclass for Unions. Nothing special.
    """
    pass

class Request(Protobj):
    """
        mostly just a value holder for :meth:`ooxcb.ext.Extension.send_request`
    """
    def __init__(self, conn, buffer, opcode, void, checked):
        # TODO: check size??
        self.opcode = opcode
        self.is_void = void
        self.is_checked = checked

        Protobj.__init__(self, conn)

        self.buffer = buffer
        self.size = len(buffer)

class Response(Protobj):
    """
        a response wrapper. Had a *sequence* getter in the past,
        but it isn't used. If it should be added again, file a bug.
    """
    pass

class Error(Response):
    """
        An error is a special kind of response that is used when an
        error occured. It will be "packed into" a Python exception
        in :meth:`Error.set`.
    """
    @classmethod
    def set(cls, conn, err):
        """
            raise the right exception for the
            :class:`ooxcb.libxcb.xcb_generic_error_t` struct *err*
            if it is an error.

            :param err: a ctypes pointer to a
                        :class:`ooxcb.libxcb.xcb_generic_error_t`.
        """
        if err:
            e = err.contents
            # get the opcode and the corresponding error type / exception class
            opcode = e.error_code
            type, exception = conn.errors[opcode]
            address = ctypes.addressof(e)

            inst = type.create_from_address(conn, address)
            libc.free(address)

            raise exception(conn, inst)

class Event(Response):
    """
        An event is a special kind of response.
        And in ooxcb, it comes with a builtin ability to be dispatched.

        For that purpose, every Event subclass has an `event_name` member.
        That's the name of the event, e.g. 'on_configure_notify'. It is
        'on_event' as fallback here, so if you stumble upon 'on_event'
        somewhere, there is something wrong.

        So, if you want to dispatch an event, just call :meth:`dispatch`.
        A typical line in the main loop would then be:

        ::

            conn.wait_for_event().dispatch()

        which will automatically dispatch every received event.

        Every event will be dispatched to an appropriate target, e.g.
        a :class:`ooxcb.xproto.ButtonPressEvent` will be dispatched
        to the window the event happened in. The targets are defined
        in the interface files. The fallback target is the connection.

        If you want to know which event types a class receives, you can
        access the *event_types* attribute that is a list of event names.

        If you want to know the event target of an event, you can access
        its *event_target* attribute.

        Every event is sent with the event itself as the first and only
        argument. So all ooxcb event handlers have the following signature:

        ::

            def on_blabla(evt)

    """
    event_name = 'on_event'

    def __init__(self, conn):
        Response.__init__(self, conn)
        self.event_target = conn

    @classmethod
    def create(cls, conn, event):
        opcode = event.contents.response_type & ~0x80 # strip 'send event' bit

        type = cls

        if (opcode in conn.events and conn.events[opcode]):
            type = conn.events[opcode]

        address = ctypes.addressof(event.contents)
        evt = type.create_from_address(conn, address)
        libc.free(address)
        return evt

    def dispatch(self):
        """
            dispatch *self* to my event target
        """
        return self.event_target.dispatch_event(self.event_name, self)

class Reply(Response):
    """
        a reply is a :class:`response.Response` subclass.
    """
    @cached_property
    def _struct(self):
        return xcb_generic_reply_t.from_address(self._address)

    @property
    def length(self):
        """
            The reply length.
        """
        return self._struct.length

