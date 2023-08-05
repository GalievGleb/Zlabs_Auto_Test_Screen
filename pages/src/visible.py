import os
from playwright.sync_api import Playwright, sync_playwright

screenshot_counter = 0

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto("http://localhost:5173/#/visuallyImpaired")

    click_with_screenshot(page, page.locator("label").nth(1))
    click_with_screenshot(page, page.get_by_title("Большой"))
    click_with_screenshot(page, page.get_by_role("button", name="A A"))
    click_with_screenshot(page, page.get_by_role("button", name="large"))
    click_with_screenshot(page, page.get_by_title("Черный на белом"))
    click_with_screenshot(page, page.get_by_title("Желтый на черном"))

    context.close()
    browser.close()


def take_screenshot(page, screenshot_name):
    project_root = os.getcwd()
    screenshots_dir = os.path.join(project_root, "screenshots_test")
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"screenshot_{screenshot_name}.png")
    page.screenshot(path=screenshot_path)


def click_with_screenshot(page, element):
    global screenshot_counter
    screenshot_counter += 1

    element.click()
    page.wait_for_timeout(500)  # Ожидаем 500 мс (0.5 секунды)
    take_screenshot(page, screenshot_counter)  # Сделать скриншот после клика на элементе


with sync_playwright() as playwright:
    run(playwright)
