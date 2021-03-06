import string


def fml():
    str1 = "James"
    str2 = str1[0] + str1[int(len(str1) / 2)] + str1[-1]
    print(str2)


def mid():
    str1 = "JhonDipPeta"
    middle = int(len(str1) / 2)
    str2 = str1[middle - 1] + str1[middle] + str1[middle + 1]
    print(str2)


def new_string():
    s1 = "Ault"
    s2 = "Kelly"
    middle = int(len(s1) / 2)
    s3 = s1[:middle] + s2 + s1[middle:]
    print(s3)


def fml1():
    s1 = "America"
    s2 = "Japan"
    mid1 = int(len(s1) / 2)
    mid2 = int(len(s2) / 2)

    s3 = s1[0] + s2[0] + s1[mid1] + s2[mid2] + s1[-1] + s2[-1]

    print(s3)


def lower_first():
    str1 = 'PyNaTive'
    str2 = ''

    for i in str1:
        if i.islower():
            str2 += i
    for i in str1:
        if i.isupper():
            str2 += i
    print(str2)


def count():
    str1 = "P@#yn26at^&i5ve"
    letter = 0
    number = 0
    symbol = 0

    for i in str1:
        if i.isalpha():
            letter += 1
        elif i.isdigit():
            number += 1
        else:
            symbol += 1

    print("Letter - ", letter, "\nNumber - ", number, "\nSymbol - ", symbol)


def mixed():
    s1 = "Abc"
    s2 = "Xyz"
    s3 = ''

    s2 = s2[::-1]

    for i in range(len(s1)):
        s3 += s1[i]
        s3 += s2[i]

    print(s3)


def balance_test():
    s1 = "Yn"
    s2 = "PYnative"

    for j in s1:
        if j not in s2:
            return False

    return True


def occurrence():
    str1 = "Welcome to USA. usa awesome, isn't it?"
    str2 = "usa"

    str1 = str1.lower()
    counter = str1.count(str2)
    print(counter)


def sum_avg():
    str1 = "PYnative29@#8496"
    sum1 = 0
    counter = 0

    for i in str1:
        if i.isdigit():
            i = int(i)
            sum1 += i
            counter += 1

    avg = sum1 / counter

    print("Sum - ", sum1, "\nAverage - ", avg)


def occurrences1():
    str1 = "Apple"
    dict = {}

    for i in str1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    print(dict)


def rev_string():
    str1 = "PYnative"
    str1 = str1[::-1]
    print(str1)


def last():
    str1 = "Emma is a data scientist who knows Python. Emma works at google."

    index = str1.rfind("Emma")

    print("Last occurrence - ", index)


def hyphen():
    str1 = "Emma-is-a-data-scientist"
    lst = str1.split("-")
    for i in lst:
        print(i)


def empty():
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    str_list1 = [i for i in str_list if i is not None and i != ""]
    print(str_list1)


def special():
    str1 = "/*Jon is @developer & musician"
    new_str = str1.translate(str.maketrans('', '', string.punctuation))

    print(new_str)


def digits_only():
    str1 = 'I am 25 years and 10 months old'
    str2 = ''

    for i in str1:
        if i.isdigit():
            str2 += i
    print(str2)


def digits_alpha():
    str1 = "Emma25 is Data scientist50 and AI Expert"
    lst = str1.split()

    for i in lst:
        if not (i.isdigit() or i.isalpha()):
            print(i)

def rep():
    str1 = '/*Jon is @developer & musician!!'

    for i in string.punctuation:
        str1 = str1.replace(i, "#")

    print(str1)

if __name__ == '__main__':
    fml()
    mid()
    new_string()
    fml1()
    lower_first()
    count()
    mixed()
    print(balance_test())
    occurrence()
    sum_avg()
    occurrences1()
    rev_string()
    last()
    hyphen()
    empty()
    special()
    digits_only()
    digits_alpha()
    rep()
