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

import struct

class List(list):
    """
        :class:`List` is a :class:`list` subclass that reads its
        members from a memory stream. It also provides with
        methods to convert this data to more useful values.
    """
    def __init__(self, conn, stream, length, type, size=-1):
        """
            :Parameters:
                `conn`: :class:`ooxcb.conn.Connection`
                `stream`: stream-like object
                    The stream to read the list data from. That will
                    most likely be a :class:`ooxcb.memstream.MemoryInputStream`
                    but any other object offering a buffer interface
                    is allowed.
                `length`: int
                    Count of items the list contains
                `type`: a typestring or a class
                    Information about the list type.
                `size`: int
                    The size of one item; not necessarily required.

            There are three kinds of lists here:

             * If *type* is a string (a typecode), the list contains *length*
               elementar, homogenous items, each *size* bytes big.
             * Otherwise, if *size* is > 0, *type* has to be a class that
               is initiated for each element. Then, the `read` method is called
               on the resulting object, with the stream as first element.
               The object is required to read exactly *size* bytes.
             * Otherwise, *type* is also required to be a class and is
               instantiated, `read` is called, and then the `size` attribute
               is read. That's for dynamic objects.
               Now, if the type has a `pythonize_lazy` method defined, it
               will be called on the object. That's a convenience method, ie
               for strings. The user doesn't have to bother with
               :class:`protocol.xproto.Str` instances, it is just converted to a Python
               string lazily and on-the-fly.
        """
        self.conn = conn
        cur = 0
        root = stream.tell()
        if isinstance(type, str):
            if length:
                fmt = '=' + (type * length)
                self.extend(struct.unpack(fmt, stream.read(size * length)))
                cur = size * length
        else:
            for i in xrange(length):
                # TODO: I don't think that call is necessary. If there are problems
                # try to comment in this call ;-)
                #stream.seek(cur)
                if size > 0:
                    obj = type(conn)
                    obj.read(stream)
                    cur += size
                    # If the type has a `pythonize_lazy` method defined, call it.
                    if type.pythonize_lazy:
                        obj = obj.pythonize_lazy()
                else:
                    obj = type(conn) # ... is a sequence
                    obj.read(stream)
                    datalen = obj.size
                    cur += datalen
                    # If the type has a `pythonize_lazy` method defined, call it.
                    if type.pythonize_lazy:
                        obj = obj.pythonize_lazy()

                self.append(obj)

        self.size = stream.tell() - root

    def to_string(self):
        """
            my value is a list of ordinal values; return
            the string.
        """
        return ''.join(map(chr, self))

    def to_utf8(self):
        """
            interpret the string returned by :meth:`to_string`
            as utf-8 and return a Python unicode object.
        """
        return self.to_string().decode('utf-8')

    def to_atoms(self):
        """
            my value is a list of atom ids, return a list of
            :class:`Atom <ooxcb.protocol.xproto.Atom>` instances.
        """
        return map(self.conn.atoms.get_by_id, self)

    def to_resources(self, cls):
        """
            interpret the data as a homogenous list of X ids.

            :param cls: The resource class to instantiate if the
                        corresponding X id couldn't be found in
                        the cache.
            :returns: a list of *cls* instances
        """
        return [self.conn.get_from_cache_fallback(xid, cls)
                for xid in self]

    def to_windows(self):
        """
            I am a list of :class:`ooxcb.protocol.xproto.Window` Ids. Just
            a shortcut for :meth:`to_resources`.
        """
        from ooxcb.protocol.xproto import Window # TODO: imports in methods are not nice
        return self.to_resources(Window)

    @staticmethod
    def from_resources(resources):
        """
            returns an ordinary Python list that contains the X ids
            of the resources in *resources*.
        """
        return [res.get_internal() for res in resources]

    @staticmethod
    def from_atoms(atoms):
        """
            returns an ordinary Python list that contains the atom ids
            of the atoms in *atoms*.

            :note: Actually that's the same as :meth:`from_resources`.
                   But explicit is better than implicit ...
        """
        return [atom.get_internal() for atom in atoms]

    @staticmethod
    def from_string(string):
        """
            returns a Python list containing the ordinal values of *string*'s
            chars (should also for unicode objects)
        """
        return map(ord, string)

    @staticmethod
    def from_stringlist(stringlist):
        """
            returns a Python list containing the ordinal values of each string
            in *stringlist*, all of them linked together by \\x00 bytes and
            with a trailing \\x00 byte.
        """
        return map(ord, '\x00'.join(stringlist)) + [0]

