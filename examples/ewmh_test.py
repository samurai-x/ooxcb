import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto
from ooxcb.contrib import ewmh

ewmh.mixin()
conn = ooxcb.connect()
screen = conn.setup.roots[conn.pref_screen]

print 'Client List:', screen.ewmh_get_client_list()
print 'Client List (stacking):', screen.ewmh_get_client_list_stacking()
print 'Number of desktops:', screen.ewmh_get_number_of_desktops()
print 'Current desktop:', screen.ewmh_get_current_desktop()

conn.disconnect()
