import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto

conn = ooxcb.connect()

screen = conn.pref_screen_object
active = screen.get_active_window()
reply = active.get_property('_NET_WM_NAME', 'UTF8_STRING').reply()
if reply.exists:
    print 'The property exists.'
else:
    print 'The property does not exist.'
print 'Value: %s' % repr(reply.typed_value)

for atom in screen.root.list_properties().reply().atoms:
    prop = screen.root.get_property(atom, xproto.GetPropertyType.Any).reply()
    print '%s(%s) = %r' % (atom.name, prop.type.name, prop.typed_value)
