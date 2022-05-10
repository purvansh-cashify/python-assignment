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


if __name__ == '__main__':
    fml()
    mid()
    new_string()
    fml1()
    lower_first()
    count()
    mixed()
