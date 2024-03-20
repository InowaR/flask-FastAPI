import asyncio
import aiohttp
import os
import time

urls = ['https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666389850_35-mykaleidoscope-ru-p-klassnaya-priroda-oboi'
        '-37.jpg',
        'https://ae04.alicdn.com/kf/A3b29b1df8590451098f96ffd0f3b9ce69.jpeg'
        ]


async def download_image(url, filename, images_folder="images"):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                os.makedirs(images_folder, exist_ok=True)
                full_filename = os.path.join(images_folder, filename)
                with open(full_filename, 'wb') as f:
                    f.write(await response.read())
    end_time = time.time()
    print(f"Скачано: {filename}, время: {end_time - start_time:.2f} сек.")


async def main(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        filename = os.path.basename(url)
        tasks.append(asyncio.create_task(download_image(url, filename)))
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} сек.")


asyncio.run(main(urls))
