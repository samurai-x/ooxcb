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

from . import (libxcb, util)
from .exception import XcbException
from .protobj import Error

class Cookie(object):
    """
        A Cookie is something like a placeholder for a request's response.
        When invoking a request method, you will get a
        :class:`ooxcb.cookie.Cookie` subclass instance as return value.
        If you need the reply, you just call the
        :meth:`ooxcb.cookie.Cookie.reply` method and you get a
        :class:`ooxcb.response.Response` subclass instance. The request
        is sent and handled just when you call `reply`.
        If you have a request without a response (a void request), you
        have to call the `..._checked` method to be able to check this
        specific cookie using the :meth:`ooxcb.cookie.Cookie.check`
        method.

        See http://lists.freedesktop.org/archives/xorg-announce/2006-September/000134.html
        for a better description of checked and unchecked requests :)
    """
    def __init__(self):
        self.conn = None
        self.reply_cls = None
        self.request = None
        self.cookie = libxcb.xcb_void_cookie_t()

    def check(self):
        """
            Explicitly check a void, checked request.
            Raises an error if there is one. If there is none,
            None is returned.
            That will raise an `XcbException` if the request is not checked
            and/or not void.
        """
        error = ctypes.pointer(libxcb.xcb_generic_error_t())
        if not (self.request.is_void and self.request.is_checked):
            raise XcbException('Request is not void and checked!')
        self.conn.check_conn()

        error = libxcb.xcb_request_check(self.conn.conn, self.cookie)
        Error.set(self.conn, error)

    def reply(self):
        """
            return the reply of the request. That will raise a
            `XcbException` if the request is void.
        """
        if self.request.is_void:
            raise XcbException('Request has no reply.')
        self.conn.check_conn()

        err = libxcb.xcb_generic_error_t()
        error = ctypes.pointer(err)
        data = libxcb.xcb_wait_for_reply(self.conn.conn,
                self.cookie.sequence, ctypes.byref(error))
        Error.set(self.conn, error)
        if not data:
            raise IOError("I/O error on X server connection.")
        return self.reply_cls.create_from_address(self.conn, data)

class VoidCookie(Cookie):
    """
        a void cookie class.
    """
    pass

__all__ = ['Cookie', 'VoidCookie']
