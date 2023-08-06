from playwright.sync_api import Playwright, sync_playwright
from base.base_class import BasePage
import re

URL = "http://localhost:5173/#/sensors?pageIndex=undefined"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    page.goto(URL)

    base_page = BasePage(page)
    page.locator("body").press("Alt+s+1"),

    elements = [
        # Начиная с 9 строчки копируем
        page.get_by_text("Лаборатория(Физика)"),
        page.get_by_role("navigation").get_by_text("Датчик T эксп."),
        page.get_by_text("Датчик P абс."),
        page.get_by_text("Тесламетр"),
        page.get_by_text("Вольтметр"),
        page.get_by_text("Амперметр"),
        page.get_by_text("Датчик ускорения. Ось X"),
        page.get_by_text("Датчик ускорения. Ось Y"),
        page.get_by_text("Датчик ускорения. Ось Z")
        # Заканчиваем до строчки context.close
    ]

    for idx, element in enumerate(elements, start=1):
        base_page.click_with_screenshot(element, name=f"{idx}")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
