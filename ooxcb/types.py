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

from .protobj import Protobj

SIZES = {
        8: 'B',
        16: 'H',
        32: 'I',
        }

def make_array(data, typecode):
    """
        return a packed representation of the data *data*.

        :Parameters:
            `data`: list or str or unicode
                should be a list of numeric values, each item
                suitable for the given typecode.
                If it's a str or unicode instance, each char
                is converted to its ordinal value and then packed.
                Any element's `get_internal` method will be called
                if present.
            `typecode`: str
                one of:
                 * 'b', 8 bit signed
                 * 'B', 8 bit unsigned
                 * 'h', 16 bit signed,
                 * 'H', 16 bit unsigned
                 * 'i', 32 bit signed
                 * 'I', 32 bit unsigned
                 * 'f', float
                 * 'd', double
        :returns: a string
    """
    if isinstance(data, basestring):
        data = map(ord, data)
    for idx, item in enumerate(data):
        if hasattr(item, 'get_internal'):
            # Hell Yeah, so evil.
            data[idx] = item.get_internal()
    fmt = '=' + (typecode * len(data))
    return struct.pack(fmt, *data)

def make_void_array(data, format):
    """
        Return a packed representation of the data *data*.
        The only difference to `make_array` is that you pass the
        count of bytes per value to `make_void_array`, and all
        values are treated as unsigned.

        :param format: the count of bits to pack per value,
                       one of 8, 16, 32.
    """
    typecode = SIZES[format]
    return make_array(data, typecode)

def build_list(conn, stream, list_, type):
    """
        writes a *list_* of objects of the elementar
        data type *type* (where *type* is a :mod:`struct`-compatible
        type char) to *stream*.

        For each item, this checks if the item is a
        :class:`ooxcb.protobj.Protobj`. If it is, the object's `build` method
        is called.
    """
    for item in list_:
        if getattr(type, 'create_lazy', None):
            item = type.create_lazy(conn, item)
        if isinstance(item, Protobj):
            item.build(stream)
        else:
            stream.write(struct.pack(type, item))

