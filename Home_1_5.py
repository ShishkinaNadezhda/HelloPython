# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa = int(input('Введите координату x точки А: '))
ya = int(input('Введите координату y точки А: '))
xb = int(input('Введите координату x точки B: '))
yb = int(input('Введите координату y точки B: '))

#distanceX = (xb - xa)*(xb - xa)
#distanceY = (ya - yb)*(ya - yb)
import cmath
i = round((cmath.sqrt((xb - xa)*(xb - xa) + (ya - yb)*(ya - yb))),2)
#i = (cmath.sqrt((xb - xa)*(xb - xa) + (ya - yb)*(ya - yb)))
print(f'A ({xa}, {ya}); B ({xb, yb}) -> {i}')
