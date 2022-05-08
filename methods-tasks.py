def func():
    print("Create a function with default argument - ")
    print("This is a function. \n")


def variable(*args):
    lst = [i for i in args]
    print("Create a function with variable length of arguments - ")

    return sum(lst)


def calculation(a, b):
    sm = a + b
    diff = a - b
    print("Return multiple values from a function - ")

    return sm, diff


def employee(name, salary=9000):
    print("Create a function with default argument - ")
    print("Name - ", name, " Salary - ", salary, "\n")


def outer(a, b):
    def inner(c, d):
        sm = c + d
        return sm

    sum1 = inner(a, b) + 5
    print("Create an inner function to calculate the addition in the following way - ")
    return sum1


def recursive(num):
    if num > 0:
        return num + recursive(num - 1)
    else:
        return 0


def display_student(name, age):
    print("Assign a different name to function and call it through the new name -")
    print(name, age, "\n")


def print_even():
    print("Generate a Python list of all the even numbers between 4 to 30 - ")
    for i in range(4, 31):
        if i % 2 == 0:
            print(i, end=" ")
    print("\n")


def largest(lst):
    num = max(lst)
    print("Find the largest item from a given list - ")
    return num


if __name__ == "__main__":
    func()
    print("Sum - ", variable(20, 40))
    print(calculation(50, 30), "\n")
    employee("Ben", 12000)
    employee("Jessa")
    print(outer(3, 4), "\n")
    print("Create a recursive function - \n", (recursive(10)), "\n")
    show_student = display_student
    show_student("Emma", 26)
    print_even()
    print(largest([4, 6, 8, 24, 12, 2]))
