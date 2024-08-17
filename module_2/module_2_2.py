first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print ('Количество равных чисел: ', 3)
elif first == second or first == third or second == third:
    print ('Количество равных сичел: ', 2)
else:
    print (0, 'Равных чисел нет')
