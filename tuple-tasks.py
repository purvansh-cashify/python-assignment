def reverse_tuple():
    tuple1 = (10, 20, 30, 40, 50)
    tuple1 = tuple1[::-1]

    print("Reverse the tuple - ")
    print(tuple1, '\n')


def access():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

    print("Access value 20 from the tuple - ")
    print(tuple1[1][1], "\n")


def create():
    tuple1 = tuple([50])

    print("Create a tuple with single item 50 - ")
    print(tuple1, "\n")


def unpack():
    tuple1 = (10, 20, 30, 40)

    a, b, c, d = tuple1

    print("Unpack the tuple into 4 variables - ")
    print(a)
    print(b)
    print(c)
    print(d, "\n")


if __name__ == '__main__':
    reverse_tuple()
    access()
    create()
    unpack()
