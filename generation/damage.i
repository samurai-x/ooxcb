ImportCode:
    - "from ooxcb.protocol.xproto import Drawable"

Mixins:
    DRAWABLE: Drawable

ExternallyWrapped:
    - DRAWABLE
    - REGION

ResourceClasses:
    - DAMAGE

Requests:
    Destroy:
        subject: damage

    Subtract:
        subject: damage

    Add:
        subject: drawable
        name: damage_add # TODO: mixin??

Events:
    Notify:
        member: drawable
        classname: DamageNotifyEvent
        eventname: on_damage_notify

Classes:
    Damage:
        - classmethod:
            name: create
            arguments: [conn, drawable, level]
            code:
                - "did = conn.generate_id()"
                - "damage = cls(conn, did)"
                - "conn.damage.create_checked(damage, drawable, level).check()"
                - "conn.add_to_cache(did, damage)"
                - "return damage"

# vim: ft=yaml
