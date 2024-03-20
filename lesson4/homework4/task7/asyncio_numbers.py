import asyncio
import random
import time


arr = [0] * 10000000


async def fill_array_part(arr, start, end):
    for i in range(start, end):
        arr[i] = random.randint(1, 100)


async def calculate_sum(arr, start, end):
    return sum(arr[start:end])


async def main():
    chunk_size = len(arr) // 10

    fill_tasks = []
    start_time_fill = time.time()
    for i in range(10):
        task = asyncio.create_task(fill_array_part(arr, i * chunk_size, (i + 1) * chunk_size))
        fill_tasks.append(task)

    await asyncio.gather(*fill_tasks)
    end_time_fill = time.time()

    sum_tasks = []
    start_time_sum = time.time()
    for i in range(10):
        task = asyncio.create_task(calculate_sum(arr, i * chunk_size, (i + 1) * chunk_size))
        sum_tasks.append(task)

    partial_sums = await asyncio.gather(*sum_tasks)
    end_time_sum = time.time()

    total_sum = sum(partial_sums)

    print(f"Время заполнения: {end_time_fill - start_time_fill:.6f} секунд")
    print(f"Время вычисления суммы: {end_time_sum - start_time_sum:.6f} секунд")
    print(f"Общее время: {end_time_sum - start_time_fill:.6f} секунд")
    print(f"Сумма элементов массива: {total_sum}")


if __name__ == '__main__':
    asyncio.run(main())
