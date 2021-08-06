from __future__ import annotations
import typing as t


def stuple(value):
    return tuple(sfun(value))


def slist(value):
    return list(sfun(value))


def sfun(value):
    if isinstance(value, (list, tuple, set)):
        return list(itemstostr(value))
    if not isinstance(value, (str, int, float)):
        raise TypeError
    return str(value) if isinstance(value, (int, float)) else value


def itemstostr(collection):
    if not isinstance(collection, (list, tuple, set)):
        raise TypeError('The argument has to be a collection.')
    _type = type(collection)
    collection = list(collection)
    for i in range(len(collection)):
        if isinstance(collection[i], (str, int, float)):
            collection[i] = str(collection[i])
        else:
            raise TypeError
    return _type(collection)


def lower(value) -> list:
    if not isinstance(value, list):
        value = list(value)
    for i in range(len(value)):
        value[i] = value[i].lower()
    return value


if __name__ == '__main__':
    pass
