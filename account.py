from datetime import date
from datetime import timedelta


class Account:
    start_date = None
    end_date = None
    leave_hours = None
    holidays = []
    vacation_days = []

    def set_start_date(self, start_date: date):
        self.start_date = start_date

    def set_end_date(self, end_date: date):
        self.end_date = end_date

    def set_leave_hours(self, leave_hours: float):
        self.leave_hours = leave_hours

    def add_holiday(self, holiday: date or list):
        self.holidays.append(holiday)

    def add_vacation_day(self, vacation_day: date or list):
        self.vacation_days.append(vacation_day)

    def get_leave_hours(self):
        return self.leave_hours

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_holidays(self):
        return self.holidays

    def get_vacation_days(self):
        return self.vacation_days

    def get_weekday_dates(self) -> list:
        list_of_dates = []
        exclude_dates = self.holidays + self.vacation_days
        delta = self.end_date - self.start_date

        for i in range(delta.days + 1):
            d = self.start_date + timedelta(days=i)
            if d.weekday() < 5 and d not in exclude_dates:
                list_of_dates.append(d)

        return list_of_dates

    def get_list_of_working_days(self) -> list:
        list_of_dates = []
        delta = self.end_date - self.start_date
        for i in range(delta.days + 1):
            list_of_dates.append(self.start_date + timedelta(days=i))
        return list_of_dates

