print('Твоя задача - спасти принцессу из заточения.')
print('Ты стоишь перед замком и можешь "войти через парадный вход", "войти через чёрный вход" или "вернуться домой".')
print('Введи одно из слов в кавычках для выбора.')
a = input()
if a == 'войти через парадный вход':
    print('О, нет! Ты встретился с разъярёнными львами!')
elif a == 'вернуться домой':
    print('Ты просто трус!')
elif a == 'войти через чёрный вход' or 'войти через черный вход':
    print('Внутри замка ты увидел старую крутую лестницу и поднялся по ней.')
    print('Перед тобой две двери: на одной написано "Дракоша", а на другой "Принцесса".')
    print('Какую ты выберешь?')
    b = input()
    if b == 'Дракоша':
        print('Дракоша явно не в настроении и не отдаст тебе принцессу.')
    elif b == 'Принцесса':
        print('Получилось! Перед тобой стоит принцесса, которая очень долго ждала спасения.')
        print('Ты очень умный и отважный! Настоящий герой!')