# -*- coding: utf-8 -*-

SENTINEL = object()


def filter_sentinel(obj):
    if isinstance(obj, list):
        return [arg for arg in obj if arg != SENTINEL]
    if isinstance(obj, tuple):
        return tuple(arg for arg in obj if arg != SENTINEL)
    if isinstance(obj, dict):
        return {key: val for key, val in obj.items() if val != SENTINEL}
    raise ValueError("Couldn't identify obj")
