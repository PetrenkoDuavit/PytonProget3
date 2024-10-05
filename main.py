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


# # Homeworck 3.1
# a = int(input("Enter First number: ")) #Ввод числел для вычислений
# b = int(input("Enter Second number: "))
#
# user_select = input("Chouse from - + / *. and press enter: ") # выбор действия
#
# match user_select: #
#     case ("-"): #
#         print( a - b)# вычисление и вывод в консоль результата
#     case ("+"):
#         print(a + b)
#     case ("*"):
#         print(a * b)
#     case ("/"):
#         if b == 0:
#             b = int(input("Invalid number, select enother number: ")) # перевірка ділення на 0, з мозжливістю виправитись
#         print( a / b)
#     case _:
#         print("Invalid input please try again")
# Homeworck 3.2



# Homeworck 3.3

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9] # В задании не было указано что нужно сделать инпут, поэтому сделал так..
if len(numbers) % 2:  # Проверка длины массива, четная или нечетная
 lengthOfArr1 =  len(numbers) // 2 + 1 # сдвигаю на 1 для того чтобы правильно записать длину в новый массив
 lengthOfArr2 = len(numbers) // 2 + 1
else:                 # во всех других случаях делю массив на 2
    lengthOfArr1 = len(numbers) // 2
    lengthOfArr2 = len(numbers)// 2
part1 = numbers[:lengthOfArr1] # создаю новые массивы для вывода в консоль
part2 = numbers[lengthOfArr2:]
print(part1)
print(part2)
