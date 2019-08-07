from datetime import date
from datetime import timedelta
from account import Account


def main():
    account1 = Account()

    account1.set_start_date(date.today())
    account1.set_end_date(date(2019, 12, 31))
    account1.add_holiday([
        date(2019, 9, 2),
        date(2019, 10, 14),
        date(2019, 11, 11),
        date(2019, 11, 23),
        date(2019, 11, 23),
        date(2019, 12, 24),
        date(2019, 12, 25)
        ])
    account1.add_vacation_day([
        date(2019, 8, 22),
        date(2019, 8, 23)
        ])
    account1.set_leave_hours(167.73)

    remaining_potential_hours = len(weekdays) * 8

    for day in working_dates:
        if day.weekday() == 4:
            pto_hours += 4
            remaining_potential_hours -= 8
        else:
            pto_hours += 1
            remaining_potential_hours -= 8
        if remaining_potential_hours - pto_hours < 0:
            print('No more work after: {}'.format(day))
            break

    def print_dates(dates: list):
        for i in dates:
            print(i)


if __name__ == '__main__':
    main()