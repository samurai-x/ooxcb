ooxcb.protocol.shape
====================

.. module:: ooxcb.protocol.shape

.. class:: shapeExtension

    .. data:: header


    .. method:: query_version(self)


    .. method:: query_version_unchecked(self)


.. class:: WindowMixin

    .. data:: target_class


    .. method:: shape_rectangles_checked(self, operation, destination_kind, ordering, x_offset, y_offset, rectangles)


    .. method:: shape_rectangles(self, operation, destination_kind, ordering, x_offset, y_offset, rectangles)


    .. method:: shape_mask_checked(self, operation, destination_kind, x_offset, y_offset, source_bitmap)


    .. method:: shape_mask(self, operation, destination_kind, x_offset, y_offset, source_bitmap)


    .. method:: shape_combine_checked(self, operation, destination_kind, source_kind, x_offset, y_offset, source_window)


    .. method:: shape_combine(self, operation, destination_kind, source_kind, x_offset, y_offset, source_window)


    .. method:: shape_offset_checked(self, destination_kind, x_offset, y_offset)


    .. method:: shape_offset(self, destination_kind, x_offset, y_offset)


    .. method:: shape_query_extents(self)


    .. method:: shape_query_extents_unchecked(self)


    .. method:: shape_select_input_checked(self, enable)


    .. method:: shape_select_input(self, enable)


    .. method:: shape_input_selected(self)


    .. method:: shape_input_selected_unchecked(self)


    .. method:: shape_get_rectangles(self, source_kind)


    .. method:: shape_get_rectangles_unchecked(self, source_kind)


.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: major_version

    .. attribute:: minor_version

.. class:: QueryVersionCookie

.. class:: NotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: server_time

    .. attribute:: shaped

    .. attribute:: extents_y

    .. attribute:: extents_x

    .. attribute:: affected_window

    .. attribute:: extents_height

    .. attribute:: extents_width

    .. attribute:: shape_kind

    .. attribute:: response_type

.. class:: GetRectanglesReply

    .. method:: __init__(self, conn)


    .. attribute:: ordering

    .. attribute:: rectangles

    .. attribute:: rectangles_len

.. class:: QueryExtentsCookie

.. class:: SK

    .. data:: Bounding


    .. data:: Clip


    .. data:: Input


.. class:: SO

    .. data:: Set


    .. data:: Union


    .. data:: Intersect


    .. data:: Subtract


    .. data:: Invert


.. class:: InputSelectedReply

    .. method:: __init__(self, conn)


    .. attribute:: enabled

.. class:: QueryExtentsReply

    .. method:: __init__(self, conn)


    .. attribute:: clip_shape_extents_width

    .. attribute:: bounding_shape_extents_y

    .. attribute:: bounding_shaped

    .. attribute:: bounding_shape_extents_width

    .. attribute:: bounding_shape_extents_height

    .. attribute:: clip_shape_extents_y

    .. attribute:: clip_shape_extents_x

    .. attribute:: clip_shape_extents_height

    .. attribute:: clip_shaped

    .. attribute:: bounding_shape_extents_x

.. class:: GetRectanglesCookie

.. class:: InputSelectedCookie

