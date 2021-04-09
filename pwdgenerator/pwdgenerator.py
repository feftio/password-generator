from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice
from math import ceil, log
from duration import Duration
from speed import Speed


class PasswordGenerator:

    def __init__(self, *args: str):
        self.sink = ''.join(args)

    @property
    def sink(self):
        return self.__sink

    @sink.setter
    def sink(self, string: str):
        self.__sink = string

    def generate_by_length(self, length):
        return ''.join(choice(self.sink) for _ in range(length))

    def generate_by_params(self, P, V, T, _sink: str = None):
        sink = _sink if isinstance(_sink, str) else self.sink
        S = V.inMinutes * T.inMinutes / P
        # return log(S, len(sink))
        return log(S, 36)


if __name__ == '__main__':
    password_generator = PasswordGenerator(ascii_letters, digits, punctuation)
    # print(Duration(weeks=Speed(1).aHour).inMinutes)
    print(password_generator.generate_by_params(
        P=10**(-6), V=Speed(10).aMinute, T=Duration(weeks=1)))
