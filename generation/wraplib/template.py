from string import Template

def template(tmpl, **kwargs):
    return Template(tmpl).safe_substitute(**kwargs)

