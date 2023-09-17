import os
import shutil

def create_dir():
    name = input("Введите название папки: \n")
    if (os.path.exists(name)):
        print("Такая папка уже создана")
    else:
        os.mkdir(name)

def delete_dirfile():
    name = input("Введите название папки или файла для удаления: \n")
    if (os.path.exists(name)):
        if(os.path.isfile(name)):
            os.remove(name)
        else:
            os.rmdir(name)
    else:
        print("Такой папки или файла не существует")

def copy_dirfile():
    name = input("Введите название папки или файла для копирования: \n")
    new_name = input("Введите новое название папки или файла: \n")
    if (os.path.exists(name)):
        if (os.path.isfile(name)):
            shutil.copyfile(name, new_name)
        else:
            shutil.copytree(name, new_name)
    else:
        print("Такой папки или файла не существует")

def dirfile():
    return os.listdir()
def print_dirfile():
    print(dirfile())

def print_dir():
    new_list = []
    for i in dirfile():
        if os.path.isdir(i):
            new_list.append(i)
    print(new_list)

def print_file():
    new_list = []
    for i in dirfile():
        if os.path.isfile(i):
            new_list.append(i)
    print(new_list)
