from pwdgenerator.password import Password
from random import choice
from math import ceil, log


class Generator:

    def __init__(self, *args: str):
        self.sink = ''.join(args)
        self.min_length = None

    @property
    def sink(self):
        return self.__sink

    @sink.setter
    def sink(self, string: str):
        self.__sink = string

    def set_min_length(self, min):
        self.min_length = min

    def generate_by_length(self, length):
        return ''.join(choice(self.sink) for _ in range(length))

    def generate_by_params(self, P, V, T, sink: str = None):
        sink = sink if isinstance(sink, str) else self.sink
        A, S = len(sink), V.inMinutes * T.inMinutes / P
        L = int(log(S) / log(A)) + 1
        if self.min_length is not None and self.min_length > L:
            L = self.min_length
        return Password(self.generate_by_length(L), A=A, P=P, V=V, T=T)
