#!/usr/bin/python3
from decimal import Decimal
from math import sqrt

#получение коэффициентов от пользователя
a, b, c = map(Decimal, (input('Введите коэффициенты a, b, c через пробел: ').split()))

dict = {'X**2'}


print(uravnenie)

#дискриминант
d = b**2-4*a*c


print(f'Для заданных коэффициентов уравнение будет выглядетьДискриминант в этом уравнении будет {d}')



if d > 0:
    print(f'Найдено два корня уравнения - x1 = {(-b+sqrt(d))/(2*a)}, x2 = {(-b-sqrt(d)/(2*a))}')
elif d == 0:
    print(f'Наден корень уравнения x = {-b/(2*a)}')
else:
    print('Уравнение не имеет корней')
