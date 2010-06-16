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

from . import libxcb

class Extension(object):
    """
        A wrapper for an X11 extension.
        This class provides with a :meth:`Extension.send_request`
        method. You will most likely do not have to use this
        class directly.
    """
    def __init__(self, conn, key=None):
        """
            :type conn: :class:`ooxcb.conn.Connection`
            :param key: The corresponding :class:`ooxcb.extkey.ExtensionKey`
                        instance (optional)
        """
        self.key = key
        self.conn = conn
        self.major_opcode = 0
        self.first_event = 0
        self.first_error = 0

    def send_request(self, request, cookie, reply_cls=None):
        """
            sends *request* to the X server. Then it provides
            *cookie* with the needed attributes and returns it.
            *reply_cls* is the optional reply class which will
            also be redirected to *cookie*.
            If :attr:`ooxcb.conn.Connection.synchronous_check`
            is True, this will also force every request to be
            checked and check it immediately after sending.
        """
        # TODO: remove that...
        if (self.conn.synchronous_check and request.is_void):
            request.is_checked = True

        xcb_req = libxcb.xcb_protocol_request_t()
        xcb_req.count = 2
        xcb_req.ext = (ctypes.pointer(self.key.key)
                if self.key is not None else None) # TODO?
        xcb_req.opcode = request.opcode
        xcb_req.isvoid = request.is_void

        s = request.buffer
        data = ctypes.cast(
                ctypes.create_string_buffer(s, len(s)),
                ctypes.c_void_p
        )

        xcb_parts = (libxcb.iovec * 2)()
        addr = ctypes.cast(xcb_parts, ctypes.c_void_p).value

        xcb_parts[0].iov_base = data
        xcb_parts[0].iov_len = request.size
        xcb_parts[1].iov_base = 0
        xcb_parts[1].iov_len = -xcb_parts[0].iov_len & 3 # ... O_o

        flags = libxcb.XCB_REQUEST_CHECKED if request.is_checked else 0
        seq = libxcb.xcb_send_request(self.conn.conn, flags,
                xcb_parts,
                ctypes.byref(xcb_req))
        cookie.conn = self.conn
        cookie.request = request
        cookie.reply_cls = reply_cls
        cookie.cookie.sequence = seq

        # TODO: remove that...
        if (self.conn.synchronous_check and request.is_void):
            cookie.check()
        return cookie

class ExtensionKey(object):
    """
        just a wrapper class for :class:`libxcb.xcb_extension_t`.
        :todo: explain what an extension key is
    """
    def __init__(self, name):
        self.key = libxcb.xcb_extension_t()
        self.key.name = name
        self.name = name

    def __hash__(self):
        return hash(self.name)

