ONE_SYMBOL_VOLUME = 4

pages_in_book = 100
string_on_page = 50
symbols_in_string = 25
volume_diskette = 1.44

book = symbols_in_string * pages_in_book * string_on_page * ONE_SYMBOL_VOLUME / 1024**2 # находим объем одной книги
book_in_disskette = int(volume_diskette // book) # находим сколько целых книг поместится на дискету

print("Количество книг, помещающихся на дискету:", book_in_disskette)
