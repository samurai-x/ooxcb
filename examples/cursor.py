# Today: How to construct your own cursors!

import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto

conn = ooxcb.connect()
screen = conn.setup.roots[conn.pref_screen]

# First, we create a pixmap with the depth of 1. Such a pixmap
# is also called a bitmap, because each pixel is either 1 or
# 0. We want a 32x32 cursor.
pixmap = xproto.Pixmap.create(conn, screen.root, 32, 32, 1)
# Now we create a graphics context for that pixmap. Initially, it has
# the foreground pixel 0, and the background pixel 1.
gc = xproto.GContext.create(conn, pixmap, foreground=0, background=1)
# Here we clear the mask. After that, all pixels in `pixmap` are turned
# off (0).
gc.poly_fill_rectangle(pixmap,
        [xproto.Rectangle.create(conn, 0, 0, 640, 480)])
# Since we now want to draw the shape of the cursor, we swap the
# foreground and background pixels.
gc.change(foreground=1, background=0)
# And we draw the shape of our cursor.
gc.poly_line(pixmap, [(0, 0), (32, 32)])

# After having done that, we create a cursor from that bitmap.
cursor = xproto.Cursor.create(conn,
        # That's our source bitmap.
        pixmap,
        # We could pass a mask bitmap here that specifies the
        # pixels that should be displayed. If we pass None,
        # all pixels of the source bitmap are displayed.
        None,
        # Here we pass the RGB values for all pixels with a value of 1.
        # Note that the range of each RGB value is 0..65535.
        65535,
        0,
        0,
        # That's the RGB value for all pixels with a value of 0.
        0,
        65535,
        0,
        # The last two arguments describe the x, y position of the cursor
        # hotspot. It defines the point that is reported if when pointer
        # event occurs.
        0,
        0
        )

# Since we want to test our cursor, we create a window for it ^_^
window = xproto.Window.create_toplevel_on_screen(conn, screen,
        cursor=cursor,
        back_pixel=screen.white_pixel,
        event_mask=xproto.EventMask.Exposure)

window.map()

conn.flush()

@window.event
def on_expose(evt):
    window.clear_area(0, 0, 640, 480)
    conn.flush()

while True:
    conn.wait_for_event().dispatch()

conn.disconnect()
