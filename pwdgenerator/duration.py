from __future__ import annotations
import typing as t


class Duration:
    def __init__(self, minutes: int = 0, hours: int = 0, days: int = 0, weeks: int = 0):
        self.minutes: int = minutes
        self.hours: int = hours
        self.days: int = days
        self.weeks: int = weeks
        self.dividend: t.Optional[t.Union[int, float]] = None

    @property
    def inMinutes(self) -> t.Union[int, float]:
        minutes = self.minutes + (60 * self.hours) + \
            (1440 * self.days) + (10080 * self.weeks)
        return minutes if self.dividend is None else self.dividend / minutes

    @property
    def inHours(self) -> t.Union[int, float]:
        hours = (self.minutes / 60) + self.hours + \
            (24 * self.days) + (168 * self.weeks)
        return hours if self.dividend is None else self.dividend / hours

    @property
    def inDays(self) -> t.Union[int, float]:
        days = (self.minutes / 1440) + (self.hours / 24) + \
            self.days + (7 * self.weeks)
        return days if self.dividend is None else self.dividend / days

    @property
    def inWeeks(self) -> t.Union[int, float]:
        weeks = (self.minutes / 10080) + (self.hours / 168) + \
            (self.days / 7) + self.weeks
        return weeks if self.dividend is None else self.dividend / weeks

    def __rtruediv__(self, dividend: int) -> Duration:
        self.dividend = dividend
        return self

    def __mul__(self, duration: Duration) -> Duration:
        return self.inMinutes * duration.inMinutes
