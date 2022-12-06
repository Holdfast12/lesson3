#!/usr/bin/python3

x = 0
y = 0

dir = input('Выберите направление движения для персонажа (влево/вправо/вверх/вниз): ')
steps = int(input(f'Введите нужное целое количество шагов для движения персонажа {dir}: '))
if steps > 0:
    if dir == 'влево':
        x -= 1 * steps
    elif dir == 'вправо':
        x += 1 * steps
    elif dir == 'вверх':
        y += 1 * steps
    elif dir == 'вниз':
        y -= 1 * steps
    else:
        print('Выбор направления не был сделан')
else:
    print('Движение с отрицательным количеством шагов не предусмотрено')

print('Персонаж находится в точке (%s;%s)' % (x, y))
