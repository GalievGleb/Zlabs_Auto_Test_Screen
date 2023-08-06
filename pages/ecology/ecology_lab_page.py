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
    page.locator("body").press("Alt+s+3"),

    elements = [
        # Начиная с 9 строчки копируем
        page.get_by_text("Лаборатория(Экология)"),
        page.get_by_role("navigation").get_by_text("Датчик электропроводимости"),
        page.get_by_text("Датчик T эксп."),
        page.get_by_text("Иономер"),
        page.get_by_text("Датчик влажности"),
        page.get_by_text("Датчик освещенности"),
        page.get_by_text("Датчик Т окр."),
        # Заканчиваем до строчки context.close
    ]

    for idx, element in enumerate(elements, start=1):
        base_page.click_with_screenshot(element, name=f"{idx}")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
