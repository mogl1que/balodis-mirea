def insertion_sort(array):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(array)):
        key = array[i]  # Текущий элемент, который нужно вставить
        j = i - 1       # Индекс предыдущего элемента
        
        # Перемещаем элементы array[0..i-1], которые больше key
        # на одну позицию вперед
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        
        # Вставляем key на правильное место
        array[j + 1] = key

def print_array(array):
    # Выводим элементы массива через пробел
    for value in array:
        print(value, end=" ")
    print()

# Основная функция для тестирования
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    
    print("Исходный массив:")
    print_array(array)
    
    insertion_sort(array)
    
    print("Отсортированный массив:")
    print_array(array)
