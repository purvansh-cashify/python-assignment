def fml():
    str1 = "James"
    str2 = str1[0] + str1[int(len(str1) / 2)] + str1[-1]
    print(str2)

def mid():
    str1 = "JhonDipPeta"
    middle = int(len(str1)/2)
    str2 = str1[middle-1] + str1[middle] + str1[middle+1]
    print(str2)

def new_string():
    s1 = "Ault"
    s2 = "Kelly"
    middle = int(len(s1)/2)
    s3 = s1[:middle] + s2 + s1[middle:]
    print(s3)


if __name__ == '__main__':
    fml()
    mid()
    new_string()

