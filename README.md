# Проект "Автоматизация скриншотных тестов с использованием Python, Playwright и Pillow"

## Введение

Данный проект представляет собой инструмент для автоматизации скриншотных тестов на языке Python с использованием библиотек Playwright и Pillow. Он предназначен для сриншотного тестирования в рамках различных лабораторий.

## Структура проекта

Все директории в проекте названы именами соответствующих лабораторий. Например: `biology`, что обеспечивает удобную организацию и управление тестами. В каждой из этих директорий мы обнаружим две подпапки:

1. `screenshot_test`: Эта директория содержит скриншоты, полученные в результате функционального тестирования. Скриншоты создаются автоматически и сохраняются в файлах с именем вида `имя_лаборатории_lab_page`. Например: `biology_lab_page`.

2. `screenshot_work`: В этой директории хранятся "рабочие" скриншоты, которые используются для сравнения. Они также имеют формат `screenshot_x`, где `x` соответствует конкретному тесту.

## Работа с тестами

Для выполнения скриншотного теста необходимо выполнить следующие шаги:

1. Выполнить команду `npm run dev` для ПО Zlabs

2. Запустите файл `имя_лаборатории_lab_page` в выбранной директории лаборатории.

3. В результате работы тестов будут автоматически созданы скриншоты функционального пути и сохранены в директорию `screenshot_test`.

4. В файле `имя_лаборатории_lab_page`, в функции `save_screenshot` поменять названия директории на `screenshot_work`, для последующего сравнения с директорией `screenshot_test`.

5. Для сравнения полученных скриншотов с "рабочими" скриншотами из директории `screenshot_work`, используйте файл `contrast`.

6. В директории `result_screenshots` будут сохранены скриншоты, которые имеют различия.

7. Красной сеткой будет выделено место различия. Пример: ![main_window](https://i.imgur.com/4rbr8S2.png)

## Используемые инструменты

- Playwright: Библиотека для автоматизации веб-тестирования, которая обеспечивает создание скриншотов на основе функциональных тестов.

- Pillow: Мощная библиотека для обработки и сравнения изображений, используется для анализа скриншотов и сравнения результатов.

## Установка зависимостей

Перед запуском проекта убедитесь, что у вас установлены необходимые зависимости. Для этого используйте команду в консоли 
```bash
pip install -r requirements.txt
```
