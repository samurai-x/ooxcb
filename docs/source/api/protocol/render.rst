ooxcb.protocol.render
=====================

.. module:: ooxcb.protocol.render

.. class:: BadGlyph

.. class:: PictFormatError

    .. method:: __init__(self, conn)


.. class:: Directformat

    .. method:: __init__(self, conn)


    .. attribute:: alpha_shift

    .. attribute:: blue_shift

    .. attribute:: red_shift

    .. attribute:: blue_mask

    .. attribute:: alpha_mask

    .. attribute:: green_mask

    .. attribute:: red_mask

    .. attribute:: green_shift

.. class:: ScreenMixin

    .. data:: target_class


    .. method:: get_render_pictformat(self)


.. class:: GlyphSetError

    .. method:: __init__(self, conn)


.. class:: BadPicture

.. class:: QueryVersionCookie

.. class:: Pictdepth

    .. method:: __init__(self, conn)


    .. attribute:: visuals

    .. attribute:: num_visuals

    .. attribute:: depth

.. class:: PictureError

    .. method:: __init__(self, conn)


.. class:: Picture

    .. method:: __init__(self, conn, xid)


    .. method:: change_checked(self, **values)


    .. method:: change(self, **values)


    .. method:: set_clip_rectangles_checked(self, clip_x_origin, clip_y_origin, rectangles)


    .. method:: set_clip_rectangles(self, clip_x_origin, clip_y_origin, rectangles)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. method:: composite_checked(self, op, mask, dst, width, height, src_x=0, src_y=0, mask_x=0, mask_y=0, dst_x=0, dst_y=0)


    .. method:: composite(self, op, mask, dst, width, height, src_x=0, src_y=0, mask_x=0, mask_y=0, dst_x=0, dst_y=0)


    .. method:: trapezoids_checked(self, op, dst, traps, mask_format=None, src_x=0, src_y=0)


    .. method:: trapezoids(self, op, dst, traps, mask_format=None, src_x=0, src_y=0)


    .. method:: triangles_checked(self, op, dst, triangles, mask_format=None, src_x=0, src_y=0)


    .. method:: triangles(self, op, dst, triangles, mask_format=None, src_x=0, src_y=0)


    .. method:: tri_strip_checked(self, op, dst, points, mask_format=None, src_x=0, src_y=0)


    .. method:: tri_strip(self, op, dst, points, mask_format=None, src_x=0, src_y=0)


    .. method:: tri_fan_checked(self, op, dst, points, mask_format=None, src_x=0, src_y=0)


    .. method:: tri_fan(self, op, dst, points, mask_format=None, src_x=0, src_y=0)


    .. method:: composite_glyphs8_checked(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0)


    .. method:: composite_glyphs8(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0)


    .. method:: composite_glyphs16_checked(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0)


    .. method:: composite_glyphs16(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0)


    .. method:: composite_glyphs32_checked(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0)


    .. method:: composite_glyphs32(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0)


    .. method:: fill_rectangles_checked(self, op, color, rects)


    .. method:: fill_rectangles(self, op, color, rects)


    .. method:: set_transform_checked(self, transform)


    .. method:: set_transform(self, transform)


    .. method:: set_filter_checked(self, filter, values)


    .. method:: set_filter(self, filter, values)


    .. method:: add_traps_checked(self, traps, x_off=0, y_off=0)


    .. method:: add_traps(self, traps, x_off=0, y_off=0)


    .. classmethod:: create(cls, conn, drawable, format, **values)


    .. classmethod:: create_solid_fill(cls, conn, color)


    .. classmethod:: create_linear_gradient(cls, p1, p2, num_stops, stops, colors)


    .. classmethod:: create_radial_gradient(cls, p1, p2, num_stops, stops, colors)


    .. classmethod:: create_conical_gradient(cls, center, angle, num_stops, stops, colors)


.. class:: Repeat

    .. data:: _None


    .. data:: Normal


    .. data:: Pad


    .. data:: Reflect


.. class:: Triangle

    .. method:: __init__(self, conn)


    .. attribute:: p2

    .. attribute:: p3

    .. attribute:: p1

