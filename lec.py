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

# if, if-else
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# elif
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

# while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# while else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
# Пожалуй
# хватит )
# 32

# for
for i in 1, -2, 3, 14, 5:
    print(i)
# 1
# -2
# 3
# 14
# 5

for i in 1, 2, 3, 4, 5:
    print(i**2)

list = [1, 2, 3, 4, 5]
for i in list:
    print(i**2)

r = range(10)
for i in r:
    print(r)

for i in range(10):
    print(r)

for i in range(1, 4):
    print(r)

for i in range(1, 10, 2):
    print(r)

for i in range('qwerty'):
    print(r)

for i in range('qwe - rty'):
    print(r)

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)


text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]


# Списки: введение
colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый
# многократно

def f(x):
    return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType

arg = 2.3
print(f(arg))
print(type(f(arg)))