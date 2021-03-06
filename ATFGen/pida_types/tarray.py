from abc_type import IdaTypes
from serializer_ida_type import serialize_to_string
from ida_types import IDA_TYPES


class IdaTArray(IdaTypes):
    def __init__(self, ida_type=IDA_TYPES['array']):
        self.ida_type = {'idt': ida_type, 'value': {'count': 0, 'type': None}}

    def decode(self, data):
        import ida_decoder

        count = ord(data[0])
        offset = 1
        if count > 0x80:
            count = 0x80 * ord(data[1])
            count |= ~(0x80 - ord(data[0]))
            offset = 2

        rbyte, value = ida_decoder.decode_step(ida_type=data[offset:])
        offset += rbyte
        self.ida_type['value']['count'] = count
        self.ida_type['value']['type'] = value
        return offset

    def get_type(self):
        return self.ida_type

    def to_string(self, session):
        return serialize_to_string(self.ida_type['value']['type'], session).format(ptr='*{ptr}', name='{name}')

    def from_dict(self, data):
        self.ida_type = data
