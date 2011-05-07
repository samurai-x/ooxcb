from __future__ import with_statement

import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto
from ooxcb.contrib import cairo

conn = ooxcb.connect()
screen = conn.setup.roots[conn.pref_screen]
visualtype = screen.get_root_visual_type()
width = 640
height = 480
running = True

with conn.bunch():
    win = xproto.Window.create_toplevel_on_screen(conn, screen,
            width=width, height=height,
            back_pixel=screen.white_pixel,
            event_mask=xproto.EventMask.Exposure | xproto.EventMask.ButtonPress
    )
    win.map()

    # create a surface for this window
    surface = cairo.cairo_xcb_surface_create(conn, win,
            visualtype,
            width, height)
    
    # and a cairo context
    cr = cairo.cairo_create(surface)
    cairo.cairo_set_operator(cr, cairo.CAIRO_OPERATOR_SOURCE)
    cairo.cairo_set_source_surface(cr, surface, 0, 0)
    cairo.cairo_set_source_rgba(cr, 255, 0, 0, 0)

@win.event
def on_expose(event):
    # paint a red rectangle when an expose event occurs
    cairo.cairo_set_source_rgb(cr, 255, 0, 0)
    cairo.cairo_rectangle(cr, 100, 100, 300, 300)
    cairo.cairo_fill(cr)
    # don't forget to flush!
    conn.flush()

@win.event
def on_button_press(event):
    global running
    running = False

while 1:
    conn.wait_for_event().dispatch()
    if not running:
        break

conn.disconnect()
