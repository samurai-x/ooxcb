ImportCode:
    - "from ooxcb.protocol.xproto import Window"

ExternallyWrapped:
    - WINDOW
    - PIXMAP

Mixins:
    WINDOW: Window

Ignored:
    - KIND
    - OP

Requests:
    # Not wrapped:
    # QueryVersion
    Rectangles:
        name: shape_rectangles # TODO: really prefix?
        subject: destination_window
    
    Mask:
        name: shape_mask # TODO: really prefix?
        subject: destination_window

    Combine:
        name: shape_combine
        subject: destination_window

    Offset:
        name: shape_offset
        subject: destination_window

    QueryExtents:
        name: shape_query_extents
        subject: destination_window

    SelectInput:
        name: shape_select_input
        subject: destination_window

    InputSelected:
        name: shape_input_selected
        subject: destination_window

    GetRectangles:
        name: shape_get_rectangles
        subject: window
        
Events:
    Notify:
        member: affected_window

# vim: ft=yaml