.. class:: Glyphset

    .. method:: __init__(self, conn, xid)


    .. method:: reference_checked(self, existing)


    .. method:: reference(self, existing)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. method:: add_glyphs_checked(self, glyphids, glyphs, data)


    .. method:: add_glyphs(self, glyphids, glyphs, data)


    .. method:: free_glyphs_checked(self, glyphs)


    .. method:: free_glyphs(self, glyphs)


.. class:: Pictvisual

    .. method:: __init__(self, conn)


    .. attribute:: visual

    .. attribute:: format

.. class:: Spanfix

    .. method:: __init__(self, conn)


    .. attribute:: y

    .. attribute:: r

    .. attribute:: l

.. class:: DrawableMixin

    .. data:: target_class


    .. method:: query_filters(self)


    .. method:: query_filters_unchecked(self)


.. class:: PictOp

    .. data:: Clear


    .. data:: Src


    .. data:: Dst


    .. data:: Over


    .. data:: OverReverse


    .. data:: In


    .. data:: InReverse


    .. data:: Out


    .. data:: OutReverse


    .. data:: Atop


    .. data:: AtopReverse


    .. data:: Xor


    .. data:: Add


    .. data:: Saturate


    .. data:: DisjointClear


    .. data:: DisjointSrc


    .. data:: DisjointDst


    .. data:: DisjointOver


    .. data:: DisjointOverReverse


    .. data:: DisjointIn


    .. data:: DisjointInReverse


    .. data:: DisjointOut


    .. data:: DisjointOutReverse


    .. data:: DisjointAtop


    .. data:: DisjointAtopReverse


    .. data:: DisjointXor


    .. data:: ConjointClear


    .. data:: ConjointSrc


    .. data:: ConjointDst


    .. data:: ConjointOver


    .. data:: ConjointOverReverse


    .. data:: ConjointIn


    .. data:: ConjointInReverse


    .. data:: ConjointOut


    .. data:: ConjointOutReverse


    .. data:: ConjointAtop


    .. data:: ConjointAtopReverse


    .. data:: ConjointXor


.. class:: Pictscreen

    .. method:: __init__(self, conn)


    .. attribute:: depths

    .. attribute:: fallback

    .. attribute:: num_depths

.. class:: Animcursorelt

    .. method:: __init__(self, conn)


    .. attribute:: cursor

    .. attribute:: delay

.. class:: GlyphSet

    .. classmethod:: create(cls, conn, format)


.. class:: renderExtension

    .. data:: header


    .. method:: query_version(self, client_major_version, client_minor_version)


    .. method:: query_version_unchecked(self, client_major_version, client_minor_version)


    .. method:: query_pict_formats(self)


    .. method:: query_pict_formats_unchecked(self)


    .. method:: create_picture_checked(self, pid, drawable, format, value_mask, value_list)


    .. method:: create_picture(self, pid, drawable, format, value_mask, value_list)


    .. method:: create_glyph_set_checked(self, gsid, format)


    .. method:: create_glyph_set(self, gsid, format)


    .. method:: create_cursor_checked(self, cid, source, x, y)


    .. method:: create_cursor(self, cid, source, x, y)


    .. method:: create_anim_cursor_checked(self, cid, cursors)


    .. method:: create_anim_cursor(self, cid, cursors)


    .. method:: create_solid_fill_checked(self, picture, color)


    .. method:: create_solid_fill(self, picture, color)


    .. method:: create_linear_gradient_checked(self, picture, p1, p2, num_stops, stops, colors)


    .. method:: create_linear_gradient(self, picture, p1, p2, num_stops, stops, colors)


    .. method:: create_radial_gradient_checked(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors)


    .. method:: create_radial_gradient(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors)


    .. method:: create_conical_gradient_checked(self, picture, center, angle, num_stops, stops, colors)


    .. method:: create_conical_gradient(self, picture, center, angle, num_stops, stops, colors)


