print("Вы пришли в заброшенный город."'Куда вы пойдёте: налево, направо или прямо?')
a = input()
if "налево" in a:
    print("Вы нашли заброшенную больницу.Возможно там вы найдёте медикаменты.Куда вы выберите пойти: налево, направо или прямо?")
    b = input()
    if "направо" in b:
        print("Увы, вы нашли пустую комнату, идите обратно.")
    elif "налево" in b:
        print("Вы нашли аптечку! Но она пустая, придётся обратно идти")
    elif "прямо" in b:
        print('Вы нашли бинты и выход на улицу. Вы выходите и слева видете люк от бункера, возможно там есть выжившие.')
        print('Справа вы видете полицейский участок, возможно вы найдёте оружие.')
        print('А прямо перед вами закрытый участок, может кто-то там живёт.')
        print('Куда же вы пойдёте: налево, направо или же прямо?')
        c = input()
        if "налево" in c:
            print("Вы подошли к бункеру и увидели что люк открытый. Вы спускаетесь и на вас налетает зомби.")
            print("Вы сумели отбится, но обернувшись, увидели целую орду.")
            print("Прощайте, в следующий раз повезёт!")
        elif "направо" in c:
            print("Вы заходите в полицейский участок, ищите инвертарь участка.")
            print("Вдруг вы слышите странные звуки, обернувшись вы видете что на вас бежит зомби.")
            print("Убегая по корридорам вы прибегаете в тупик, вам страшно, вдруг вы видете у трупа в руках пистолет.")
            print("Наведясь на зомби вы нажимаете на курок, мгновение! Но, вам не повезло, в нём не осталось патронов.")
            print("В следующий раз повезёт!")
        elif "прямо" in c:
            print("Вы перелезаете через забор, вдруг слышите выстрел, и моментально падаете на землю, истекая кровью.")
            print("Увы но кому сейчас не нужны новые друзья. \n Вследующий раз повезёт!")
elif "направо" in a:
    print("Вы идёте и видете выживших! Вам повезло, они оказались добрыми, вы пока что в безопасности. \n До встречи!")
elif "прямо" in a:
    print("Вы идёте, и вдруг падаете в яму. Открыв глаза, вы понимаете что сломали ногу. Увы, но теперь это смерть в муках!")
    print("Попробуйте другой вариант!")
else:
    print("Такое направление я не предусмотрел!")