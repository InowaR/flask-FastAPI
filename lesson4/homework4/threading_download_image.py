import os
import time
from threading import Thread
import requests

urls = ['https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666389850_35-mykaleidoscope-ru-p-klassnaya-priroda-oboi'
        '-37.jpg',
        'https://ae04.alicdn.com/kf/A3b29b1df8590451098f96ffd0f3b9ce69.jpeg'
        ]


def download_image(url, filename, images_folder="images"):
    start_time = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(images_folder, exist_ok=True)
        full_filename = os.path.join(images_folder, filename)
        with open(full_filename, 'wb') as f:
            f.write(response.content)
    end_time = time.time()
    print(f"Скачано: {filename}, время: {end_time - start_time:.2f} сек.")


def main(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        filename = os.path.basename(url)
        thread = Thread(target=download_image, args=(url, filename))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} сек.")


main(urls)
