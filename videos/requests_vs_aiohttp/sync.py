import os
import time
import random
import requests
from time import perf_counter


SITE = "https://thispersondoesnotexist.com/image"
IMAGES_COUNT = 50
# PROXY = "12.155.121.214:8000"


def generate_filename(file_extension):
    temp = str(int(time.time()))
    for _ in range(5):
        temp += chr(random.randint(65, 75))
    return f"{temp}.{file_extension}"


def main():
    # proxies = {
    #     "http": f"http://{PROXY}",
    #     "https": f"http://{PROXY}"
    # }

    for image_num in range(IMAGES_COUNT):
        response = requests.get(SITE, proxies=None)
        extension = response.headers["content-type"].split('/')[-1]
        filename = generate_filename(extension)

        with open(os.path.join("images", filename), "wb") as file:
            file.write(response.content)
        print(f"image: {image_num + 1} finished..")


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"time: {(perf_counter() - start):.02f}")
