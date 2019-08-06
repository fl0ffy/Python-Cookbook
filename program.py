from datetime import date
from datetime import timedelta


def main():
    start_date = date.today()
    end_date = date(2019, 12, 31)
    pto_hours = 167.73
    holidays = [
        date(2019, 9, 2),
        date(2019, 10, 14),
        date(2019, 11, 11),
        date(2019, 11, 23),
        date(2019, 11, 23),
        date(2019, 12, 24),
        date(2019, 12, 25)
        ]
    vacay_days = [
        date(2019, 8, 22),
        date(2019, 8, 23)
        ]
    exclude_days = holidays + vacay_days
    working_dates = get_weekday_dates(start_date, end_date, exclude_days)
    weekdays = get_weekday_dates(start_date, end_date)
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

#    print('PTO Hours: {}'.format(pto_hours))
#    print('Working Days Remaining: {}'.format(len(working_dates)))
#    print('Weekdays Remaining: {}'.format(len(weekdays)))
#    print('Remaining Potential Hours: {}'.format(remaining_potential_hours))


def get_user_input(start_date: date, End_date: date, start_pto_hours: float):
    pass


def get_weekday_dates(start_date: date, end_date: date, exclude_dates: list = []) -> list:
    list_of_dates = []
    delta = end_date - start_date
    for i in range(delta.days +1):
        d = start_date + timedelta(days=i)
        if d.weekday() < 5 and d not in exclude_dates:
            list_of_dates.append(d)
    return list_of_dates


def get_list_of_working_days(start_date: date, end_date: date) -> list:
    list_of_dates = []
    delta = end_date - start_date
    for i in range(delta.days +1):
        list_of_dates.append(start_date + timedelta(days=i))
    return list_of_dates


def print_dates(dates: list):
    for i in dates:
        print(i)


if __name__ == '__main__':
    main()