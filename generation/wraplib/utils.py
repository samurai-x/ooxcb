import re

def pythonize_camelcase_name(name):
    """
        GetProperty -> get_property
    """
    def repl(match):
        return '_' + match.group(0).lower()

    s = re.sub(r'([A-Z])', repl, name)
    if s.startswith('_'):
        return s[1:]
    else:
        return s

