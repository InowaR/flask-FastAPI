import asyncio
import os
import time

import aiofiles

MY_PATH = '.'


async def worker(file_):
    async with aiofiles.open(file_, 'r', encoding='utf-8') as f:
        content = await f.read()
        print(f'Слов в {file_} : {len(content.split())}')


async def main():
    for root, dirs, file_name in os.walk(MY_PATH):
        for f in file_name:
            task = asyncio.create_task(worker(f))
            await task


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Время выполнения: {time.time() - start_time}')
