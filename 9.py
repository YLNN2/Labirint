print('Гуляя по лесу вы набрели на старый дом.\
 Вы можете "заглянуть в него", "обойти его" или "пройти мимо".\
 Выберите один из вариантов, данных в кавычках.')
a = input()
if a == "заглянуть в него":
    print('Вы решили заглянуть в это неизвестное строение.\
 Входная дверь оказалась открытой.\
 Перед вами открылась просторная гостинная.')
    print('Вы можете "погулять по дому" или "выйти из дома".\
 Выберите один из вариантов, данных в кавычках.')
    b = input()
    if b == "погулять по дому":
        print('Вы ещё долго гуляли по этому старому домику. На улице наступил вечер.\
 И вы с хорошим настроением отправились домой.')
    elif b == "выйти из дома":
        print('Вы вышли из домика. На улице начинал накрапывать дождь,\
 поэтому вам пришлось поспешить домой.')
elif a == "обойти его":
    print('Обойдя дом, вы увидели вход в подвал. Вы можете "заглянуть" в него\
 или "пройти мимо". Выберите один из вариантов, данных в кавычках.')
    b = input()
    if b == "заглянуть":
        print('Вы зашли в подвал. Включив фонарик и пройдя немного вперёд,\
 вы услышали как дверь за Вами захлопнулась.')
        print('Вы ещё долго пытались её\
 открыть, но сделать это так и не получилось. На следующий день Вас\
 отыскали в бессознательном состоянии и отправили в больницу.')
    elif b == "пройти мимо":
        print('Обойдя дом, вы не нашли ничего интересного, поэтому решили дальше\
 погулять по лесу.')
elif a == "пройти мимо":
    print('Вы прошли мимо дома. Тропинка привела вас к озеру, на берегу которого\
 вы заметили лодку. С виду она была пригодна для использования.')
    print('У вас есть выбор: "прокатиться" на лодке по озеру или "отправиться\
 домой". Выберите один из вариантов, данных в кавычках.')
    b = input()
    if b == 'прокатиться':
        print('Вы сели в лодку, оттолкнулись от берега. Доехали до середины озера.\
 Всё было прекрасно, но вдруг вы заметили течь.')
        print('Лодка медленно тонула, и вскоре полностью ушла под воду.Вы\
 кое-как доплыли до берега и с испорченным настроением отправились домой.')
    elif b == "отправиться домой":
        print('Вы отправились дальше. Ещё немного погуляли по лесу, после вышли\
 на уже знакомую тропинку и отправились домой.')
else:
    print('Вы ещё долго думали, что вам сделать, но не успели принять решения,\
 т.к. неожиданно вы услышали выстрел, и в Вашу голову влетела пуля из охотничьего ружья.')
