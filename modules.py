# PyCharm 2025.2.0.1
# Build #PY-252.23892.515, built on August 12, 2025
# Source revision: a49d407cfb992

import os
import sys
import random
import shutil

# ILLEGAL_NTFS_CHARS = "[<>:/\\|?*\"]|[\0-\31]"
# def removeIllegalChars(name):
#     # removes characters that are invalid for NTFS
#     return re.sub(ILLEGAL_NTFS_CHARS, "", name)

def this_catalog():
    print('Текущий рабочий каталог: ', os.getcwd()) #.venv
    #print('\n')

def create_new_folder():
    # for i in range(5):
    #     #проверка на существование
    #     if not os.path.exists('folder{}'.format(str(i))):
    #         #создать папку
    #         os.mkdir('folder{}'.format(str(i)))
    new_folder = input('Введите имя для новой папки: ')
    if not new_folder:
        print("Имя папки не заполнено, попробуйте ещё раз.")
    elif not os.path.exists(new_folder):
        os.mkdir(new_folder)
        print('Папка ', new_folder, 'успешно создана.')
    else:
        print('Папка ', new_folder, 'уже была создана ранее.')

def look_work_directory():
    # просмотр содержимого рабочей директории
    print('Cодержимое рабочей директории: ', os.listdir(), '\n')

def remove_folder():
    # for i in range(5):
    #     #удалить папку
    #     os.rmdir('folder{}'.format(str(i)))
    #pass
    folder_to_del = input('Введите имя папки/файла, который нужно удалить: ')
    if not os.path.exists(folder_to_del):
        print('Папка или файл: ', folder_to_del, ', не существует. Операция не может быть выполнена.')
    else:
        os.rmdir(folder_to_del)
        print('Папка или файл: ', folder_to_del, ', была успешно удалена.')

def building_path():
    #пример универсальное соеденения путей для win/linux
    path = os.path.join(os.getcwd(), 'other', 'file.txt')
    print(path)

def create_copy_dir():
    ##shutil, при копировании перезаписывает прежнюю копию с аналогичным именем
    #shutil.copy('main.py', 'main_copy.py')
    dir_to_copy = input('Введите имя папки/файла, для которого нужно создать копию: ')
    if not os.path.exists(dir_to_copy):
        print('Папка или файл: ', dir_to_copy, ', не существует. Операция не может быть выполнена.')
    else:
        if os.path.isdir(dir_to_copy):
            copy_name = input('Введите новое имя для копии папки, без использования символов [<>/?*"|]: ')
            shutil.copytree(dir_to_copy, copy_name)
            print('Папка: ', dir_to_copy, ', была успешно скопирована.', copy_name)
        elif os.path.isfile(dir_to_copy):
            copy_name = input('Введите новое имя для копии файла, без использования символов [<>/?*"|]: ')
            shutil.copy(dir_to_copy, copy_name)
            print('Файл: ', dir_to_copy, ', был успешно скопирована.', copy_name)

def version_platform():
    #sys
    print('Версия платформы: ', sys.platform)
    ##где питон ищет файлы - в ядре питона
    #print('Путь: ', sys.path)

def list_of_dir(user_choise):
    if user_choise == 0:
        folders = [item for item in os.listdir('.') if os.path.isdir(item)]
        print("Только папки:", folders)
    elif user_choise == 1:
        files = [item for item in os.listdir('.') if os.path.isfile(item)]
        print("Только файлы:", files)

    #create_new_folder()