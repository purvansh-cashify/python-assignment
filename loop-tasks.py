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

def


if __name__ == "__main__":
    first_ten()
    pattern()
    calculate(10)