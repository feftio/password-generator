from pwdgenerator.password import Password
from random import choice
from math import ceil, log
from typing import List, Callable, Type


def string_to_list(string: str):
    if not isinstance(string, str):
        return string
    return list(string)

def object_to_string(_object):
    if not isinstance(_object, str):
        return str(_object)
    return _object


class Generator:

    def __init__(self, symbols=[]):
        self.sink : List[str] = ''.join(symbols)
        self.min_length : int = None

    def generate_by_length(self, length):
        return ''.join(choice(self.sink) for _ in range(length))

    def generate_by_params(self, P, V, T, sink: str = None) -> Type[Password]:
        sink = sink if isinstance(sink, str) else self.sink
        A, S = len(sink), V.inMinutes * T.inMinutes / P
        L = int(log(S) / log(A)) + 1
        if self.min_length is not None and self.min_length > L:
            L = self.min_length
        return Password(self.generate_by_length(L), A=A, P=P, V=V, T=T)

    @staticmethod
    def generate_by_templates(templates : list[list]) -> str:
        password = []
        for i in range(len(templates)):
            templates[i] = string_to_list(templates[i])
            for j in range(len(templates[i])):
                templates[i][j] = object_to_string(templates[i][j])
            password.append(choice(templates[i]))
        return ''.join(password)