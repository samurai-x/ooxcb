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
import time
import sys

from . import (libxcb, exception)
from .conn import Connection
from ooxcb.constant import *

SETUP = None

CORE = None
CORE_MODULE = None
CORE_EVENTS = {}
CORE_ERRORS = {}

EXTDICT = {}
EXT_EVENTS = {}
EXT_ERRORS = {}

def parse_auth(authstr):
    """
        Parse the X11 authentication string *authstr* and return
        a new `libxcb.xcb_auth_info` instance.
    """
    name, data = authstr.split(':')
    auth = libxcb.xcb_auth_info()
    auth.namelen = len(name)
    auth.name = name
    auth.datalen = len(data)
    auth.data = data
    return auth

def connect(display='', fd=None, auth_string=None, cls=Connection):
    """
        establishes a connection to a X display.

        The X display to connect to can be specified ...

         * by *display*, an X display string.
           If *display* is an empty string, the DISPLAY environment
           variable will be used.
         * by *fd*, an open unix file descriptor.
           *auth_string* is not relevant here.

        *cls* can be used to customize the connection class.
        There has to be an X core protocol module loaded, otherwise an
        :class:`XcbException` is raised.
        :func:`connect` returns a ready to use instance of *cls*.
    """
    auth = None

    if CORE is None:
        raise exception.XcbException(
                "No core protocol object has been set. "
                "Did you import ooxcb.protocol.xproto?"
                )

    conn = cls(CORE)
    if auth_string is not None:
        auth = parse_auth(auth_string)

    if fd is not None:
        conn.conn = libxcb.xcb_connect_to_fd(fd, ctypes.byref(auth))
    elif auth is not None:
        pref_screen = ctypes.c_int()
        conn.conn = libxcb.xcb_connect_to_display_with_auth_info(
                display, ctypes.byref(auth), ctypes.byref(pref_screen)
        )
        conn.pref_screen = pref_screen.value
    else:
        pref_screen = ctypes.c_int()
        conn.conn = libxcb.xcb_connect(display, ctypes.byref(pref_screen))
        conn.pref_screen = pref_screen.value

    conn.do_initial_setup()
    return conn

def popcount(i):
    """
        just a wrapper for the libxcb `xcb_popcount` function that determines
        the number of asserted bits in *i*.
    """
    return libxcb.xcb_popcount(i)

def type_pad(t, i):
    """
        calculates the needed type pad. Mostly for internal use.
    """
    return -i & (3 if t > 4 else t - 1)

def _add_core(value, setup, events, errors):
    """
        called by the core protocol module. Do not call it yourself
        and do not use two core modules :)
    """
    global CORE, CORE_MODULE, CORE_EVENTS, CORE_ERRORS, SETUP # eeeeeevil
    # TODO: I skipped the error checking blah blah
    if CORE is not None:
        raise XcbException("There is already a core module loaded (%s, module %r)" % (CORE, CORE_MODULE))
    CORE_MODULE = sys.modules[value.__module__]
    CORE = value
    CORE_EVENTS = events
    CORE_ERRORS = errors
    SETUP = setup

def _add_ext(key, value, events, errors):
    """
        called by X extension modules. Do not call it yourself.
    """
    EXTDICT[key] = value
    EXT_EVENTS[key] = events
    EXT_ERRORS[key] = errors

def _resize_obj(obj, size):
    """
        sets `obj.size = size`.
    """
    obj.size = size

def timestamp():
    """
        return a cardinal timestamp. a shortcut.
    """
    return int(time.time())

from ooxcb.list import *
from ooxcb.protobj import *
from ooxcb.exception import *
from ooxcb.cookie import *
from ooxcb.ext import *
from ooxcb.resource import *
