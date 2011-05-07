ResourceClasses:
    - CONTEXT

Xizers:
    ClientSpecs:
        type: seq
        seq_in: client_specs
        seq_out: client_specs
        length_out: num_client_specs

    Ranges:
        type: seq
        seq_in: ranges
        seq_out: ranges
        length_out: num_ranges

ClassAliases:
    ClientInfo: ClientInfo
    ExtRange: ExtRange
    ElementHeader: ElementHeader

Requests:
    CreateContext:
        arguments: ["context", "element_header", "client_specs", "ranges"]
        precode:
            - !xizer "ClientSpecs"
            - !xizer "Ranges"
    RegisterClients:
        subject: context
        arguments: ["element_header", "client_specs", "ranges"]
        precode:
            - !xizer "ClientSpecs"
            - !xizer "Ranges"
    UnregisterClients:
        subject: context
        arguments: ["client_specs"]
        precode:
            - !xizer "ClientSpecs"
    GetContext:
        subject: context
        name: get
    EnableContext:
        subject: context
        name: enable
    DisableContext:
        subject: context
        name: disable
    FreeContext:
        subject: context
        name: free

Classes:
    Context:
        - classmethod:
            name: create
            arguments: ["conn", "element_header", "client_specs", "ranges"]
            code:
                - "xid = conn.generate_id()"
                - "ctx = Context(conn, xid)"
                - "conn.record.create_context_checked(ctx, element_header, client_specs, ranges).check()"
                - "conn.add_to_cache(xid, ctx)"
                - "return ctx"

    Range:
        - classmethod:
            name: create
            arguments: [conn, core_requests, core_replies, ext_requests, ext_replies, delivered_events, device_events, errors, client_started, client_died]
            code:
                - "self = cls(conn)"
                - "self.core_requests = Range8.create(conn, *core_requests)"
                - "self.core_replies = Range8.create(conn, *core_replies)"
                - "self.ext_requests = ExtRange.create(conn, *ext_requests)"
                - "self.ext_replies = ExtRange.create(conn, *ext_replies)"
                - "self.delivered_events = Range8.create(conn, *delivered_events)"
                - "self.device_events = Range8.create(conn, *device_events)"
                - "self.errors = Range8.create(conn, *errors)"
                - "self.client_started = client_started"
                - "self.client_died = client_died"
                - "return self"
    Range8:
        - classmethod:
            name: create
            arguments: [conn, first, last]
            code:
                - "self = cls(conn)"
                - "self.first = first"
                - "self.last = last"
                - "return self"
    Range16:
        - classmethod:
            name: create
            arguments: [conn, first, last]
            code:
                - "self = cls(conn)"
                - "self.first = first"
                - "self.last = last"
                - "return self"
    ExtRange:
        - classmethod:
            name: create
            arguments: [conn, major_first, major_last, minor_first, minor_last]
            code:
                - "self = cls(conn)"
                - "self.major = Range8.create(conn, major_first, major_last)"
                - "self.minor = Range16.create(conn, minor_first, minor_last)"
                - "return self"
    Category:
        - attribute:
            name: FromServer
            value: 0
        - attribute:
            name: FromClient
            value: 1
        - attribute:
            name: ClientStarted
            value: 2
        - attribute:
            name: ClientDied
            value: 3
        - attribute:
            name: StartOfData
            value: 4
        - attribute:
            name: EndOfData
            value: 5
# vim: ft=yaml
