import os
import time
import random
import aiohttp
import asyncio
import aiofiles
from time import perf_counter


SITE = "https://thispersondoesnotexist.com/image"
IMAGES_COUNT = 50
# PROXY = "12.155.121.214:8000"


def generate_filename(file_extension):
    temp = str(int(time.time()))
    for _ in range(5):
        temp += chr(random.randint(65, 75))
    return f"{temp}.{file_extension}"


async def download_image(image_num):
    async with aiohttp.ClientSession() as session:
        async with session.get(SITE, proxy=None) as response:
            extension = response.headers['content-type'].split('/')[-1]
            filename = os.path.join("images", generate_filename(extension))

            async with aiofiles.open(filename, mode='wb') as file:
                async for chunk in response.content.iter_chunked(64 * 1024):
                    await file.write(chunk)
    print(f"image: {image_num + 1} finished..")


async def main():
    image_tasks = []
    for image_num in range(IMAGES_COUNT):
        image_tasks.append(asyncio.create_task(download_image(image_num)))
    await asyncio.gather(*image_tasks)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    print(f"time: {(perf_counter() - start):.02f}")
