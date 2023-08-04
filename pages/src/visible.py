import os
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto("http://localhost:5173/#/visuallyImpaired")
    page.locator("label").nth(1).click()
    page.get_by_title("Большой").click()
    page.get_by_role("button", name="A A").click()
    page.get_by_role("button", name="large").click()
    page.get_by_title("Черный на белом").click()
    page.get_by_title("Желтый на черном").click()
    context.close()
    browser.close()


def take_screenshot(page):
    project_root = os.getcwd()
    screenshots_dir = os.path.join(project_root, "screenshots_test")
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_counter = len(os.listdir(screenshots_dir)) + 1
    screenshot_name = f"screenshot_{str(screenshot_counter)}"
    screenshot_path = os.path.join(screenshots_dir, f"{screenshot_name}.png")
    page.screenshot(path=screenshot_path)


def click_element_with_text(page, text):
    element = page.locator("div").filter(has_text=text).nth(3)  # Выбираем 4-й элемент с текстом "Датчики"
    element.click()
    page.wait_for_timeout(500)  # Ожидаем 500 мс (0.5 секунды)
    take_screenshot(page)  # Сделать скриншот после клика на элементе


with sync_playwright() as playwright:
    run(playwright)
    # time.sleep(0.5)
    # save_screenshot(page, "screenshot66")
    # page.locator("html").press("Alt+s+1")
