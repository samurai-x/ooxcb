from .names import prefix_if_needed

class Struct(object):
    def __init__(self):
        self.renew()

    def renew(self):
        self.fields = []
        self.size = 0
        self.fmt = ''

    def flush(self):
        ret = (self.fields, self.size, self.fmt)
        self.renew()
        return ret

    def push_format(self, field):
        self.fmt += field.type.py_format_str
        self.fields.append(field)
        self.size += field.type.size

    def push_something(self, field, size, format):
        self.fmt += format
        self.fields.append(field)
        self.size += size

    def push_pad(self, size):
        self.fmt += size * 'x'
        self.size += size

