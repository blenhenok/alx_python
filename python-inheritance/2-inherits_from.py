"""Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class"""
def inherits_from(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)