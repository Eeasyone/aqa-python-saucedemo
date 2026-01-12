# AQA SauceDemo Login Tests

Автоматизированные UI-тесты авторизации для сайта  
https://www.saucedemo.com/

Проект выполнен в рамках тестового задания AQA Python.


## Описание

Проект автоматизирует проверку сценариев логина на сайте SauceDemo с использованием Selenium и паттерна Page Object.

Реализованы проверки:
- корректности перехода по URL
- отображения ключевых элементов страниц
- обработки ошибок авторизации
- устойчивости к задержкам загрузки

Тесты воспроизводимы и могут быть запущены как локально, так и в Docker-контейнере.


## Стек

- Python
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Allure Report
- Docker


## Покрытые сценарии

Реализовано **5 автотестов**:

1. Успешный логин  
   `standard_user / secret_sauce`

2. Логин с неверным паролем  
   `standard_user / wrong_password`

3. Логин заблокированного пользователя  
   `locked_out_user`

4. Логин с пустыми полями
    (поля username и password не заполнены)

5. Логин пользователем  
   `performance_glitch_user`  
   (проверка корректного перехода несмотря на задержки)


## Локальный запуск

### 1. Создание и активация виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Запуск тестов

```bash
pytest --alluredir=reports/allure-results
```

Для запуска с видимым браузером:

```bash
HEADLESS=false pytest --alluredir=reports/allure-results
```


## Allure отчёт

Для просмотра отчёта требуется установленный Allure CLI.

```bash
allure serve reports/allure-results --host 0.0.0.0 --port 39171
```

## Запуск в Docker (Python 3.10)

### Сборка образа

```bash
docker build -t aqa-saucedemo .
```

### Запуск тестов в контейнере

```bash
docker run --rm aqa-saucedemo
```

## Примечания

- Все зависимости зафиксированы в `requirements.txt`
- Тесты запускаются в headless-режиме по умолчанию
- В Docker используется Python 3.10, Chrome и chromedriver одной версии
- Проект не зависит от локальной версии Python и браузера
