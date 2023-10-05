import sys

import dir_file
import victory
import bank
import dir_file as df
import os
import json

account = 0
purchase_history = []
path_account = 'account.txt'
path_purchase_history = 'purchase_history.txt'
path_listdir = 'listdir.txt'
if os.path.exists(path_account):
    with open(path_account, 'r') as f:
        account = int(f.read())
if os.path.exists(path_purchase_history):
    with open(path_purchase_history, 'r') as f:
        purchase_history = json.load(f)

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
                        "12 - запись списка файлов и папок в файл listdir\n"
                        "13 - выход.\n")
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
            account = bank.banking(account, purchase_history)
        case "11":
            os.chdir("C:\project")
            print(f'Текущая рабочая директория - {os.getcwd()}')
        case "13":
            with open(path_account, 'w') as f:
                f.write(str(account))
            with open(path_purchase_history, 'w') as f:
                json.dump(purchase_history, f)
            break
        case "12":
            dir_file.create_listdir(path_listdir)
        case _:
            print("Введено некорректное значение")
