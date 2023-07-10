from PIL import Image, ImageDraw
import os


class ScreenAnalysis:
    def __init__(self):
        self.analyze()

    def analyze(self):
        screenshots_dir_staging = "screenshots_test"
        screenshots_dir_production = "screenshots_work"
        result_dir = "result_screenshots"
        columns = 30
        rows = 40

        # Создание директории для результатов, если она не существует
        os.makedirs(result_dir, exist_ok=True)

        for filename in os.listdir(screenshots_dir_staging):
            if filename.endswith(".png"):
                screenshot_staging_path = os.path.join(screenshots_dir_staging, filename)
                screenshot_production_path = os.path.join(screenshots_dir_production, filename)

                if os.path.exists(screenshot_production_path):
                    screenshot_staging = Image.open(screenshot_staging_path)
                    screenshot_production = Image.open(screenshot_production_path)

                    screen_width, screen_height = screenshot_staging.size
                    block_width = ((screen_width - 1) // columns) + 1
                    block_height = ((screen_height - 1) // rows) + 1
                    found_differences = False

                    for y in range(0, screen_height, block_height + 1):
                        for x in range(0, screen_width, block_width + 1):
                            region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                            region_production = self.process_region(screenshot_production, x, y, block_width,
                                                                    block_height)

                            if region_staging is not None and region_production is not None and region_production != region_staging:
                                draw = ImageDraw.Draw(screenshot_staging)
                                draw.rectangle((x, y, x + block_width, y + block_height), outline="red")
                                found_differences = True

                    if found_differences:
                        result_filename = f"result_{filename}"
                        result_path = os.path.join(result_dir, result_filename)
                        screenshot_staging.save(result_path)

    def process_region(self, image, x, y, width, height):
        region_total = 0
        factor = 100

        for coordinateY in range(y, y + height):
            for coordinateX in range(x, x + width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel) / 4
                except:
                    return

        return region_total / factor


ScreenAnalysis()
