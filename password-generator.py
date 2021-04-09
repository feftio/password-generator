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
        S = V.inMinutes * T.inMinutes / P
        # return log(S, len(sink))
        return log(S, len(sink))


class Duration:

    def __init__(self, minutes=0, hours=0, days=0, weeks=0):
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.weeks = weeks
        self.value = None

    @property
    def inMinutes(self):
        minutes = self.minutes + (60 * self.hours) + \
            (1440 * self.days) + (10080 * self.weeks)
        return minutes if self.value is None else self.value / minutes

    @property
    def inHours(self):
        hours = (self.minutes / 60) + self.hours + \
            (24 * self.days) + (168 * self.weeks)
        return hours if self.value is None else self.value / hours

    @property
    def inDays(self):
        days = (self.minutes / 1440) + (self.hours / 24) + \
            self.days + (7 * self.weeks)
        return days if self.value is None else self.value / days

    @property
    def inWeeks(self):
        weeks = (self.minutes / 10080) + (self.hours / 168) + \
            (self.days / 7) + self.weeks
        return weeks if self.value is None else self.value / weeks

    def __rtruediv__(self, value: int):
        self.value = value
        return self


class Speed:

    def __init__(self, value):
        self.value = value

    @property
    def aMinute(self):
        return self.value / Duration(minutes=1)

    @property
    def aHour(self):
        return self.value / Duration(hours=1)

    @property
    def aDay(self):
        return self.value / Duration(days=1)

    @property
    def aWeek(self):
        return self.value / Duration(weeks=1)


if __name__ == '__main__':
    password_generator = PasswordGenerator(ascii_letters, digits, punctuation)
    # print(Duration(weeks=Speed(1).aHour).inMinutes)
    print(password_generator.generate_by_params(
        P=10**(-6), V=Speed(10).aMinute, T=Duration(weeks=1)))
    print(password_generator.generate_by_params(
        P=10**(-6), V=10/Duration(minutes=1), T=Duration(days=7)))
