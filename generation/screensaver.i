ImportCode:
    - "from ooxcb.protocol.xproto import Drawable, Window"

ExternallyWrapped:
    - DRAWABLE
    - WINDOW

Mixins:
    DRAWABLE: Drawable
    WINDOW: Window

Xizers:  
    CW:
        type: values
        enum_name: CW
        values_dict_name: values
        xize:
            - back_pixmap
            - cursor
            - colormap
    # TODO: see xproto.i
  
Requests:
    # Not wrapped: QueryVersion
    QueryInfo:
        subject: drawable
    SelectInput:
        subject: drawable
    SetAttributes:
        subject: drawable
        attributes: ["x", "y", "width", "height", "border_width", "_class", "depth", "visual", "**values"]
        precode:
            - !xizer "CW"
    UnsetAttributes:
        subject: drawable
    Suspend:
        _: _ # bla bla.

Events:
    Notify:
        member: window

# vim: ft=yaml
