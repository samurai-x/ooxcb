ImportCode:
    - "from ooxcb.protocol.xproto import Drawable, Screen"

ResourceClasses:
    - PICTURE
    - PICTFORMAT
    - GLYPHSET
    - CURSOR

ExternallyWrapped:
    - WINDOW
    - DRAWABLE
    - RECTANGLE

Ignored:
    - POINTFIX
    - FIXED

Mixins:
    DRAWABLE: Drawable
    SCREEN: Screen

Xizers:
    CP:
        type: values
        enum_name: CP
        values_dict_name: values
        xize:
            - alpha_map # TODO: can be none
            - clip_mask # TODO: can be None
            - dither # TODO: can be None

    RectanglesObjects:
        type: objects
        name: rectangles

    Rectangles:
        type: seq
        seq_in: rectangles
        length_out: rectangles_len
        seq_out: rectangles

Requests:
    QueryFilters:
        subject: drawable

    QueryPictIndexValues:
        subject: format

#    CreatePicture:

    ChangePicture:
        name: change
        subject: picture
        arguments:
            - "**values"
        precode:
            - !xizer "CP"

    SetPictureClipRectangles:
        name: set_clip_rectangles
        subject: picture
        doc: ":type rectangles: a list of :class:`Rectangle` instances"

    FreePicture:
        name: free
        subject: picture

    Composite:
        subject: src
        defaults:
            src_x: 0
            src_y: 0
            mask_x: 0
            mask_y: 0
            dst_x: 0
            dst_y: 0

    FillRectangles:
        subject: dst
        doc: ":type rects: a list of :class:`Rectangle` instances\n:type color: :class:`Color`"

    Trapezoids:
        subject: src
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    Triangles:
        subject: src
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    TriStrip:
        subject: src
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    TriFan:
        subject: src
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    CompositeGlyphs8:
        subject: src
        # TODO: no idea about the rest
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    CompositeGlyphs16:
        subject: src
        # TODO: no idea about the rest
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    CompositeGlyphs32:
        subject: src
        # TODO: no idea about the rest
        defaults:
            src_x: 0
            src_y: 0
            mask_format: None

    SetPictureTransform:
        subject: picture
        name: set_transform

    SetPictureFilter:
        subject: picture
        name: set_filter

    AddTraps:
        subject: picture
        defaults:
            x_off: 0
            y_off: 0

    # GlyphSet methods

    ReferenceGlyphSet:
        subject: gsid
        name: reference

    FreeGlyphSet:
        subject: glyphset
        name: free

    AddGlyphs:
        subject: glyphset
        # TODO: no idea how the `glyphs` and `glyphids` parameters work?

    FreeGlyphs:
        subject: glyphset


Classes:
    GlyphSet:
        - classmethod:
            name: create
            arguments: ["conn", "format"]
            code:
                - "gsid = conn.generate_id()"
                - "gs = cls(conn, gsid)"
                - "conn.render.create_glyph_set_checked(gs, format).check()"
                - "conn.add_to_cache(gsid, gs)"
                - "return gs"
    Picture:
        - classmethod:
            name: create
            arguments: ["conn", "drawable", "format", "**values"]
            code:
                - "pid = conn.generate_id()"
                - "pict = cls(conn, pid)"
                - !xizer "CP"
                - "conn.render.create_picture_checked(pict, drawable, format, value_mask, value_list).check()"
                - "conn.add_to_cache(pid, pict)"
                - "return pict"

        - classmethod:
            name: create_solid_fill
            arguments: ["conn", "color"]
            code:
                - "pid = conn.generate_id()"
                - "pict = cls(conn, pid)"
                - "conn.render.create_solid_fill_checked(pict, color).check()"
                - "conn.add_to_cache(pid, pict)"
                - "return pict"

        - classmethod:
            name: create_linear_gradient
            arguments: [p1, p2, num_stops, stops, colors]
            code:
                - "pid = conn.generate_id()"
                - "pict = cls(conn, pid)"
                - "conn.render.create_linear_gradient_checked(pict, p1, p2, num_stops, stops, colors).check()"
                - "conn.add_to_cache(pid, pict)"
                - "return pict"

        - classmethod:
            name: create_radial_gradient
            arguments: [p1, p2, num_stops, stops, colors]
            code:
                - "pid = conn.generate_id()"
                - "pict = cls(conn, pid)"
                - "conn.render.create_radial_gradient_checked(pict, inner, outer, inner_radius, outer_radius, num_stops, stops, colors).check()"
                - "conn.add_to_cache(pid, pict)"
                - "return pict"

        - classmethod:
            name: create_conical_gradient
            arguments: [center, angle, num_stops, stops, colors]
            code:
                - "pid = conn.generate_id()"
                - "pict = cls(conn, pid)"
                - "conn.render.create_conical_gradient_checked(pict,p1, p2, num_stops, stops, colors).check()"
                - "conn.add_to_cache(pid, pict)"
                - "return pict"

    Color:
        - classmethod:
            name: create
            arguments: ["conn", "red", "green", "blue", "alpha"]
            code:
                - "self = cls(conn)"
                - "self.red = red"
                - "self.green = green"
                - "self.blue = blue"
                - "self.alpha = alpha"
                - "return self"

    Cursor:
        - classmethod:
            name: create
            arguments: ["conn", "source", "x=0", "y=0"]
            code:
                - "cid = conn.generate_id()"
                - "cursor = cls(conn, cid)"
                - "conn.render.create_cursor_checked(cursor, source, x, y).check()"
                - "conn.add_to_cache(cid, cursor)"
                - "return cursor"

        - classmethod:
            name: create_anim
            arguments: ["cursors"]
            code:
                - "cid = conn.generate_id()"
                - "cursor = cls(conn, cid)"
                - "conn.render.create_anim_cursor_checked(cursor, cursors).check()"
                - "conn.add_to_cache(cid, cursor)"
                - "return cursor"

    ScreenMixin:
        - base: Mixin
        - method:
            name: get_render_pictformat
            code:
                - "reply = self.conn.render.query_pict_formats().reply()"
                - "screen_num = self.conn.setup.roots.index(self)"
                - "render_screen = reply.screens[screen_num]"
                - "for d in render_screen.depths:"
                - !indent
                - "if d.depth == self.root_depth:"
                - !indent
                - "for v in d.visuals:"
                - !indent
                - "if v.visual == self.root_visual:"
                - !indent
                - "return v.format"
                - !dedent
                - !dedent
                - !dedent
                - !dedent
                - 'raise Exception("Failed to find an appropriate Render pictformat!")' # TODO: better exception

# vim: ft=yaml
