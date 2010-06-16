import imp
import os

def import_interface(modname):
    """
        load the `$modname.i.py` module and return it.
    """
    iname = '%s.i' % modname
    
    fil = open(os.path.abspath('%s.py' % iname), 'r')
    try:
        return imp.load_module('interface', fil, iname, ('.py', 'r', imp.PY_SOURCE))
    finally:
        fil.close()

class InterfaceProxy(object):
    def __init__(self, default, custom):
        self.default = default
        self.custom = custom

    def __getattr__(self, name):
        if hasattr(self.custom, name):
            return getattr(self.custom, name)
        else:
            return getattr(self.default, name)

