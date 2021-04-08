from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice
from math import ceil, log


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

    def generate_by_params(self, P, V, T, _sink=None):
        sink = _sink if isinstance(_sink, str) else self.sink
        S = V * T.inMinutes / P
        # return log(S, len(sink))
        return log(S, 36)


class Duration:

    def __init__(self, minutes=0, hours=0, days=0, weeks=0):
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.weeks = weeks

    @property
    def inMinutes(self):
        return self.minutes + (60 * self.hours) + (1440 * self.days) + (10080 * self.weeks)

    @property
    def inHours(self):
        return (self.minutes / 60) + self.hours + (24 * self.days) + (168 * self.weeks)

    @property
    def inDays(self):
        return (self.minutes / 1440) + (self.hours / 24) + self.days + (7 * self.weeks)

    @property
    def inWeeks(self):
        return (self.minutes / 10080) + (self.hours / 168) + (self.days / 7) + self.weeks


class Speed:

    def __init__(self, value):
        self.value = value
        self.type = None

    @property
    def aMinute(self):
        return Converter(self.value, [1, 1 / 60, 1440, 10080])

    @property
    def aHour(self):
        return Converter(self.value, [1 / 60, 1, 24, 168])

    @property
    def aDay(self):
        return Converter(self.value, [1 / 1440, 1 / 24, 1, 7])

    @property
    def aWeek(self):
        return Converter(self.value, [1 / 10080, 1 / 168, 1 / 7, 1])


class Converter():

    def __init__(self, value, rules):
        self.value = value
        self.rules = rules

    @property
    def toMinutes(self):
        return self.value * self.rules[0]

    @property
    def toHours(self):
        return self.value * self.rules[1]


if __name__ == '__main__':
    password_generator = PasswordGenerator(ascii_letters, digits, punctuation)
    # print(Duration(weeks=Speed(1).aHour).inMinutes)
    # print(password_generator.generate_by_params(
    #     P=10**(-6), V=Speed(10).aWeek, T=Duration(weeks=1)))
    print(Speed(10).aDay.toMinutes)
