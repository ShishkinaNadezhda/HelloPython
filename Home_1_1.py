# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
#    - 6 -> да
#    - 7 -> да
#    - 1 -> нет

day = int(input('Введите порядковый номер дня недели: '))
if (day == 1):
    print('Понедельник, рабочий день')
elif (day == 2):
    print('Вторник, рабочий день')
elif (day == 3):
    print('Среда, рабочий день')
elif (day == 4):
    print('Четверг, рабочий день')
elif (day == 5):
    print('Пятница, рабочий день')
elif (day == 6):
    print('Суббота, выходной')
elif (day == 7):
    print('Воскресенье, выходной')
else:
    print('Некорректный ввод, повторите попытку!')

# второй вариант:
day = int(input('Введите порядковый номер дня недели: '))
if (1 <= day 5 <= 1):
    print('рабочий день')
elif (6 <= day <= 7):
    print('выходной')
else:
    print('Некорректный ввод, повторите попытку!')