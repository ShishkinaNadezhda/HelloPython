# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# первый вариант
# num1 = int(input('Введите первое число: '))
#num2 = int(input('Введите второе число: '))
#num3 = int(input('Введите третье число: '))
#num4 = int(input('Введите четвертое число: '))
#num5 = int(input('Введите пятое число: '))

#if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#    print (f'{num1} - максимальное число')
#elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#    print (f'{num2} - максимальное число')
#elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
#    print (f'{num3} - максимальное число')
#elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
#    print (f'{num4} - максимальное число')
#elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
#    print (f'{num5} - максимальное число')

# второй вариант:
#numbers = []
#for i in range(1,6):
#    numbers.append(int(input(f'Введите элемент под номером {i}: ')))
#    #numbers.append - метод добавления списка
#print(numbers)
#print(max(numbers))
#my_max = num1
#if my_max < num2:
#    my_max = num2
#if my_max<num3:
#    my_max = num3
#if my_max<num4:
#    my_max = num4
#if my_max<num5:
#    my_max = num5
#print(my_max)

# третий вариант:
my_max = 0
for i in range(5):
    num = int(input('Введите число: '))
    if my_max < num:
        my_max = num
print(my_max)
