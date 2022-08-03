import phone_item


def phone_list(file_directory: str, book: list):
    with open(file_directory, 'r', encoding='utf_8') as file:
        items = file.readlines()
        for i in range(0, len(items)):
            phone_item = tuple(items[i].split('**'))
            book.append(phone_item)


def open_book(book: list):
    if len(book) == 0:
        print('*** Телефонная книга пуста. ***')
    else:
        for i in range(0, len(book)):
            print(f'{i}    Фамилия: {book[i][0]} \n     Имя: {book[i][1]} \n      Комментарий: {book[i][2]} \n      Номер: {book[i][3]}')
            print('')


def add_item(item, book: list):
    book.append(item)


def save_changes(book: list, file_directory: str):
    with open(file_directory, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            surname=book[i][0]
            name = book[i][1]
            comment = book[i][2]
            phone = book[i][3]
            file.writelines(f'{surname}**{name}**{comment}**{phone}')
            file.writelines('\n')
                    


def import_phone_book1(new_file: str, phone_book_file: str, book: list):
    with open(new_file, 'r', encoding='utf_8') as file:
        items = file.readlines()
        for i in range(0, len(items)):
            phone_item = tuple(items[i].split('**'))
            book.append(phone_item)
    #with open(phone_book_file, 'w', encoding='utf-8') as file:
        #for i in range(0, len(book)):
            #surname=book[i][0]
           # name = book[i][1]
           # comment = book[i][2]
           # phone = book[i][3]
           # file.writelines(f'{surname}**{name}**{comment}**{phone}\n')
        


def export_phone_book1(book: list, file_directory: str, form: str, new_direct: str = 'export_file'):
   # with open(file_directory, 'w', encoding='utf-8') as file:
       # for i in range(0, len(book)):
          #  surname=book[i][0]
          #  name = book[i][1]
           # comment = book[i][2]
           # phone = book[i][3]
           # file.writelines(f'{surname}**{name}**{comment}**{phone}')
    new_direct = f'{new_direct}.{form}'
    with open(new_direct, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            surname=book[i][0]
            name = book[i][1]
            comment = book[i][2]
            phone = book[i][3]
            file.writelines(f'{surname}**{name}**{comment}**{phone}')
   
   
def export_phone_book2(book: list, file_directory: str, form: str, new_direct: str = 'export_file'):
  #  with open(file_directory, 'w', encoding='utf-8') as file:
      #  for i in range(0, len(book)):
           # surname=book[i][0]
          #  name = book[i][1]
           # comment = book[i][2]
          #  phone = book[i][3]
          #  file.writelines(f'*{surname}**{name}**{comment}**{phone}*')
    new_direct = f'{new_direct}.{form}'
    with open(new_direct, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            surname=book[i][0]
            name = book[i][1]
            comment = book[i][2]
            phone = book[i][3]
            file.writelines(f'*{surname}* \n *{name}* \n *{comment}* \n *{phone}* \n \n')
            
def import_phone_book2(new_file: str, phone_book_file: str, book: list):
    with open(new_file, 'r', encoding='utf_8') as file:
        items = file.readlines()
        for i in range(0, len(items)):
            phone_item = tuple(items[i].split('*\n*'))
            book.append(phone_item)