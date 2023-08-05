import os

class BasePage:
    screenshot_counter = 0

    def __init__(self, page):
        self.page = page

    def take_screenshot(self, name):
        project_root = os.getcwd()
        screenshots_dir = os.path.join(project_root, "screenshots_test")
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_name = f"screenshot_{name}"
        screenshot_path = os.path.join(screenshots_dir, f"{screenshot_name}.png")
        self.page.screenshot(path=screenshot_path)

    def click_with_screenshot(self, element):
        BasePage.screenshot_counter += 1

        element.click()
        self.page.wait_for_timeout(500)  # Ожидаем 500 мс (0.5 секунды)
        self.take_screenshot(BasePage.screenshot_counter)  # Сделать скриншот после клика на элементе
