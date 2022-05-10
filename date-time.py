from datetime import timedelta, datetime
import time


def get_time():
    print(datetime.now())


def str_to_dt():
    date_string = "Feb 25 2020 4:20PM"
    datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(datetime_object)


def week_minus():
    given_date = datetime(2020, 2, 25)
    new_date = given_date - timedelta(days=7)
    print(new_date)


def date_format():
    given_date = datetime(2020, 2, 25)
    print(given_date.strftime("%A %d %B %Y"))


def day_of_week():
    given_date = datetime(2020, 7, 26)
    print(given_date.strftime("%A"))


def add_week():
    given_date = datetime(2020, 3, 22, 10, 0, 0)
    new_date = given_date + timedelta(days=7, hours=12)
    print(new_date)


def milli():
    milliseconds = int(time.time() * 1000)
    print(milliseconds)


if __name__ == "__main__":
    get_time()
    str_to_dt()
    week_minus()
    date_format()
    day_of_week()
    add_week()
    milli()
