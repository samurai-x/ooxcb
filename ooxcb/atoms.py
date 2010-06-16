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

class AtomDict(dict):
    """
        A dictionary which is able to lazily load an atom
        and that contains all predefined atoms from :mod:`ooxcb.constant`.

        ::

            dic = AtomDict(my_connection)
            print dic['WM_CLASS'] # Yay, it is lazily loaded!
            aid = dic['WM_CLASS'].get_internal()
            # ... and vice-versa:
            assert dic.get_by_id(aid) == dic['WM_CLASS']

        You should not modify the dictionary manually.

    """
    def __init__(self, conn, *boo, **far):
        dict.__init__(self, *boo, **far)
        self.conn = conn
        self._by_id = {}
        self._add_predefined()
        self.do_name_lookup = True

    def _add_predefined(self):
        """
            add the predefined atoms from :module:`ooxcb.constant`.
        """
        # TODO: uglyuglyuglyuglyuglyUGLY
        from . import constant
        from ooxcb.protocol.xproto import Atom # TODO:
        for name in dir(constant):
            if name.startswith('XA_'):
                key = name[len('XA_'):]
                value = getattr(constant, name)
                atom = Atom(self.conn, value)
                self.add_atom(key, atom)

    def add_atom(self, name, atom):
        """
            add the atom *atom* with the name *name* to the cache.
        """
        self[name] = atom
        self._by_id[atom.get_internal()] = atom

    def __missing__(self, key):
        self[key] = value = self.conn.core.intern_atom(key, False).reply().atom
        self._by_id[value.get_internal()] = value
        return value

    def get_by_id(self, aid):
        """
            return an atom instance for the ID *aid*.

            That is not part of the connection's XID cache because atom ids
            do not seem to be part of the XID space; they have their own
            space.

            For aid == 0, it will return None, but this may
            change in the future.

            :todo: currently, this depends on :mod:`ooxcb.protocol.xproto`. That's
                   not really consistent.
        """
        from ooxcb.protocol.xproto import Atom # TODO: uuuuuuuugly
        if aid == 0:
            return None # TODO: That's basically AnyProperty ... better solution?
        try:
            return self._by_id[aid]
        except KeyError:
            atom = Atom(self.conn, aid)
            if self.do_name_lookup:
                self._by_id[aid] = atom
                name = atom.get_name().reply().name
                self[name] = atom
            return atom

