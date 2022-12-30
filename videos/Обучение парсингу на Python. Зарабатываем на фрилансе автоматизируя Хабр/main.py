import random
import aiohttp
import asyncio
from bs4 import BeautifulSoup


CATEGORIES = [
    "https://habr.com/ru/hub/programming",
    "https://habr.com/ru/hub/python"
]


with open("proxy.txt") as file:
    PROXY_LIST = ''.join(file.readlines()).split('\n')


async def send_request(url, rand_proxy) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=f"http://{rand_proxy}") as resp:
            return await resp.text(encoding="utf-8")


async def parse_category(category_url):
    random_proxy = random.choice(PROXY_LIST)
    html_response = await send_request(category_url, random_proxy)
    soup = BeautifulSoup(html_response, "lxml")
    pagination_block = soup.find("div", class_="tm-pagination__pages")
    pages_count = pagination_block.find_all("a", class_="tm-pagination__page")[-1].text.strip()
    print(f"category: {category_url} | pages: {pages_count}")

    for page in range(int(pages_count)):
        page_response = await send_request(
            url=f"{category_url}/page{page}/",
            rand_proxy=random_proxy
        )

        page_soup = BeautifulSoup(page_response, "lxml")
        articles = page_soup.find_all("article", class_="tm-articles-list__item")

        for article in articles:
            info_block = article.find("a", class_="tm-article-snippet__title-link")
            title = info_block.find("span").text.strip()
            link = f"https://habr.com{info_block.get('href')}"

            with open("articles.txt", "a") as file:
                category_name = category_url.split('/')[-1]
                result_string = f"{category_name} | {title} | {link}\n"
                file.write(result_string)
                print(result_string, end="")


async def main():
    data = [parse_category(category) for category in CATEGORIES]
    await asyncio.gather(*data)


if __name__ == "__main__":
    asyncio.run(main())