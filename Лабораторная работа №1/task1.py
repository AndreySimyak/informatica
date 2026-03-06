numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing_item = 4 # находим пропущенный элемент списка

count_of_numbers = len(numbers) # считаем число элементов списка
sum_of_numbers = sum(numbers[:index_missing_item]) + sum(numbers[index_missing_item+1:]) # считаем сумму элементов списка без пропущенного
average_of_numbers = sum_of_numbers / count_of_numbers # считаем среднее арифметическое

numbers[index_missing_item] = average_of_numbers # заменяем пропущенный элемент на ср. арифметическое
print("Измененный список:", numbers)
