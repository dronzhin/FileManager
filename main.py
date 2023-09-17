import DirAndFile as df
import os

print("Добро пожаловать в файловый менеджер")
while True:
    answer = input("\nВыбирите необходимую операцию: \n"
                        "1 - создать папку\n"
                        "2 - удалить (файл/папку)\n"
                        "3 - копировать (файл/папку)\n"
                        "4 - просмотр содержимого рабочей директории\n"
                        "5 - посмотреть только папки\n"
                        "6 - посмотреть только файлы\n"
                        "7 - просмотр информации об операционной системе\n"
                        "8 - создатель программы\n"
                        "9 - играть в викторину\n"
                        "10 - мой банковский счет\n"
                        "11 - смена рабочей директории (*необязательный пункт)\n"
                        "12 - выход.\n")
    match answer:
        case "1":
            df.CreateDir()
        case "2":
            df.DeleteDirFile()
        case "3":
            df.CopyDirFile()
        case "4":
            df.PrintDirFile()
        case "5":
            df.PrintDir()
        case "6":
            df.PrintFile()
        case "7":
            os.uname()
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            break
        case _:
            print("Введено некорректное значение")
