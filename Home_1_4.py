# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))
if (number == 1):
    print(F'{number} -> x > 0; y > 0')
elif (number == 2):
    print(F'{number} -> x < 0; y > 0')
elif (number == 3):
    print(F'{number} -> x < 0; y < 0')
elif (number == 4):
    print(F'{number} -> x > 0; y < 0')
else:
    print('Некорректный ввод, повторите попытку!')
