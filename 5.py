def possibilities(step, room):
    res = []
    if rooms[step + 1][room - 1] <= rooms[step][room]:
        res.append(-1)
    res.append(0)
    if rooms[step + 1][room + 1] <= rooms[step][room]:
        res.append(1)
    print(rooms[step + 1][room + 1], rooms[step + 1][room - 1])
    return(res)


rooms = [[10, 10, 10, 1, 10, 10, 10], [10, 10, 1, 2, 1, 10, 10], [10, 1, 1, 3, 2, 0, 10]]
# ееее, вырезаем контент, [10, 1, 2, 3, 2, -1, 10]]
room = 3
secret = False
for step in range(2):
    if rooms[step][room] == 0:
        secret = True
        print("Вы нашли комнату, оставленную разробтчиками")
    pos = possibilities(step, room)
    move = -2
    while move == -2:
        print("Выберите направление" + ('"влево"' if -1 in pos else "") + '"вперёд"' + ('" вправо"' if 1 in pos else "") + "?")
        a = input()
        move = -1 if a == "влево" else (0 if a == "вперёд" else (1 if a == "вправо" else -2))
    room += move
nn = " но вы не нашли секрет, попробуйте ещё раз и найдите его"
if secret:
    nn = ". А так же вы нашли секрет на своём пути"
sts = [0, "вы умерли, поздравляем"]
sts.append("в следущей комнате не было дверей, а дверь через которую вы вошли оказалась заперта. Поздравляем!!!")
sts.append("Ваша прямолинейность привела вас к смерти, поздравляем")
sts.append("Кто бы мог подумать, что открывание случайных дверей убьют вас. Но так произошло. Удивительно")
sts.append("Вы сделали что? Вы выжили? Интересно. Надо будеть закрыть эту дверь")
print(sts[room] + nn)
