import sys
sys.path.append('..')

import ooxcb
from ooxcb.contrib.gdk import get_icon_pixbufs, choose_icon
from ooxcb.protocol import xproto

SIZE = (96, 128)

conn = ooxcb.connect()
screen = conn.pref_screen_object
root = screen.root

clients = root.get_property('_NET_CLIENT_LIST', 'WINDOW').reply().typed_value
for window in clients:
    icon_reply = window.get_property('_NET_WM_ICON', 'CARDINAL').reply()
    if icon_reply.exists:
        icons = get_icon_pixbufs(icon_reply.typed_value)
        print icons
        icon = choose_icon(icons, SIZE)
        if icon is not None:
            icon.save('icon-0x%x.png' % window.xid, 'png')

