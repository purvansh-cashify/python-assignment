def user_input():
    print("Accept numbers from a user - ")
    # num = int(input("Enter your value - "))
    # print(num, "\n")


def print_name():
    print(" Display three string “Name”, “Is”, “James” as “Name**Is**James” -")
    print('My', 'Name', 'Is', 'James', sep='**')


def octal(num):
    print("\nConvert Decimal number to octal using print() output formatting - ")
    print('%o' % num)


def decimal(num):
    print("Convert Decimal number to octal using print() output formatting - ")
    print('%.2f' % num)


if __name__ == "__main__":
    user_input()
    print_name()
    octal(10)
    decimal(518.4567)
