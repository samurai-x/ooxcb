# a simple xtest extension test.
from __future__ import with_statement

import sys
sys.path.append('..')

import ooxcb
from ooxcb import XNone
from ooxcb.protocol import xproto, xtest
from ooxcb.constant import KeyPress, KeyRelease, MotionNotify
from ooxcb.keysymdef import keysyms

# necessary for using the `compare_cursor` mixin method of `Window`.
xtest.mixin()

conn = ooxcb.connect()

# fetch the keycode of the 'b' key
keycode = conn.keysyms.get_keycode(keysyms["b"])

with conn.bunch():
    # simulate a 'b' key press
    conn.xtest.fake_input(KeyPress, detail=keycode)
    # simulate a 'b' key release (necessary)
    conn.xtest.fake_input(KeyRelease, detail=keycode)

# and now move the cursor to the center of the screen
screen = conn.setup.roots[conn.pref_screen]
center = (screen.width_in_pixels // 2, screen.height_in_pixels // 2)

with conn.bunch():
    conn.xtest.fake_input(MotionNotify, rootX=center[0], rootY=center[1])

# Now test if the root window's cursor is the null cursor.
# Note that `compare_cursor` was mixed into the Window class.
print screen.root.compare_cursor(XNone).reply().same
# If you wouldn't have called `xtest.mixin` above, you'd have
# to call the method like this:
#print xtest.WindowMixin.compare_cursor(screen.root, XNone).reply().same

