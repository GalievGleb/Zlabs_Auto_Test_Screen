from playwright.sync_api import Playwright, sync_playwright
from base.base_class import BasePage


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    page.goto("http://localhost:5173/#/visuallyImpaired")

    base_page = BasePage(page)

    base_page.click_with_screenshot(page.locator("label").nth(1))
    base_page.click_with_screenshot(page.get_by_title("Большой"))
    base_page.click_with_screenshot(page.get_by_role("button", name="A A"))
    base_page.click_with_screenshot(page.get_by_role("button", name="large"))
    base_page.click_with_screenshot(page.get_by_title("Черный на белом"))
    base_page.click_with_screenshot(page.get_by_title("Желтый на черном"))

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
