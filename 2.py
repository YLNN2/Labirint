print('Ваш персонаж находится в комнате, из которой есть несколько ходов:')
print('направо, налево и прямо')
print('Для того, чтобы выбрать куда идти введите ход, например: направо')
print('Выбор хода:')
a = input()
if a == 'прямо':
    print('Вы попали вдругую комнату')
    print('Вы можете пойти направо или налево')
    print('Выбор хода:')
    b = input()
    if b == 'налево':
        print('Вы прошли лабиринт!')
    elif b == 'направо':
        print('Вы попали в комнату к дракону и умерли :( ')
    else:
        print('ОШИБКА')
elif a == 'налево':
    print('Здесь тупик и много змей, лучше бегите!!!')
elif a == 'направо':
    print('ВЫ попали в темницу, будете гнить до конца дней...')
else:
    print('ОШИБКА')
