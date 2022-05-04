def reverse_tuple():
    tuple1 = (10, 20, 30, 40, 50)
    tuple1 = tuple1[::-1]

    print("Reverse the tuple - ")
    print(tuple1, '\n')


def access():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

    print("Access value 20 from the tuple - ")
    print(tuple1[1][1])


if __name__ == '__main__':
    reverse_tuple()
    access()
