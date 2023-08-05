from playwright.sync_api import Playwright, sync_playwright
from base.base_class import BasePage

URL = "http://localhost:5173/#/visuallyImpaired"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    page.goto(URL)

    base_page = BasePage(page)

    elements = [
        # Начиная с 9 строчки копируем
        page.locator("label").nth(1),
        page.get_by_title("Большой"),
        page.get_by_role("button", name="A A"),
        page.get_by_role("button", name="large"),
        page.get_by_title("Черный на белом"),
        page.get_by_title("Желтый на черном"),
        # Заканчиваем до строчки context.close
    ]

    for idx, element in enumerate(elements, start=1):
        base_page.click_with_screenshot(element, name=f"{idx}")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
