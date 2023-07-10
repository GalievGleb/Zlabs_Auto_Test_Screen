import os
import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    # ---------------------8
    # ---------------------end
    context.close()
    browser.close()


def save_screenshot(page, name):
    project_root = os.getcwd()  # Получаем текущую рабочую директорию (корень проекта)
    screenshots_dir = os.path.join(project_root, "screenshots_test")
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"{name}.png")
    page.screenshot(path=screenshot_path)


with sync_playwright() as playwright:
    run(playwright)
    # time.sleep(0.5)
    # save_screenshot(page, "screenshot66")
