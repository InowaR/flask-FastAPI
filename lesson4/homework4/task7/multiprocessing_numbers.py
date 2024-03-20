import multiprocessing
import random
import time


arr = multiprocessing.Array('i', [0] * 10000000)


def fill_array_part(arr, start, end):
    for i in range(start, end):
        arr[i] = random.randint(1, 100)


def calculate_sum(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.put(partial_sum)


chunk_size = len(arr) // 10

fill_processes = []
start_time_fill = time.time()
for i in range(10):
    process = multiprocessing.Process(target=fill_array_part, args=(arr, i * chunk_size, (i + 1) * chunk_size))
    fill_processes.append(process)
    process.start()

for process in fill_processes:
    process.join()

end_time_fill = time.time()

sum_processes = []
results = multiprocessing.Queue()
start_time_sum = time.time()
for i in range(10):
    process = multiprocessing.Process(target=calculate_sum, args=(arr, i * chunk_size, (i + 1) * chunk_size, results))
    sum_processes.append(process)
    process.start()

for process in sum_processes:
    process.join()

end_time_sum = time.time()

total_sum = 0
while not results.empty():
    total_sum += results.get()

print(f"Время заполнения массива: {end_time_fill - start_time_fill:.6f} секунд")
print(f"Время вычисления суммы: {end_time_sum - start_time_sum:.6f} секунд")
print(f"Общее время: {end_time_sum - start_time_fill:.6f} секунд")
print(f"Сумма элементов массива: {total_sum}")
