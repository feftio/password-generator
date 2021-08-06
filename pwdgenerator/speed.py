from __future__ import annotations
import typing as t
from pwdgenerator.duration import Duration


class Speed:
    def __init__(self, value: float):
        self.value: float = value

    @property
    def aMinute(self) -> Duration:
        return self.value / Duration(minutes=1)

    @property
    def aHour(self) -> Duration:
        return self.value / Duration(hours=1)

    @property
    def aDay(self) -> Duration:
        return self.value / Duration(days=1)

    @property
    def aWeek(self) -> Duration:
        return self.value / Duration(weeks=1)


if __name__ == '__main__':
    print(Speed(60).aHour * Duration(hours=1))
    print(Duration(hours=1) * (60 / Duration(hours=1)))
