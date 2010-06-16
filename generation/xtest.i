ImportCode:
    - "from ooxcb.protocol.xproto import Window"

ExternallyWrapped:
    - WINDOW
    - CURSOR

Mixins:
    WINDOW: Window

Requests:
    FakeInput:
        defaults:
            detail: 0
            time: 0
            window: None
            rootX: 0
            rootY: 0
            deviceid: 0
    CompareCursor:
        subject: window

# vim: ft=yaml
