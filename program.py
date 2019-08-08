from datetime import date
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

    def print_dates(dates: list):
        for i in dates:
            print(i)


if __name__ == '__main__':
    main()