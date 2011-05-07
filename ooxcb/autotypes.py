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

from .protocol import xproto

def _resource(type):
    def _converter(conn, values):
        return [conn.get_from_cache_fallback(value, type) for value in values]
    return _converter

AUTO_TYPES = {
    'WINDOW': _resource(xproto.Window),
    'PIXMAP': _resource(xproto.Pixmap),
    'DRAWABLE': _resource(xproto.Drawable),
    'STRING': lambda conn, values: ''.join(map(chr, values)),
    'UTF8_STRING': lambda conn, values: ''.join(map(chr, values)).decode('utf-8'),
    'CARDINAL': lambda conn, values: values,
    'ATOM': lambda conn, values: map(conn.atoms.get_by_id, values),
    'INTEGER': lambda conn, values: values,
}

class AutotypesError(Exception):
    pass

def autoconvert_value(conn, type, values):
    """
        Return a converted version of *values*.
        :Parameters:
            `conn`
            `type`: Atom
            `values`:
                A list of numeric values descsribing the value.
    """
    type_name = type.get_name().reply().name
    if type_name not in AUTO_TYPES:
        raise AutotypesError("Don't know how to convert %r" % type_name)
    return AUTO_TYPES[type_name](conn, values)
