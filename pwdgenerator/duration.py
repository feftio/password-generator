class Duration:

    def __init__(self, minutes=0, hours=0, days=0, weeks=0):
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.weeks = weeks
        self.dividend = None

    @property
    def inMinutes(self):
        minutes = self.minutes + (60 * self.hours) + \
            (1440 * self.days) + (10080 * self.weeks)
        return minutes if self.dividend is None else self.dividend / minutes

    @property
    def inHours(self):
        hours = (self.minutes / 60) + self.hours + \
            (24 * self.days) + (168 * self.weeks)
        return hours if self.dividend is None else self.dividend / hours

    @property
    def inDays(self):
        days = (self.minutes / 1440) + (self.hours / 24) + \
            self.days + (7 * self.weeks)
        return days if self.dividend is None else self.dividend / days

    @property
    def inWeeks(self):
        weeks = (self.minutes / 10080) + (self.hours / 168) + \
            (self.days / 7) + self.weeks
        return weeks if self.dividend is None else self.dividend / weeks

    def __rtruediv__(self, value: int):
        self.dividend = value
        return self
