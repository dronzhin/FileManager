def start_victory():
    count_true = 0

    answer1 = input("Введите год рождения Пушкина: ") # 6 июня 1799 г.
    if answer1 == "1799":
        print("Верно")
        count_true += 1
    else:
        print("Не верно")

    answer2 = input("Введите год рождения Сталина: ") # 18 декабря 1878 г.
    if answer2 == "1878":
        print("Верно")
        count_true += 1
    else:
        print("Не верно")

    answer3 = input("Введите год рождения Петра 1: ") # 9 июня 1672 г.
    if answer3 == "1672":
        print("Верно")
        count_true += 1
    else:
        print("Не верно")

    answer4 = input("Введите год рождения Ленина: ") # 22 апреля 1870 г..
    if answer4 == "1870":
        print("Верно")
        count_true += 1
    else:
        print("Не верно")

    answer5 = input("Введите год рождения Петина: ") # 7 октября 1952 г.
    if answer5 == "1952":
        print("Верно")
        count_true += 1
    else:
        print("Не верно")

    print("Количество правильных ответов -", count_true)
    print("Количество ошибок -", 5 - count_true)
    print("Процент правильных ответов  -", count_true/5*100)
    print("Процент неправильных ответов  -", 100 - count_true/5*100)