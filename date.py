class Date:
    _single_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                    9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        """
        Constructor
        :param day: int, month: int, year: int
        """
        self._day = day
        self._month = month
        self._year = year

    def __lt__(self, other):
        """Override < sign"""
        if self._year < other.year:
            return True
        elif self._year == other.year and self._month < other.month:
            return True
        elif self._year == other.year and self._month == other.month and \
                self._day < other.day:
            return True
        else:
            return False

    def __gt__(self, other):
        """Override > sign"""
        if self._year > other.year:
            return True
        elif self._year == other.year and self._month > other.month:
            return True
        elif self._year == other.year and self._month == other.month and \
                self._day > other.day:
            return True
        else:
            return False

    def __eq__(self, other):
        """Override == sign"""
        if self._day == other.day and self._month == other.month and \
                self._year == other.year:
            return True
        else:
            return False

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if 0 < value <= self._single_year[self._month]:
            self._day = value
        else:
            raise ValueError("Invalid day value")

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if 1 <= value <= 12:
            self._month = value
        else:
            raise ValueError("Invalid month value")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value > 0:
            self._year = value
        else:
            raise ValueError("Invalid year value")

    def set_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def date_to_str(self):
        """Convert date to string representation"""
        return str(self._day) + ":" + str(self._month) + ":" + str(self._year)

    def is_leap_year(self):
        """Check if year is leap"""
        if (self._year % 400 == 0) or (self._year % 100 != 0) and \
                (self._year % 4 == 0):
            return True
        else:
            return False

    def calc_difference(self, other):
        """
        Calculate difference between two dates in days
        From smaller date (self) to greater (other)
        :param other: Date
        :return days: int
        """
        days = 0

        for year in range(self._year+1, other.year):
            days += 365
            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                days += 1

        if self.year == other.year:
            for month in range(self.month+1, other.month):
                days += self._single_year[month]
                if month == 2 and self.is_leap_year():
                    days += 1
        else:
            for month in range(self.month + 1, 13):
                days += self._single_year[month]
                if month == 2 and self.is_leap_year():
                    days += 1

            for month in range(1, other.month):
                days += self._single_year[month]
                if month == 2 and other.is_leap_year():
                    days += 1

        if self.month == other.month and self.year == other.year:
            days += other.day - self.day
        else:
            days += self._single_year[self._month] - self._day
            days += other.day

        return days


if __name__ == '__main__':
    date1 = Date(1, 1, 2000)
    date2 = Date(1, 1, 2019)
    print(date1.date_to_str())
    print(date2.date_to_str())
    print(date1.calc_difference(date2))
