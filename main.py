# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Homeworck 3.1
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))

user_select = input("Chouse from - + / *. and press enter: ")

match user_select:
    case ("-"):
        print( a - b)
    case ("+"):
        print(a + b)
    case ("*"):
        print(a * b)
    case ("/"):
        if b == 0:
            b = int(input("Invalid number, select enother number: "))
        print( a / b)
    case _:
        print("Invalid input please try again")


