class _Indent(object):
    def __repr__(self):
        return '<Indent instruction>'

class _Dedent(object):
    def __repr__(self):
        return '<Dedent instruction>'

INDENT = _Indent()
DEDENT = _Dedent()

class Codegen(object):
    def __init__(self):
        self.buf = ''
        self.indent_level = 0

    def __call__(self, fmt=''):
        if callable(fmt): # callable. call.
            self(fmt())
            return self
        elif isinstance(fmt, (list, tuple)):
            map(self, fmt)
            return self

        if fmt is INDENT:
            self.indent()
        elif fmt is DEDENT:
            self.dedent()
        else:
            if not fmt:
                self.buf += '\n' # no unneeded indentation spaces
            else:
                self.buf += '    ' * self.indent_level + fmt + '\n'
        return self

    def indent(self, level=1):
        self.indent_level += level
        return self

    def dedent(self, level=1):
        self.indent_level -= level
        return self

class CodegenBase(object):
    def generate_code(self):
        """
            returns a list of lines
        """
        raise NotImplementedError()

    def generate_docs(self):
        """
            returns a list of lines
        """
        raise NotImplementedError()

