import sys
import victory
import bank
import dir_file as df
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
            df.create_dir()
        case "2":
            df.delete_dirfile()
        case "3":
            df.copy_dirfile()
        case "4":
            df.print_dirfile()
        case "5":
            df.print_dir()
        case "6":
            df.print_file()
        case "7":
            print(sys.platform)
        case "8":
            print("Создатель программы Ронжин Д.А.")
        case "9":
            victory.start_victory()
        case "10":
            bank.banking()
        case "11":
            os.chdir("C:\project")
            print(f'Текущая рабочая директория - {os.getcwd()}')
        case "12":
            break
        case _:
            print("Введено некорректное значение")
