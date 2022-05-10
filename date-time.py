import datetime


def get_time():
    print(datetime.datetime.now())

def str_to_dt():
    date_string = "Feb 25 2020 4:20PM"
    datetime_object = datetime.datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(datetime_object)


if __name__ == "__main__":
    get_time()
    str_to_dt()

