print('Внимание! Запись повториться 1 раз. Слушайте внимательно!')
print('Если вы читаете это, то вы смогли выбраться из лап злодея')
print('и спешите выбраться отсюда. Особо не радуетесь. Злодей предусмотрел это')
print('. Есть три двери: левая, центральная, правая.')
print('Я сейчас пойду в левую дверь, если у этой записи не будет продолжения,')
print('то знаете, я погиб, выбрав левую дверь, не идите туда')
print('')
print('Ух, ну и обстановочка!')
print('Как думаете:стоит ли довериться таинственному первопроходцу из записки?')
print('Дайте ответ "да" или "нет"')
answer1 = input()
if answer1 == 'да':
    print('Хорошо, тогда выбираем из центральной или правой двери.')
    print('Выберете дверь с помомщью слов "центральная" или "правая"')
    answer1_1 = input()
    if answer1_1 == 'центральная':
        print('В комнате была лава, вы сгорели. Попробуйте ещё раз!')
    elif answer1_1 == 'правая':
        print('За дверью есть 2 пути: люк наверх и веревочная лестница,')
        print('ведущая вниз. Выберете продолжение словом "люк" или "лестица".')
        answer1_2 = input()
        if answer1_2 == 'люк':
            print('Наверху вас ждал человек с дубинкой и ножницами в кармане.')
            print('Неудачная попытка. Попробуйте ещё раз!')
        elif answer1_2 == 'лестница':
            print('Сверху из люка к вам спустился человек с ножницами и...')
            print('разрезал лестницу. Неудача. Попробуйте ещё раз!')
if answer1 == 'нет':
    print('Действиельно. Нет оснований ему доверять. это может быть сам злодей')
    print('что хочет нас запутать')
    print('Выбирайте дверь с помощью слов "левая", "центральная", "правая".')
    answer2 = input()
    if answer2 == 'центральная':
        print('В комнате была лава, вы сгорели. Попробуйте ещё раз!')
    elif answer2 == 'правая':
        print('За дверью есть 2 пути: люк наверх и веревочная лестница,')
        print('ведущая вниз. Выберете продолжение словом "люк" или "лестица".')
        answer1_2 = input()
        if answer1_2 == 'люк':
            print('Наверху вас ждал человек с дубинкой и ножницами в кармане.')
            print('Неудачная попытка. Попробуйте ещё раз!')
        elif answer1_2 == 'лестница':
            print('Сверху из люка к вам спустился человек с ножницами и...')
            print('разрезал лестницу. Неудача. Попробуйте ещё раз!')
        else:
            print('Попробуй заново. Внимательно читай условие')
    elif answer2 == 'левая':
        print('За этой дверью лежит грозный лев, который не ел год')
        print('Что будем делать?')
        print('1ый вариант: на цыпочках пройти мимо него')
        print('2ой вариант: просто побежать')
        print('Выберете варианты с помощью слов "первый" или "второй."')
        answer2_1 = input()
        if answer2_1 == 'первый':
            print('Вы подсколзнулись на ровном месте и расшибли себе голову.')
            print('Вы явно такого не ожидали. Попробуйте ещё раз.')
        elif answer2_1 == 'второй':
            print('Согласен. Нет смысла идти осторожно, когда лев давно умер')
            print('от голода. Вы быстро выбрались на улицу, преодолев')
            print('опасности. Вы справились со всеми испытниями.')
            print('Мои поздравления!')
        else:
            print('Попробуй заново. Внимательно читай условие')
    else:
        print('Попробуй заново. Внимательно читай условие')
else:
    print('Попробуй заново. Внимательно читай условие')
