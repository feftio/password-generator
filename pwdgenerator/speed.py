from pwdgenerator.duration import Duration


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
