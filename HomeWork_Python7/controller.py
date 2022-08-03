import sys

import logger
import phone_item
import operations
from collections import namedtuple

phone_book = []


def create_menu():
    print('----------------------------------------------------- \n'
          '|    1. Открыть телефонную книгу                     | \n'
          '|    2. Добавить запись                              | \n'
          '|    3. Импорт контактов в файл без пустых строк     | \n'
          '|    4. Экспорт контактов из файла без пустых строк  | \n'
          '|    5. Импорт контактов в файл c пустыми строками   | \n'
          '|    6. Экспорт контактов из файла c пустыми строками| \n'
          '|    7. Завершить работу                             | \n'
          '-----------------------------------------------------')

def end_prog():
    cont = input('\nПродолжить работу с телефонной книгой (да/нет): ')
    if cont == 'да':
        print('Продолжаем работу  -> \n')
        return
    else:
        operations.save_changes(phone_book, 'phone_book.txt')
        print('Закрытие телефонной книги...')
        sys.exit()


def program():
    operations.phone_list("phone_book.txt", phone_book)
    while True:
        create_menu()
        command = int(input('Введите номер команды: '))

        if command == 1:
            operations.open_book(phone_book)
            end_prog()

        elif command == 2:
            contact_surname = input('Фамилия контакта: ')
            contact_name = input('Имя контакта: ')
            contact_comment = input('Комментарий к контакту: ')
            contact_phone = input('Номер телефона: ')
            operations.add_item(phone_item.phone_item(contact_surname, contact_name, contact_comment, contact_phone), phone_book)
            logger.log(len(phone_book) - 1, 'adding', phone_book)
            operations.save_changes(phone_book, 'phone_book.txt')

        elif command == 3:
            new_file = input('Введите директорию файла для импорта: ')
            operations.import_phone_book1(new_file, 'phone_book.txt', phone_book)
            logger.log_import_export('import', new_file)
            print('Файл успешно импортирован. \n')

        elif command == 4:
            format = input('Введите формат экспорта: ')
            file = 'phone_book.txt'
            operations.export_phone_book1(phone_book, 'phone_book.txt', format)
            logger.log_import_export('export', file)
            print('Файл успешно экспортирован. \n')
        elif command == 5:
            new_file = input('Введите директорию файла для импорта: ')
            operations.import_phone_book2(new_file, 'phone_book.txt', phone_book)
            logger.log_import_export('import', new_file)
            print('Файл успешно импортирован. \n')

        elif command == 6:
            format = input('Введите формат экспорта: ')
            file = 'phone_book.txt'
            operations.export_phone_book2(phone_book, 'phone_book2.txt', format)
            logger.log_import_export('export', file)
            print('Файл успешно экспортирован. \n')

        elif command == 7:
            operations.save_changes(phone_book, 'phone_book.txt')
            break