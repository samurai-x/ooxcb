import keyword

def prefix_if_needed(name):
    """
        prefix `name` with a '_' if it's a reserved
        word or starts with a number or is 'None'.
    """
    if (keyword.iskeyword(name)
            or name[0].isdigit()
            or name == 'None'):
        name = '_' + name
    return name

