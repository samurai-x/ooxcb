import sys
sys.path.append('../..')
from time import time

import xcb
from xcb import xproto as X

NUM_NAMES = 500
NAMES = ['NAME%d' % i for i in xrange(NUM_NAMES)]

conn = xcb.connect()
start = time()

cookies = []
atoms = []
for name in NAMES:
    cookies.append(conn.core.InternAtom(False, len(name), name))

for cookie in cookies:
    reply = cookie.reply()
    if reply:
        atoms.append(reply.atom)

end = time()

print 'Elapsed time: %f' % (end - start)
