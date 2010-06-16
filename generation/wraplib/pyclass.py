from .codegen import CodegenBase, INDENT, DEDENT
from .template import template
from .pymember import PyMethod, PyAttribute

class PyClass(CodegenBase):
    def __init__(self, name, base='object', order=100):
        self.name = name
        self.base = base
        self.members = []
        self.instance_attributes = {}
        self.order = order

    def add_member(self, member):
        self.members.append(member)

    def get_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise KeyError(name)

    def new_method(self, name):
        ret = PyMethod(name)
        self.members.append(ret)
        return ret

    def new_attribute(self, name, value):
        ret = PyAttribute(name, value)
        self.members.append(ret)
        return ret

    def add_instance_attribute(self, name, description):
        self.instance_attributes[name] = description

    def generate_code(self):
        code = [
            template('class $name($base):',
                name = self.name,
                base = self.base
            ),
            INDENT]
        if not self.members:
            code.append('pass')
        else:
            for member in self.members:
                code += member.generate_code()
        if code[-1] != '': # force a newline
            code.append('')
        code.append(DEDENT)
        return code

    def generate_docs(self):
        return ['.. class:: %s' % self.name, '',
                INDENT,
                    [m.generate_docs() for m in self.members if m.name not in ('read', 'build')], # do not document read and build
                    [['.. attribute:: %s' % name, INDENT,
                        desc, DEDENT]
                    for name, desc in self.instance_attributes.iteritems()],
                DEDENT]

