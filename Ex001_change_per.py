a = 23
b = 45
c = a
a = b
b = c
print(a)
print(b)

# второй вариант:
a = 23
b = 45
a,b = b,a
print(a)
print(b)