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

    def add_holiday(self, holiday: date):
        self.holidays.append(holiday)

    def add_vacation_day(self, vacation_day: date):
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
