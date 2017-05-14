import shelve
from book_file_class import * 
from bookshelf_class import *
from book_class import *

db_file_bookshelf = shelve.open('bookshelf_DB')
db_file_book_file = shelve.open('book_file_DB')
db_file_book = shelve.open('book_DB')
Key_list = []
for key in db_file_book:
        Key_list.append(key)
if Key_list == []:
        start_index = 0
else:
        print('start_index не равен 0')
        start_index = 1
index_db = 'book' + str(start_index)
print(index_db)

object_book = book()

fieldnames_eng = ('name_book','name_author','year','genre')
fieldnames_ru = ('Название книги','ФИО автора','год издания','жанр')

field_number = 0
for field in fieldnames_eng:
        field_ru = fieldnames_ru[field_number]
        if field == 'name_book':
                user_input = input('\t[%s]\nВведите название книги:' % (field_ru))
                setattr(object_book,field,user_input)
                field_number = field_number + 1
        elif field == 'name_author':
                user_input = input('\t[%s]\nВведите ФИО автора через пробел:' % (field_ru))
                setattr(object_book,field,user_input)
                field_number = field_number + 1

        elif field == 'year':
                user_input = input('\t[%s]\nВведите год издания книги:' % (field_ru))
                setattr(object_book,field,user_input)
                field_number = field_number + 1
        elif field == 'genre':
                user_input = input('\t[%s]\nВведите жанр книги:' % (field_ru))
                setattr(object_book,field,user_input)
                field_number = field_number + 1
        else: 
                pass
db_file_book[index_db] = object_book
print(object_book)



db_file_book.close()
db_file_bookshelf.close()
db_file_book_file.close()


