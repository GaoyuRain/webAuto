"""
author :Rain
Date : 2019/07/10
Description :无头浏览器
"""
from pyppeteer import launch
import requests
from pyquery import PyQuery
import asyncio

url = 'http://quotes.toscrape.com/js/'
url1 = "http://localhost"


def test01():
    response = requests.get(url)
    doc = PyQuery(response.text)
    # print(doc)
    # 获取class=quote的元素数量
    print('quote:', doc('.quote').length)
    print('test')
    print('-' * 30)
    response1 = requests.get(url1)
    doc2 = PyQuery(response1.text)
    print('selected:', doc2('.red'))
    # print(doc2)


async def test02():
    driver = await launch()
    page = await driver.newPage()
    await page.goto(url)
    doc = PyQuery(await page.content())
    print('quote:', doc('.quote').length)
    await driver.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(test02())
