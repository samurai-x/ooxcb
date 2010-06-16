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

from .exception import ProtocolDataError
from .eventsys import EventDispatcher

class Resource(EventDispatcher):
    """
        A resource is nearly every object in the X world having
        an X ID: Windows, Graphics Contexts, Fonts ...
        Except atoms. Atoms are not part of the XID space, and
        they have a separate cache.

        Each resource has an *xid* attribute. It can also be accessed
        by :meth:`get_internal`.

        Resources are also :class:`ooxcb.eventsys.EventDispatcher`
        subclasses.
    """
    def __init__(self, conn, xid):
        self.conn = conn
        assert isinstance(xid, (int, long)), \
                "You have specified an invalid X ID: %s" % xid
        self.xid = xid

    def __repr__(self):
        return '<%s XID=%d (0x%x)>' % (
                self.__class__.__name__, self.xid, id(self)
                )

    def get_internal(self):
        """
            The internal representation of a resource is its X id.
            Return it.
        """
        return self.xid

    # No __hash__ / __cmp__ should be needed here. Resources are cached,
    # identity comparison should be sufficient. However, TODO?

class _XNone(object):
    """
        A class for *XNone*. That's something with 0 as an internal
        representation and often used :)
    """
    def __repr__(self):
        return '<XNone>'

    def get_internal(self):
        return 0

XNone = _XNone()

def get_internal(obj):
    """
        get the stream-ready internal representation of *obj*.
        There are multiple possible cases:

            * If *obj* has a `get_internal` method, the return value of
              that will be returned.
            * If *obj* is an int, it will be returned immediately.
            * If *obj* is None, 0 will be returned.
            * If *obj* is something else, a
              :class:`ProtocolDataError <ooxcb.ProtocolDataError>` will be
              raised.
    """
    if hasattr(obj, 'get_internal'):
        return obj.get_internal()
    elif isinstance(obj, int):
        return obj
    elif obj is None:
        return 0
    else:
        raise ProtocolDataError("The internal value of %r couldn't be retrieved." % obj)

