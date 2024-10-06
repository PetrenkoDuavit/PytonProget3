


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

numbersList = [12, 5, 5, 7, 4, 9]
lengOflist = len(numbersList) # помещаю длину списка в переменную lengOflist для проверок If else
if 0 == lengOflist:  # если список пустой сразу вывожу в консоль
    print(numbersList)
else:
    lastNumerOfList = numbersList.pop() # удаляю последний элемент списка и помещаю в переменную
    numbersList.insert(0, lastNumerOfList) # записываю удаленный элемент в начало списка
    print(numbersList)

# Homeworck 3.3

# numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9] # В задании не было указано что нужно сделать инпут, поэтому сделал так..
# if len(numbers) % 2:  # Проверка длины массива, четная или нечетная
#  lengthOfArr1 =  len(numbers) // 2 + 1 # сдвигаю на 1 для того чтобы правильно записать длину в новый массив
#  lengthOfArr2 = len(numbers) // 2 + 1
# else:                 # во всех других случаях делю массив на 2
#     lengthOfArr1 = len(numbers) // 2
#     lengthOfArr2 = len(numbers)// 2
# part1 = numbers[:lengthOfArr1] # создаю новые массивы для вывода в консоль
# part2 = numbers[lengthOfArr2:]
# print(part1)
# print(part2)
