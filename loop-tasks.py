def first_ten():
    num = 1
    print("Print First 10 natural numbers using while loop - ")
    while num < 11:
        print(num)
        num += 1

    print("\n")


def pattern():
    print("Print the following pattern - ")
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end='')
        print("\n")


def calculate(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i

    print("Calculate the sum of all numbers from 1 to a given number - ")
    print(sum, "\n")


def multiplication(num):
    print("Write a program to print multiplication table of a given number - ")
    for i in range(1, 11):
        print(num * i)
    print("\n")


def list_loop():
    numbers = [12, 75, 150, 180, 145, 525, 50]

    print("Display numbers from a list using loop - ")
    for i in numbers:
        print(i)
    print("\n")


def digits(num):
    num = str(num)
    cnt = len(num)

    print("Count the total number of digits in a number - ")
    print(cnt, "\n")


def pattern2():
    print("Print the following pattern - ")
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end='')
        print("")


def rev_list():
    list1 = [10, 20, 30, 40, 50]

    print("Print list in reverse order using a loop - ")
    for i in reversed(list1):
        print(i)
    print("\n")


def negative():
    print("Display numbers from -10 to -1 using for loop - ")
    for i in range(-10, 0):
        print(i)
    print("\n")


def else_done():
    print("Use else block to display a message “Done” after successful execution of for loop - ")
    for i in range(5):
        print(i)
    else:
        print("Done")


def prime():
    start = 25
    end = 50
    print("Write a program to display all prime numbers within a range - ")
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


def fibonacci():
    num1 = 0
    num2 = 1
    lst = [num1, num2]

    while len(lst) < 10:
        sum1 = num1 + num2
        num1 = num2
        num2 = sum1
        lst.append(sum1)

    print(lst)


if __name__ == "__main__":
    first_ten()
    pattern()
    calculate(10)
    multiplication(2)
    list_loop()
    digits(75869)
    pattern2()
    rev_list()
    negative()
    else_done()
    prime()
    fibonacci()
