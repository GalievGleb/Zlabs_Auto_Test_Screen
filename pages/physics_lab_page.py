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
    page.goto("http://localhost:5173/")
    page.locator("div").filter(has_text=re.compile(r"^Датчики$")).click()
    save_screenshot(page, "screenshot1")
    page.locator("html").press("Alt+s+1")
    save_screenshot(page, "screenshot2")
    page.locator("div").filter(has_text=re.compile(r"^Лаборатория\(Физика\)$")).click()
    save_screenshot(page, "screenshot3")
    page.locator("div").filter(has_text=re.compile(r"^Датчик T эксп\.Подключен$")).get_by_role("button",
                                                                                               name="Подключен").click()
    save_screenshot(page, "screenshot4")
    page.locator("div").filter(has_text=re.compile(r"^Датчик P абс\.Подключен$")).get_by_role("button",
                                                                                              name="Подключен").click()
    save_screenshot(page, "screenshot5")
    page.locator("div").filter(has_text=re.compile(r"^ТесламетрПодключен$")).get_by_role("button",
                                                                                         name="Подключен").click()
    time.sleep(1)
    save_screenshot(page, "screenshot6")
    page.locator("div").filter(has_text=re.compile(r"^ВольтметрПодключен$")).get_by_role("button",
                                                                                         name="Подключен").click()
    save_screenshot(page, "screenshot7")
    page.locator("div").filter(has_text=re.compile(r"^АмперметрПодключен$")).get_by_role("button",
                                                                                         name="Подключен").click()
    save_screenshot(page, "screenshot8")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось XПодключен$")).get_by_role("button",
                                                                                                        name="Подключен").click()
    save_screenshot(page, "screenshot9")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось YПодключен$")).get_by_role("button",
                                                                                                        name="Подключен").click()
    save_screenshot(page, "screenshot10")
    page.get_by_role("button", name="Подключен").click()
    page.locator("div").filter(has_text=re.compile(r"^Датчик T эксп\.Отключен$")).get_by_role("button",
                                                                                              name="Отключен").click()
    save_screenshot(page, "screenshot11")
    page.locator("div").filter(has_text=re.compile(r"^Датчик P абс\.Отключен$")).get_by_role("button",
                                                                                             name="Отключен").click()
    save_screenshot(page, "screenshot12")
    page.locator("div").filter(has_text=re.compile(r"^ТесламетрОтключен$")).get_by_role("button",
                                                                                        name="Отключен").click()
    save_screenshot(page, "screenshot13")
    page.locator("div").filter(has_text=re.compile(r"^ВольтметрОтключен$")).get_by_role("button",
                                                                                        name="Отключен").click()
    save_screenshot(page, "screenshot14")
    page.locator("div").filter(has_text=re.compile(r"^АмперметрОтключен$")).get_by_role("button",
                                                                                        name="Отключен").click()
    save_screenshot(page, "screenshot15")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось XОтключен$")).get_by_role("button",
                                                                                                       name="Отключен").click()
    save_screenshot(page, "screenshot16")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось YОтключен$")).get_by_role("button",
                                                                                                       name="Отключен").click()
    save_screenshot(page, "screenshot17")
    page.get_by_role("button", name="Отключен").click()
    save_screenshot(page, "screenshot18")
    page.get_by_role("navigation").get_by_text("Датчик T эксп.").click()
    save_screenshot(page, "screenshot19")
    page.locator("div").filter(has_text=re.compile(r"^Датчик P абс\.$")).click()
    save_screenshot(page, "screenshot20")
    page.locator("div").filter(has_text=re.compile(r"^Тесламетр$")).click()
    save_screenshot(page, "screenshot21")
    page.locator("div").filter(has_text=re.compile(r"^Вольтметр$")).click()
    save_screenshot(page, "screenshot22")
    page.locator("div").filter(has_text=re.compile(r"^Амперметр$")).click()
    save_screenshot(page, "screenshot23")
    page.get_by_text("Датчик ускорения. Ось X").click()
    save_screenshot(page, "screenshot24")
    page.get_by_text("Датчик ускорения. Ось Y").click()
    save_screenshot(page, "screenshot25")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось Z$")).click()
    save_screenshot(page, "screenshot26")
    page.get_by_text("Настройки эксперимента").click()
    save_screenshot(page, "screenshot27")
    page.locator("div").filter(has_text=re.compile(r"^СекундМинут$")).get_by_role("combobox").select_option("1")
    save_screenshot(page, "screenshot28")
    page.locator("div").filter(has_text=re.compile(r"^Формат времениСекундомерММ:ССЧЧ:ММ$")).get_by_role(
        "combobox").select_option("0")
    save_screenshot(page, "screenshot29")
    page.locator("div").filter(has_text=re.compile(r"^Формат времениСекундомерММ:ССЧЧ:ММ$")).get_by_role(
        "combobox").select_option("2")
    save_screenshot(page, "screenshot30")
    page.locator("div").filter(
        has_text=re.compile(r"^Вид графика по умолчаниюВручнуюЛинияЛиния с точкамиТочки$")).get_by_role(
        "combobox").select_option("1")
    save_screenshot(page, "screenshot31")
    page.locator("div").filter(
        has_text=re.compile(r"^Вид графика по умолчаниюВручнуюЛинияЛиния с точкамиТочки$")).get_by_role(
        "combobox").select_option("2")
    save_screenshot(page, "screenshot32")
    page.locator("div").filter(
        has_text=re.compile(r"^Вид графика по умолчаниюВручнуюЛинияЛиния с точкамиТочки$")).get_by_role(
        "combobox").select_option("3")
    save_screenshot(page, "screenshot33")
    page.locator("div").filter(has_text=re.compile(r"^Связка датчиков$")).click()
    save_screenshot(page, "screenshot34")
    page.get_by_placeholder("Название").click()
    save_screenshot(page, "screenshot35")
    page.get_by_placeholder("Название").fill("1")
    save_screenshot(page, "screenshot36")
    page.get_by_role("button", name="Создать").click()
    save_screenshot(page, "screenshot37")
    page.get_by_role("button", name="Перейти").click()
    save_screenshot(page, "screenshot38")
    page.locator("div").filter(has_text=re.compile(r"^Датчик T эксп\.Отключен$")).get_by_role("button",
                                                                                              name="Отключен").click()
    save_screenshot(page, "screenshot38")
    page.locator("div").filter(has_text=re.compile(r"^Датчик P абс\.Отключен$")).get_by_role("button",
                                                                                             name="Отключен").click()
    save_screenshot(page, "screenshot40")
    page.locator("div").filter(has_text=re.compile(r"^ТесламетрОтключен$")).get_by_role("button",
                                                                                        name="Отключен").click()
    save_screenshot(page, "screenshot41")
    page.locator("div").filter(has_text=re.compile(r"^ВольтметрОтключен$")).get_by_role("button",
                                                                                        name="Отключен").click()
    save_screenshot(page, "screenshot41")
    page.locator("div").filter(has_text=re.compile(r"^АмперметрОтключен$")).get_by_role("button",
                                                                                        name="Отключен").click()
    save_screenshot(page, "screenshot42")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось XОтключен$")).get_by_role("button",
                                                                                                       name="Отключен").click()
    save_screenshot(page, "screenshot43")
    page.locator("div").filter(has_text=re.compile(r"^Датчик ускорения\. Ось YОтключен$")).get_by_role("button",
                                                                                                       name="Отключен").click()
    save_screenshot(page, "screenshot44")
    page.get_by_role("button", name="Отключен").click()
    save_screenshot(page, "screenshot45")
    page.get_by_role("button", name="Назад").click()
    save_screenshot(page, "screenshot46")
    page.locator("div").filter(has_text=re.compile(r"^Сеанс автономной работы$")).click()
    save_screenshot(page, "screenshot47")
    page.get_by_role("button", name="Запустить сеанс автономной работы").click()
    page.get_by_role("button", name="⚒️ Работа с данными сеанса").click()
    save_screenshot(page, "screenshot47")
    page.locator(".measure-graphics").first.click()
    save_screenshot(page, "screenshot48")
    page.locator(".measure-graphics").first.click()
    save_screenshot(page, "screenshot49")
    page.locator(".sc-gueYoa").click()
    save_screenshot(page, "screenshot50")
    page.locator("div").filter(has_text=re.compile(r"^Калибровка$")).click()
    save_screenshot(page, "screenshot51")
    page.get_by_role("textbox").click()
    save_screenshot(page, "screenshot52")
    page.get_by_role("textbox").fill("12345")
    save_screenshot(page, "screenshot53")
    page.get_by_role("button", name="Подтвердить").click()
    save_screenshot(page, "screenshot54")
    page.locator("div").filter(has_text=re.compile(r"^Датчик T эксп\.Калибровать$")).get_by_role("button",
                                                                                                 name="Калибровать").click()
    save_screenshot(page, "screenshot55")
    page.locator("span").filter(has_text="Калибровка датчика Датчик T эксп.").get_by_role("button").click()
    save_screenshot(page, "screenshot56")
    page.locator("div").filter(has_text=re.compile(r"^Датчик P абс\.Калибровать$")).get_by_role("button",
                                                                                                name="Калибровать").click()
    save_screenshot(page, "screenshot57")
    page.locator("span").filter(has_text="Калибровка датчика Датчик P абс.").get_by_role("button").click()
    save_screenshot(page, "screenshot58")
    page.locator("div").filter(has_text=re.compile(r"^ТесламетрКалибровать$")).get_by_role("button",
                                                                                           name="Калибровать").click()
    save_screenshot(page, "screenshot59")
    page.locator("span").filter(has_text="Калибровка датчика Тесламетр").get_by_role("button").click()
    save_screenshot(page, "screenshot60")
    page.locator("div").filter(has_text=re.compile(r"^ВольтметрКалибровать$")).get_by_role("button",
                                                                                           name="Калибровать").click()
    save_screenshot(page, "screenshot61")
    page.locator("span").filter(has_text="Калибровка датчика Вольтметр").get_by_role("button").click()
    save_screenshot(page, "screenshot62")
    page.locator("div").filter(has_text=re.compile(r"^АмперметрКалибровать$")).get_by_role("button",
                                                                                           name="Калибровать").click()
    save_screenshot(page, "screenshot63")
    page.locator("span").filter(has_text="Калибровка датчика Амперметр").get_by_role("button").click()
    save_screenshot(page, "screenshot64")
    page.get_by_text("О программе").click()
    save_screenshot(page, "screenshot65")
    page.get_by_text("О программеВерсия ПО:3.1.2Выберите лабораторию:PHYS #3355185Инструкция:Открыть и").click()
    save_screenshot(page, "screenshot66")

    # ---------------------
    context.close()
    browser.close()


def save_screenshot(page, name):
    project_root = os.getcwd()  # Получаем текущую рабочую директорию (корень проекта)
    screenshots_dir = os.path.join(project_root, "screenshots_work")
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"{name}.png")
    page.screenshot(path=screenshot_path)


with sync_playwright() as playwright:
    run(playwright)
