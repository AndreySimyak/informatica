ONE_SYMBOL_VOLUME = 4
VOLUME_DISKETTE = 1.44

pages_in_book = 100
string_on_page = 50
symbols_in_string = 25


book = symbols_in_string * pages_in_book * string_on_page * ONE_SYMBOL_VOLUME / 1024**2 # Находим объем одной книги.
book_in_disskette = int(VOLUME_DISKETTE // book) # Находим сколько целых книг поместится на дискету.

print("Количество книг, помещающихся на дискету:", book_in_disskette)
