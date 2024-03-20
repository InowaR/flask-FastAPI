import os
import time
import requests
from multiprocessing import Process, Queue

urls = ['https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666389850_35-mykaleidoscope-ru-p-klassnaya-priroda-oboi'
        '-37.jpg',
        'https://ae04.alicdn.com/kf/A3b29b1df8590451098f96ffd0f3b9ce69.jpeg'
        ]


def download_image(url, filename, queue, images_folder="images"):
    start_time = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(images_folder, exist_ok=True)
        full_filename = os.path.join(images_folder, filename)
        with open(full_filename, 'wb') as f:
            f.write(response.content)
    end_time = time.time()
    queue.put((filename, end_time - start_time))


def main(urls):
    import time
    start_time = time.time()
    queue = Queue()
    processes = []
    for url in urls:
        filename = os.path.basename(url)
        process = Process(target=download_image, args=(url, filename, queue))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    results = []
    while not queue.empty():
        filename, process_time = queue.get()
        results.append((filename, process_time))

    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} сек.")
    for filename, process_time in results:
        print(f"Скачано: {filename}, время: {process_time:.2f} сек.")


main(urls)
