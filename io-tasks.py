def user_input():
    print("Accept numbers from a user - ")
    num = int(input("Enter your value - "))
    print(num, "\n")


def print_name():
    print(" Display three string “Name”, “Is”, “James” as “Name**Is**James” -")
    print('My', 'Name', 'Is', 'James', sep='**')


def octal(num):
    print("\nConvert Decimal number to octal using print() output formatting - ")
    print('%o' % num)


def decimal(num):
    print("Convert Decimal number to octal using print() output formatting - ")
    print('%.2f' % num)


def list_accept():
    lst = []
    print("\nAccept a list of 5 float numbers as an input from the user - ")
    for i in range(0, 5):
        lst.append(float(input()))

    print(lst)


if __name__ == "__main__":
    #user_input()
    print_name()
    octal(10)
    decimal(518.4567)
    list_accept()
