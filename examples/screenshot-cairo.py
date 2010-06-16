import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto
from ooxcb.contrib import cairo

conn = ooxcb.connect()
screen = conn.setup.roots[conn.pref_screen]
root = screen.root

surface = cairo.cairo_xcb_surface_create(conn, root,
        screen.get_root_visual_type(),
        screen.width_in_pixels,
        screen.height_in_pixels)
cairo.cairo_surface_write_to_png(surface, "screenshot.png")

conn.disconnect()
