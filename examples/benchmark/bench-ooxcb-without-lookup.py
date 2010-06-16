import sys
sys.path.append('../..')
from time import time

import ooxcb
from ooxcb.protocol import xproto as X

NUM_NAMES = 500
NAMES = ['NAME%d' % i for i in xrange(NUM_NAMES)]

conn = ooxcb.connect()
conn.atoms.do_name_lookup = False
start = time()

cookies = []
atoms = []
for name in NAMES:
    cookies.append(conn.core.intern_atom(name, False))

for cookie in cookies:
    reply = cookie.reply()
    if reply:
        atoms.append(reply.atom)

end = time()

print 'Elapsed time: %f' % (end - start)
