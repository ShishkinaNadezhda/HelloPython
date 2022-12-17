# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8, 9 -> нет

# первый вариант:

#num1, num2 = int(input()), int(input())
#if num1 ** 2 == num2 or num2 ** 2 == num1:
#    print('да')
#else:
#    print("нет")

# второй вариант

# print('Введите a')
# a=int(input())
# print('Введите b')
# b= int(input())
# if a**2==b or b**2==a:
#     print('yes')
# else:
#     print('no')


# третий вариант:
# test1, test2 = int(input()), int(input())
# if test1 ** 2 == test2 or test2 == test1 ** 2: 
#    print("all done")
# else: 
# print("none")

# четвертый вариант:
first_user_number = int(input('Enter first number: '))
second_user_number = int(input('Enter second number: '))
print (f'{first_user_number}, {second_user_number} ->', end=' ')

if first_user_number == second_user_number ** 2 or second_user_number == first_user_number ** 2:
    print ('yes')
else:
    print ('no')