from datetime import timedelta, datetime


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


if __name__ == "__main__":
    get_time()
    str_to_dt()
    week_minus()
