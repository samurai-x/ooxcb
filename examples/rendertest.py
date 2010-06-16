from __future__ import with_statement

import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto, render

# use the render mixin
render.mixin()

conn = ooxcb.connect()

def find_format(realscreen, screen):
    for d in screen.depths:
        if d.depth == realscreen.root_depth:
            for v in d.visuals:
                if v.visual == realscreen.root_visual:
                    return v.format

    raise Exception("Failed to find an appropriate Render pictformat!")

def main():
    screen = conn.setup.roots[conn.pref_screen]

    win = xproto.Window.create_toplevel_on_screen(conn, screen,
            back_pixel=screen.white_pixel,
            event_mask=xproto.EventMask.Exposure | xproto.EventMask.ButtonPress
    )

    with conn.bunch():
        reply = conn.render.query_pict_formats().reply()
        format = find_format(screen, reply.screens[conn.pref_screen])
        picture = render.Picture.create(conn, win, format)
        win.map()

    @win.event
    def on_button_press(evt):
        sys.exit()

    @win.event
    def on_expose(evt):
        win.clear_area(0, 0, 0, 0)

        #for x in xrange(0, 7):
        #    for y in xrange(0, 5):
        #        rectangle = xproto.Rectangle.create(conn, (x + 1) * 24 + x * 64, (y + 1) * 24 + y * 64, 64, 64)
        #        color = render.Color.create(conn, x * 65535 / 7, y * 65535 / 5, (x * y) * 65535 / 35, 65535)
        #        picture.fill_rectangles(render.PictOp.Src, color, [rectangle])

        pic = render.Picture.create_solid_fill(conn, render.Color.create(conn, 65535, 0, 0, 65535))
        pic.composite(render.PictOp.Src, None, picture, 300, 300)
        conn.flush()


    while 1:
        conn.wait_for_event().dispatch()

if __name__ == '__main__':
    try:
        main()
    finally:
        conn.disconnect()