.. class:: Pictforminfo

    .. method:: __init__(self, conn)


    .. attribute:: colormap

    .. attribute:: depth

    .. attribute:: type

    .. attribute:: id

    .. attribute:: direct

.. class:: BadGlyphSet

.. class:: PictType

    .. data:: Indexed


    .. data:: Direct


.. class:: SubPixel

    .. data:: Unknown


    .. data:: HorizontalRGB


    .. data:: HorizontalBGR


    .. data:: VerticalRGB


    .. data:: VerticalBGR


    .. data:: _None


.. class:: Pointfix

    .. method:: __init__(self, conn)


    .. attribute:: y

    .. attribute:: x

.. class:: BadPictFormat

.. class:: Indexvalue

    .. method:: __init__(self, conn)


    .. attribute:: blue

    .. attribute:: alpha

    .. attribute:: green

    .. attribute:: pixel

    .. attribute:: red

.. class:: Cursor

    .. classmethod:: create(cls, conn, source, x=0, y=0)


    .. classmethod:: create_anim(cls, cursors)


.. class:: QueryPictIndexValuesReply

    .. method:: __init__(self, conn)


    .. attribute:: num_values

    .. attribute:: values

.. class:: QueryFiltersReply

    .. method:: __init__(self, conn)


    .. attribute:: aliases

    .. attribute:: filters

    .. attribute:: num_aliases

    .. attribute:: num_filters

.. class:: Linefix

    .. method:: __init__(self, conn)


    .. attribute:: p2

    .. attribute:: p1

.. class:: Trapezoid

    .. method:: __init__(self, conn)


    .. attribute:: top

    .. attribute:: left

    .. attribute:: right

    .. attribute:: bottom

.. class:: Trap

    .. method:: __init__(self, conn)


    .. attribute:: top

    .. attribute:: bot

.. class:: CP

    .. data:: Repeat


    .. data:: AlphaMap


    .. data:: AlphaXOrigin


    .. data:: AlphaYOrigin


    .. data:: ClipXOrigin


    .. data:: ClipYOrigin


    .. data:: ClipMask


    .. data:: GraphicsExposure


    .. data:: SubwindowMode


    .. data:: PolyEdge


    .. data:: PolyMode


    .. data:: Dither


    .. data:: ComponentAlpha


.. class:: QueryPictIndexValuesCookie

.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: major_version

    .. attribute:: minor_version

.. class:: PictOpError

    .. method:: __init__(self, conn)


.. class:: Glyphinfo

    .. method:: __init__(self, conn)


    .. attribute:: x_off

    .. attribute:: height

    .. attribute:: width

    .. attribute:: y

    .. attribute:: x

    .. attribute:: y_off

.. class:: QueryPictFormatsCookie

.. class:: PolyEdge

    .. data:: Sharp


    .. data:: Smooth


.. class:: Color

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, red, green, blue, alpha)


    .. attribute:: blue

    .. attribute:: alpha

    .. attribute:: green

    .. attribute:: red

.. class:: BadPictOp

.. class:: GlyphError

    .. method:: __init__(self, conn)


.. class:: Transform

    .. method:: __init__(self, conn)


    .. attribute:: matrix21

    .. attribute:: matrix23

    .. attribute:: matrix22

    .. attribute:: matrix11

    .. attribute:: matrix12

    .. attribute:: matrix13

    .. attribute:: matrix32

    .. attribute:: matrix33

    .. attribute:: matrix31

.. class:: Pictformat

    .. method:: __init__(self, conn, xid)


    .. method:: query_pict_index_values(self)


    .. method:: query_pict_index_values_unchecked(self)


.. class:: QueryFiltersCookie

.. class:: PolyMode

    .. data:: Precise


    .. data:: Imprecise


.. class:: QueryPictFormatsReply

    .. method:: __init__(self, conn)


    .. attribute:: num_formats

    .. attribute:: num_subpixel

    .. attribute:: screens

    .. attribute:: num_screens

    .. attribute:: formats

    .. attribute:: num_visuals

    .. attribute:: num_depths

    .. attribute:: subpixels

.. class:: Glyph

    .. method:: __init__(self, conn, xid)


