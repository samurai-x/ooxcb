from __future__ import with_statement

import sys
sys.path.append('..')

import ooxcb
from ooxcb import keysymdef
from ooxcb.protocol import xproto

conn = ooxcb.connect()
root = conn.setup.roots[conn.pref_screen].root

# We are performing a passive grab here, we grab a button.
# When the left mouse button is clicked while CTRL is pressed,
# an active grab will occur, and then *we* (and noone else) 
# get the ButtonPress, ButtonRelease and MotionNotify events.
# If either the button or CTRL is released, the active grab is
# terminated automatically. The passive grab remains.
# See http://tronche.com/gui/x/xlib/input/pointer-grabbing.html for
# more on active and passive grabs.
root.grab_button(
        (xproto.EventMask.ButtonPress |
            xproto.EventMask.ButtonRelease |
            xproto.EventMask.PointerMotion),
        xproto.ButtonIndex._1,
        xproto.ModMask.Control)

# And here's another passive grab: A key grab. If CTRL+X is pressed,
# we want to terminate this application.
# We need a keycode for grab_key. Since keycodes are hardware-dependent,
# we'll get the keycode of a hardware-independent keysym here.
keycode = conn.keysyms.get_keycode(keysymdef.keysyms["X"])
root.grab_key(keycode, xproto.ModMask.Control)

@root.event
def on_button_press(evt):
    print 'Button pressed!', evt.event

@root.event
def on_button_release(evt):
    print 'Button released!', evt.event

@root.event
def on_motion_notify(evt):
    print 'Move! x=%d y=%d' % (evt.root_x, evt.root_y)

@root.event
def on_key_press(evt):
    # We'll only get a KeyPressEvent if control and x were pressed,
    # so we don't need to check that here.
    print 'X pressed!'
    # Hey, let's gracefully ungrab what we have grabbed!
    with conn.bunch(): # flushes automatically when the block was executed
        root.ungrab_button(xproto.ButtonIndex._1, xproto.ModMask.Control)
        root.ungrab_key(keycode, xproto.ModMask.Control)
    conn.disconnect()
    sys.exit(0)

conn.flush() # <- important.

while True:
    conn.wait_for_event().dispatch()

conn.disconnect()
