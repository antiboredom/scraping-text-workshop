import asyncio
from playwright.async_api import async_playwright

URL = "https://news.ycombinator.com/front"
SELECTOR = ".titleline"
NEXT_BUTTON = ".hnmore"
MAX_PAGES = 10
SLEEP = 1000


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(URL)
        for page_number in range(MAX_PAGES):
            if SLEEP > 0:
                await page.wait_for_timeout(SLEEP)
            elements = await page.query_selector_all(SELECTOR)
            for el in elements:
                content = await el.text_content()
                print(content)
            if MAX_PAGES > 1 and NEXT_BUTTON != "":
                next_butt = await page.query_selector(NEXT_BUTTON, strict=False)
                await next_butt.click()
        await browser.close()


asyncio.run(main())
