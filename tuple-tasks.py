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


def swap():
    tuple1 = (11, 22)
    tuple2 = (99, 88)

    temp = tuple1
    tuple1 = tuple2
    tuple2 = temp

    print("Swap two tuples in Python - ")
    print("tuple1 = ", tuple1)
    print("tuple2 = ", tuple2, "\n")


def copy():
    tuple1 = (11, 22, 33, 44, 55, 66)

    tuple2 = tuple1[3:5]

    print("Copy specific elements from one tuple to a new tuple - ")
    print(tuple2, "\n")


def modify():
    tuple1 = (11, [22, 33], 44, 55)

    tuple1[1][0] = 222

    print("Modify the tuple - ")
    print(tuple1)


def sort():
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

    for i in tuple1:
        print(tuple[1])


def count():
    tuple1 = (50, 10, 60, 70, 50)
    cnt = 0

    for i in tuple1:
        if i == 50:
            cnt += 1

    print("Counts the number of occurrences of item 50 from a tuple - ")
    print(cnt, "\n")

def all_same():
    tuple1 = (45, 45, 45, 45)

    tag = True

    print("Check if all items in the tuple are the same - ")

    for i in range(len(tuple1)-1):
        if tuple1[i] != tuple1[i+1]:
            tag = False

    print(tag)




if __name__ == '__main__':
    reverse_tuple()
    access()
    create()
    unpack()
    swap()
    copy()
    modify()
    #sort()
    count()
    all_same()

