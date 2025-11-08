from modules import create_new_folder, remove_folder, create_copy_dir, look_work_directory, version_platform, list_of_dir
from my_bank import inicilization_program as my_bank_init
from game_viktorina import inicilization_program as game_viktorina_init

def inicilization_program():

    while True:
        print('1. Создать папку')
        print('2. Удалить папку / файл')
        print('3. Копировать папку / файл')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Посмотреть только папки')
        print('6. Посмотреть только файлы')
        print('7. Просмотр информации об операционной системе')
        print('8. О программе')
        print('9. Играть в викторину')
        print('10. Мой банковский счет')
        print('11. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            create_new_folder()
        elif choice == '2':
            remove_folder()
        elif choice == '3':
            create_copy_folder()
        elif choice == '4':
            look_work_directory()
        elif choice == '5':
            list_of_dir(0)
        elif choice == '6':
            list_of_dir(1)
        elif choice == '7':
            version_platform()
        elif choice == '8':
            print('Автор программы: кандидат в мастера спорта по лени :)')
        elif choice == '9':
            game_viktorina_init()
        elif choice == '10':
            my_bank_init()
        elif choice == '11':
            break
        else:
            print('Неверный пункт меню')

inicilization_program()