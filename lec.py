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

# Арифметические опеарции:
# +, -, *, /, %, //, **
# **, унарный плюс, унарный минус, *, /, //, %, -, +
# (), сокращенные операции

a = 123
b = -321
c = a+b
print(a+b)
# // - если мы хотим получить результат деления в целых числах
# % - если мыхотим получить остаток от деления
# ** - возведение в степень
c = round(a*b) # - округление результата до целого числа
c = round(a*b,3) # показывает количество чисел после запятой

a = 3
a = a + 5 # -> a += 5, a *=5  и т.д.
print(a)

# Логические операции:
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 > 4
print(a)

a = 1 > 4 and 5 < 2 # a = 1 == 2, a = 1 != 2
print(a)

f = 1 > 2 or 2 < 3
print(f)

f = [1, 2, 3, 4]
print(f)
print(2 in f)

f = [1, 2, 3, 4]
print(f)
print(not 2 in f)

is_odd = f[0] % 2 == 0
print(is_odd)

is_odd = not f[0] % 2
print(is_odd)