import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto

conn = ooxcb.connect()
screen = conn.pref_screen_object
root = screen.root

root.change_property('DEI_MUDDA', 'WINDOW', 32, [root, root, root])

conn.flush()
