# Додаткова інформація про timeit: https://docs.python.org/uk/3/library/timeit.html

mport random
import timeit
import matplotlib.pyplot as plt

def insertion_sort(arr):
    """Алгоритм сортування вставками"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Рекурсивне сортування злиттям"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Допоміжна функція злиття двох відсортованих списків"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_random_list(size):
    """Генерує список випадкових чисел заданого розміру"""
    return [random.randint(0, 10000) for _ in range(size)]

def measure_time(sort_func, data):
    """Вимірює час виконання функції сортування"""
    return timeit.timeit(lambda: sort_func(data.copy()), number=1)

def plot_results(sizes, results):
    """Будує графік часу виконання для кожного алгоритму"""
    for name, times in results.items():
        plt.plot(sizes, times, label=name)
    plt.xlabel("Розмір списку")
    plt.ylabel("Час виконання (сек)")
    plt.title("Порівняння алгоритмів сортування")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    sizes = [100, 500, 1000, 5000, 10000]
    results = {
        "Сортування вставками": [],
        "Сортування злиттям": [],
        "Timsort (вбудоване sorted)": [],
    }

    for size in sizes:
        data = generate_random_list(size)
        print(f"Тестування на {size} елементах...")

        results["Сортування вставками"].append(measure_time(insertion_sort, data))
        results["Сортування злиттям"].append(measure_time(merge_sort, data))
        results["Timsort (вбудоване sorted)"].append(measure_time(sorted, data))

    for name in results:
        print(f"\n{name}:")
        for size, t in zip(sizes, results[name]):
            print(f"  {size} елементів: {t:.5f} сек")

    plot_results(sizes, results)

if __name__ == "__main__":
    main()
