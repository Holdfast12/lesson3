#!/usr/bin/python3

x = 0
y = 0

dir = input('Выберите направление движения для персонажа (влево/вправо/вверх/вниз): ')
if dir == 'влево':
    x -= 1
elif dir == 'вправо':
    x += 1
elif dir == 'вверх':
    y += 1
elif dir == 'вниз':
    y -= 1
else:
    print('Выбор направления не был сделан')

print('Персонаж находится в точке (%s;%s)' % (x, y))
