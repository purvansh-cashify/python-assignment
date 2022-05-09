import os


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


def three_input():
    print("\nAccept any three string from one input() call - ")
    str1, str2, str3 = input("Enter three string").split()
    print('Name1:', str1)
    print('Name2:', str2)
    print('Name3:', str3)


def format1():
    quantity = 3
    totalMoney = 1000
    price = 450
    print("\nFormat variables using a string.format() method - ")
    statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
    print(statement1.format(quantity, totalMoney, price))


def file_size():
    print("\nCheck file is empty or not - ")
    size = os.stat("hello.txt").st_size
    if size == 0:
        print('file is empty')


if __name__ == "__main__":
    # user_input()
    print_name()
    octal(10)
    decimal(518.4567)
    # list_accept()
    # three_input()
    format1()
    file_size()

