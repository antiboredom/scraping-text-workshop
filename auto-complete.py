import asyncio
from playwright.async_api import async_playwright

URL = "https://bing.com"
SEARCH_NAME = "q"
RESULTS_SELECTOR = "#sa_ul li"
QUERY = "what is"
EXTRA_RESULTS = False


async def main():
    async with async_playwright() as p:
        letters = "abcdefghijklmnopqrstuvwxyz"
        if EXTRA_RESULTS:
            search_letters = []
            for l1 in letters:
                for l2 in letters:
                    search_letters.append(l1 + l2)
        else:
            search_letters = letters

        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(URL)
        await page.wait_for_timeout(2000)

        inp_field = await page.query_selector(f"[name={SEARCH_NAME}]", strict=False)

        for letter in search_letters:
            await inp_field.fill(QUERY + " " + letter)
            await page.wait_for_timeout(1000)
            results = await page.query_selector_all(RESULTS_SELECTOR)
            for r in results:
                content = await r.text_content()
                print(content)

        await browser.close()


asyncio.run(main())
