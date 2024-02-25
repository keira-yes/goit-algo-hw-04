import timeit
import random

# Імпорт функцій алгоритмів
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from tim_sort import tim_sort
from tim_sorted import tim_sorted

# Генеруємо тестові дані
data = {
    "Small": [random.randint(0, 100) for _ in range(100)],
    "Medium": [random.randint(0, 1000) for _ in range(1000)],
    "Large": [random.randint(0, 10000) for _ in range(10000)]
}

# Вимірюємо час виконання для кожного алгоритму на кожному наборі даних
for name, data in data.items():
    print(f"Data Set: {name}")
    
    # Сортування злиттям
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    print(f"Merge Sort Time: {merge_sort_time}")
    
    # Сортування вставками
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    print(f"Insertion Sort Time: {insertion_sort_time}")
    
    # Timsort 
    tim_sort_time = timeit.timeit(lambda: tim_sort(data.copy()), number=1)
    print(f"Timsort Time: {tim_sort_time}")
    
	# Timsorted
    tim_sorted_time = timeit.timeit(lambda: tim_sorted(data.copy()), number=1)
    print(f"Timsorted Time: {tim_sorted_time}")
    print()