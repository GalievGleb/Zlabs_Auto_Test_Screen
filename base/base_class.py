import os

class BasePage:
    def __init__(self, page):
        self.page = page

    def take_screenshot(self, name):
        project_root = os.getcwd()
        screenshots_dir = os.path.join(project_root, "screenshots_test")
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_name = f"screenshot_{name}.png"
        screenshot_path = os.path.join(screenshots_dir, screenshot_name)
        self.page.screenshot(path=screenshot_path)

    def click_with_screenshot(self, element, name):
        element.click()
        self.page.wait_for_load_state("networkidle")  # Wait for the page to become idle
        self.take_screenshot(name)
