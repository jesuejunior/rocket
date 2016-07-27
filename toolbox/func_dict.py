# encoding: utf-8


def ordered(obj):
    """Ordering a dict object
    :param obj:
    :return obj:
    """
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj
