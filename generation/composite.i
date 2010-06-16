ImportCode:
    - "from ooxcb.protocol.xproto import Window"
    - "from ooxcb.protocol.xfixes import Region"

ExternallyWrapped:
    - WINDOW
    - REGION

Mixins:
    WINDOW: Window
    REGION: Region

Requests:
    RedirectWindow:
        name: redirect
        subject: window
        defaults:
            update: Redirect.Automatic

    RedirectSubwindows:
        name: redirect_subwindows
        subject: window
        defaults:
            update: Redirect.Automatic

    UnredirectWindow:
        name: unredirect
        subject: window
        defaults:
            update: Redirect.Automatic

    UnredirectSubwindows:
        name: unredirect_subwindows
        subject: window
        defaults:
            update: Redirect.Automatic

    #CreateRegionFromBorderClip

    NameWindowPixmap:
        name: name_pixmap
        subject: window

    GetOverlayWindow:
        subject: window

    ReleaseOverlayWindow:
        subject: window

Classes:
    RegionMixin:
        - classmethod:
            name: create_from_border_clip
            arguments: [conn, window]
            code:
                - "rid = conn.generate_id()"
                - "region = cls(conn, rid)"
                - "conn.composite.create_region_from_border_clip_checked(region, window).check()"
                - "conn.add_to_cache(rid, region)"
                - "return region"

# vim: ft=yaml
