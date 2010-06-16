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

class MemoryInputStream(object):
    """
        `MemoryInputStream` is an object implementing the buffer
        interface which reads its data from a certain
        memory buffer. It is interpreted as an infinite
        array of 8-bit chars.
        This stream is used for ooxcb protocol parsing.
    """
    def __init__(self, address):
        """
            :Parameters:
                `address` : int
                    The address of the first character.
        """
        self._root = address
        self._ptr = address
        self._opened = True

    def close(self):
        self._opened = False

    @property
    def closed(self):
        return not self._opened

    def fileno(self):
        """ We are not using a file descriptor """
        raise IOError()

    def flush(self):
        pass

    def isatty(self):
        return False

    def readable(self):
        return True

    def readline(self, limit):
        raise NotImplementedError()

    def readlines(self, hint):
        raise NotImplementedError()

    def seek(self, offset, whence=0):
        """
            Currently you can not use whence=2.
            The stream has no end.
        """
        if whence == 0:
            # from the start position of the stream
            self._ptr = self._root + offset
            return offset
        elif whence == 1:
            # from the current position of the stream
            self._ptr += offset
            return self._ptr - self._root
        elif whence == 2:
            # from the end of the stream ... impossible, sorry.
            raise NotImplementedError('The memory stream has no end!')
        else:
            raise NotImplementedError('Unknown whence: %d' % whence)

    @property
    def address(self):
        return self._root

    def seekable(self):
        return True

    def tell(self):
        return self._ptr - self._root

    def truncate(self):
        """
            That's a no-op here. I can't think of anyone needing that
            for a memory buffer, really.
            However, it will raise a NotImplementedError. But we can
            remove that.
        """
        raise NotImplementedError() # hmmm ...

    def writable(self):
        return False

    def write(self, b):
        raise IOError()

    def read(self, b=None):
        if b is None:
            raise NotImplementedError('The memory stream has no end!')
        chunk = ctypes.string_at(self._ptr, b)
        self._ptr += b
        return chunk

    def readall(self):
        raise NotImplementedError('The memory stream has no end!')

    def readinto(self, b):
        length = len(b)
        b.extend(self.read(length))
        return length

if __name__ == '__main__':
    # TODO: build a nice test for that.
    buf = ctypes.create_string_buffer('abcdefghijklmnopqrstuvwxyz')
    stream = MemoryInputStream(ctypes.addressof(buf))
    print stream.read(2)
    print stream.read(4)
    print stream.seek(0)
    print stream.read(26)
    print repr(stream.read(10))

