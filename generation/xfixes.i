ImportCode:
    - "from ooxcb.protocol.xproto import Window, GContext, Cursor"
    - "from ooxcb.protocol.render import Picture"

ExternallyWrapped:
    - WINDOW
    - PIXMAP
    - PICTURE
    - GCONTEXT
    - CURSOR

ResourceClasses:
    - REGION
    - WINDOW
    - PIXMAP
    - GCONTEXT
    - CURSOR
    - PICTURE

Xizers:
    RectanglesObjects:
        type: objects
        name: rectangles

    Rectangles:
        type: seq
        seq_in: rectangles
        length_out: rectangles_len
        seq_out: rectangles

    CursorName:
        type: string
        seq_in: name
        seq_out: name
        length_out: nbytes

Mixins:
    WINDOW: Window
    GCONTEXT: GContext
    PICTURE: Picture
    CURSOR: Cursor

Requests:
    # Intentionally unwrapped:
    # GetCursorImage
    # GetCursorName
    # GetCursorImageAndName
    # CreateRegion

    ChangeSaveSet:
        subject: window

    SelectSelectionInput:
        subject: window

    SelectCursorInput:
        subject: window

    DestroyRegion:
        subject: region
        name: destroy

    SetRegion:
        subject: region
        name: set

    # TODO: some convenience methods for copying & stuff

    CopyRegion:
        # TODO: does *destination* have to be a free XID?
        subject: source
        name: copy

    UnionRegion:
        # TODO: does *destination* have to be a free XID?
        subject: source1
        name: union

    IntersectRegion:
        # TODO: does *destination* have to be a free XID?
        subject: source1
        name: intersect

    SubtractRegion:
        # TODO: does *destination* have to be a free XID?
        subject: source1
        name: subtract

    InvertRegion:
        # TODO: does *destination* have to be a free XID?
        subject: source
        name: invert

    TranslateRegion:
        subject: region
        name: translate

    RegionExtents:
         # TODO: does *destination* have to be a free XID?
        subject: source
        name: extents

    FetchRegion:
        subject: region
        name: fetch

    SetGCClipRegion:
        # TODO: should that really be a GContext mixin?
        subject: gc
        name: set_clip_region

    SetWindowShapeRegion:
        # TODO: Window mixin, really?
        subject: dest
        name: set_shape_region

    SetPictureClipRegion:
        # TODO: really a Picture mixin ...?
        subject: picture
        name: set_clip_region

    ExpandRegion:
        # TODO: does *destination* have to be a free XID?
        subject: source
        name: expand

    # Cursor methods

    SetCursorName:
        subject: cursor
        arguments: [name]
        name: set_name
        initcode:
            - !xizer "CursorName"

    ChangeCursor:
        subject: source # TODO: I am not sure if that subject is intuitive.
        name: change

    ChangeCursorByName:
        subject: src # TODO: I am not sure if that subject is intuitive.
        name: change_by_name
        arguments: [name]
        initcode:
            - !xizer "CursorName"

    HideCursor:
        subject: window # TODO: really a mixin?

    ShowCursor:
        subject: window # TODO: really a mixin?

Events:
    SelectionNotify:
        member: owner # TODO: not sure if `owner` or `window`

    CursorNotify:
        member: window

Classes:
    Region:
        - classmethod:
            name: create
            arguments: ["conn", "rectangles"]
            code:
                - "rid = conn.generate_id()"
                - "region = cls(conn, rid)"
                - "conn.xfixes.create_region_checked(region, rectangles).check()"
                - "conn.add_to_cache(rid, region)"
                - "return region"

        - classmethod:
            name: create_from_bitmap
            arguments: ["conn", "bitmap"]
            code:
                - "rid = conn.generate_id()"
                - "region = cls(conn, rid)"
                - "conn.xfixes.create_region_from_bitmap_checked(region, bitmap).check()"
                - "conn.add_to_cache(rid, region)"
                - "return region"

        - classmethod:
            name: create_from_window
            arguments: ["conn", "window", "kind"]
            code:
                - "rid = conn.generate_id()"
                - "region = cls(conn, rid)"
                - "conn.xfixes.create_region_from_window_checked(region, window, kind).check()"
                - "conn.add_to_cache(rid, region)"
                - "return region"

        - classmethod:
            name: create_from_gc
            arguments: ["conn", "gc"]
            code:
                - "rid = conn.generate_id()"
                - "region = cls(conn, rid)"
                - "conn.xfixes.create_region_from_g_c_checked(region, gc).check()"
                - "conn.add_to_cache(rid, region)"
                - "return region"

        - classmethod:
            name: create_from_picture
            arguments: ["conn", "picture"]
            code:
                - "rid = conn.generate_id()"
                - "region = cls(conn, rid)"
                - "conn.xfixes.create_region_from_picture_checked(region, picture).check()"
                - "conn.add_to_cache(rid, region)"
                - "return region"

# vim: ft=yaml
