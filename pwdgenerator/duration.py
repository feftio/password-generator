from __future__ import annotations
import typing as t


class Duration:
    def __init__(self, minutes: int = 0, hours: int = 0, days: int = 0, weeks: int = 0):
        self.minutes: int = minutes
        self.hours: int = hours
        self.days: int = days
        self.weeks: int = weeks
        self.dividend: t.Optional[int] = None

    @property
    def inMinutes(self) -> int:
        minutes = self.minutes + (60 * self.hours) + \
            (1440 * self.days) + (10080 * self.weeks)
        return minutes if self.dividend is None else self.dividend / minutes

    @property
    def inHours(self) -> int:
        hours = (self.minutes / 60) + self.hours + \
            (24 * self.days) + (168 * self.weeks)
        return hours if self.dividend is None else self.dividend / hours

    @property
    def inDays(self) -> int:
        days = (self.minutes / 1440) + (self.hours / 24) + \
            self.days + (7 * self.weeks)
        return days if self.dividend is None else self.dividend / days

    @property
    def inWeeks(self) -> int:
        weeks = (self.minutes / 10080) + (self.hours / 168) + \
            (self.days / 7) + self.weeks
        return weeks if self.dividend is None else self.dividend / weeks

    def __rtruediv__(self, value: int) -> Duration:
        self.dividend = value
        return self
