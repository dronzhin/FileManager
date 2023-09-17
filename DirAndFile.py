import os
import shutil

def CreateDir():
    name = input("Введите название папки: \n")
    if (os.path.exists(name)):
        print("Такая папка уже создана")
    else:
        os.mkdir(name)

def DeleteDirFile():
    name = input("Введите название папки или файла для удаления: \n")
    if (os.path.exists(name)):
        if(os.path.isfile(name)):
            os.remove(name)
        else:
            os.rmdir(name)
    else:
        print("Такой папки или файла не существует")

def CopyDirFile():
    name = input("Введите название папки или файла для копирования: \n")
    new_name = input("Введите новое название папки или файла: \n")
    if (os.path.exists(name)):
        if (os.path.isfile(name)):
            shutil.copyfile(name, new_name)
        else:
            shutil.copytree(name, new_name)
    else:
        print("Такой папки или файла не существует")

def DirAndFile():
    return os.listdir()
def PrintDirFile():
    print(DirAndFile())

def PrintDir():
    new_list = []
    for i in DirAndFile():
        if os.path.isdir(i):
            new_list.append(i)
    print(new_list)

def PrintFile():
    new_list = []
    for i in DirAndFile():
        if os.path.isfile(i):
            new_list.append(i)
    print(new_list)