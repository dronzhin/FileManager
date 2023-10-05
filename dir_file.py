import os
import shutil
import yaml

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
def create_listdir(path):
    list_dir = []
    list_file = []
    for i in dirfile():
        if os.path.isdir(i):
            list_dir.append(i)
        else:
            list_file.append(i)
    result = {'Directory': list_dir, 'File': list_file}
    with open(path, 'w') as f:
        yaml.dump(result, f, encoding='utf8')

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
