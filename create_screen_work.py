import os
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )  # Установка размера окна браузера

    page = context.new_page()
    time.sleep(2)
    page.goto("http://localhost:5173/")
    time.sleep(2)
    save_screenshot(page, "screenshot1")  # Сохранение нулевого скриншота
    page.get_by_role("navigation").locator("div").filter(has_text="Датчики").click()
    time.sleep(2)
    save_screenshot(page, "screenshot2")  # Сохранение первого скриншота
    time.sleep(2)
    page.get_by_text("Bluetooth", exact=True).click()
    time.sleep(2)
    save_screenshot(page, "screenshot3")  # Сохранение второго скриншота
    time.sleep(2)
    page.locator("html").press("Alt+s+1")
    time.sleep(2)
    save_screenshot(page, "screenshot4")  # Сохранение третьего скриншота
    page.get_by_text("Лаборатория(Физика)").click()
    time.sleep(2)
    save_screenshot(page, "screenshot5")  # Сохранение четвертого скриншота
    time.sleep(2)
    page.get_by_role("navigation").get_by_text("Датчик T эксп.").click()
    time.sleep(2)
    save_screenshot(page, "screenshot6")  # Сохранение пятого скриншота

    context.close()
    browser.close()


def save_screenshot(page, name):
    screenshots_dir = "screenshots_work"
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"{name}.png")
    page.screenshot(path=screenshot_path)


with sync_playwright() as playwright:
    run(playwright)