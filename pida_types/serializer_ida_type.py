def serialize_to_string(idt, session):
    from pida_types import binding
    obj = binding.PIDA_TYPES[idt['idt']](idt['idt'])
    obj.from_dict(idt)

    return obj.to_string(session)
