from PIL import Image, ImageDraw  # Импорт модулей PIL для работы с изображениями
from selenium import webdriver  # Импорт модуля webdriver для автоматизации браузера
import os  # Импорт модуля os для работы с файловой системой
import sys  # Импорт модуля sys для доступа к системным параметрам


class ScreenAnalysis:
    STAGING_URL = 'http://www.yahoo.com'  # URL тестовой среды
    PRODUCTION_URL = 'http://www.yahoo.com'  # URL продакшн среды
    driver = None  # Инициализация переменной для драйвера

    def __init__(self):
        self.set_up()  # Выполнение настройки
        self.capture_screens()  # Захват скриншотов
        self.analyze()  # Анализ скриншотов
        self.clean_up()  # Очистка

    def set_up(self):
        self.driver = webdriver.PhantomJS()  # Инициализация драйвера PhantomJS

    def clean_up(self):
        self.driver.close()  # Закрытие драйвера

    def capture_screens(self):
        self.screenshot(self.STAGING_URL, 'screen_staging.png')  # Захват скриншота тестовой среды
        self.screenshot(self.PRODUCTION_URL, 'screen_production.png')  # Захват скриншота продакшн среды

    def screenshot(self, url, file_name):
        print("Capturing", url, "screenshot as", file_name, "...")
        self.driver.get(url)  # Загрузка страницы в браузер
        self.driver.set_window_size(1024, 768)  # Установка размера окна браузера
        self.driver.save_screenshot(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))  # Сохранение скриншота
        self.driver.get_screenshot_as_png()  # Получение скриншота в формате PNG
        print("Done.")

    def analyze(self):
        screenshot_staging = Image.open("screenshots/screen_staging.png")  # Открытие скриншота тестовой среды
        screenshot_production = Image.open("screenshots/screen_production.png")  # Открытие скриншота продакшн среды
        columns = 60  # Количество столбцов для анализа
        rows = 80  # Количество строк для анализа
        screen_width, screen_height = screenshot_staging.size  # Получение размеров скриншота тестовой среды

        block_width = ((screen_width - 1) // columns) + 1  # Вычисление ширины блока для анализа
        block_height = ((screen_height - 1) // rows) + 1  # Вычисление высоты блока для анализа
        for y in range(0, screen_height, block_height + 1):  # Итерация по координатам y блоков
            for x in range(0, screen_width, block_width + 1):  # Итерация по координатам x блоков
                region_staging = self.process_region(screenshot_staging, x, y, block_width,
                                                     block_height)  # Вызов функции для обработки региона тестовой среды
                region_production = self.process_region(screenshot_production, x, y, block_width,
                                                        block_height)  # Вызов функции для обработки региона продакшн среды

                if region_staging is not None and region_production is not None and region_production != region_staging:  # Проверка наличия обоих регионов и их различия
                    draw = ImageDraw.Draw(
                        screenshot_staging)  # Создание объекта для рисования на скриншоте тестовой среды
                    draw.rectangle((x, y, x + block_width, y + block_height),
                                   outline="red")  # Рисование прямоугольника вокруг области с различиями

        screenshot_staging.save("result.png")  # Сохранение результирующего скриншота

    def process_region(self, image, x, y, width, height):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 100

        for coordinateY in range(y, y + height):  # Итерация по координатам y пикселей внутри блока
            for coordinateX in range(x, x + width):  # Итерация по координатам x пикселей внутри блока
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))  # Получение значения пикселя
                    region_total += sum(pixel) / 4  # Вычисление суммы значений цветовых компонент пикселя
                except:
                    return

        return region_total / factor  # Возвращение усредненного значения для региона
