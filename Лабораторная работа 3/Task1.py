def found_index(list_products, product):
    for index in range(len(list_products)):  # С помощью цикла for перебираем элементы списка
        if list_products[index] == product:  # С помощью условия сравниваем элемент с заданным индексом с товаром
            return index  # Возвращаем индекс
    return None  # Возвращаем None, если товара нет в списке


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = found_index(items_list, find_item)  # Вызываем функцию
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
