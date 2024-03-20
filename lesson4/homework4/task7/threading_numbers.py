import threading
import random
import time


arr = [0] * 10000000


def fill_array_part(arr, start, end):
    for i in range(start, end):
        arr[i] = random.randint(1, 100)


def calculate_sum(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.append(partial_sum)


chunk_size = len(arr) // 50

fill_threads = []
start_time_fill = time.time()
for i in range(50):
    thread = threading.Thread(target=fill_array_part, args=(arr, i * chunk_size, (i + 1) * chunk_size))
    fill_threads.append(thread)
    thread.start()

for thread in fill_threads:
    thread.join()

end_time_fill = time.time()

sum_threads = []
results = []
start_time_sum = time.time()
for i in range(50):
    thread = threading.Thread(target=calculate_sum, args=(arr, i * chunk_size, (i + 1) * chunk_size, results))
    sum_threads.append(thread)
    thread.start()

for thread in sum_threads:
    thread.join()

end_time_sum = time.time()

total_sum = sum(results)

print(f"Время заполнения массива: {end_time_fill - start_time_fill:.6f} секунд")
print(f"Время вычисления суммы: {end_time_sum - start_time_sum:.6f} секунд")
print(f"Общее время: {end_time_sum - start_time_fill:.6f} секунд")
print(f"Сумма элементов массива: {total_sum}")
