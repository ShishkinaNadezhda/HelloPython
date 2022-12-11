print('hello world')

# типы данных и переменные:
# int, str, boolean, float, list, none

value = None
print(value)
a = 123
b = 1.23
print(a)
print(b)
#print(type(b))

value = 12334
print(value)

s = 'hello world'
# print(s) # вывод строки

print(a, '-', b, '-',  s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

F = True
print(F)

list = ['1', '2', '3', 'hello']
print(list)

# ввод и вывод данных

print('Введите a');
a = int(input())
print('Введите b');
b = int(input())
print(a, '+', b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')