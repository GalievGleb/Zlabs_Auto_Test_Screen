from PIL import Image, ImageDraw
import os


class ScreenAnalysis:
    def __init__(self):
        self.analyze()

    def analyze(self):
        screenshot_staging = Image.open("screenshots_work/screenshot5.png")
        screenshot_production = Image.open("screenshots_work/screenshot6.png")
        columns = 30
        rows = 40
        screen_width, screen_height = screenshot_staging.size
        block_width = ((screen_width - 1) // columns) + 1
        block_height = ((screen_height - 1) // rows) + 1
        for y in range(0, screen_height, block_height + 1):
            for x in range(0, screen_width, block_width + 1):
                region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_production, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:
                    draw = ImageDraw.Draw(screenshot_staging)
                    draw.rectangle((x, y, x + block_width, y + block_height), outline="red")

        screenshot_staging.save("result.png")

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