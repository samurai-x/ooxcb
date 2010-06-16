import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto, shape

shape.mixin()

conn = ooxcb.connect()
screen = conn.setup.roots[0]
win = xproto.Window.create_toplevel_on_screen(conn, screen,
        event_mask=xproto.EventMask.Exposure,
        back_pixel=screen.white_pixel,
        override_redirect=True)
win.map()

conn.flush()

pixmap = xproto.Pixmap.create(conn, win, 640, 480, 1)
gc = xproto.GContext.create(conn, pixmap, foreground=0, background=1)
gc.poly_fill_rectangle(pixmap, [xproto.Rectangle.create(conn, 0, 0, 640, 480)])
gc.change(foreground=1, background=1)
gc.poly_fill_rectangle(pixmap, [xproto.Rectangle.create(conn, 30, 30, 80, 80)])

win.shape_mask(
        shape.SO.Set,
        shape.SK.Bounding,
        0,
        0,
        pixmap)

conn.flush()

@win.event
def on_expose(evt):
    pass

while True:
    conn.wait_for_event().dispatch()
