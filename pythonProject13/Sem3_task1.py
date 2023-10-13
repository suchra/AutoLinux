# Задание

# Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.


import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Инициализация браузера (в данном случае, Chrome)
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()

def test_contact_us_form(browser):
    # Открытие страницы личного кабинета
    browser.get("https://test-stand.gb.ru/login")

    # Навигация к форме "Contact Us" (предположим, что это ссылка или кнопка на странице)
    contact_us_link = browser.find_element_by_link_text("Contact Us")
    contact_us_link.click()

    # Заполнение формы
    name_field = browser.find_element_by_id("name")
    name_field.send_keys("John Doe")

    email_field = browser.find_element_by_id("email")
    email_field.send_keys("johndoe@example.com")

    message_field = browser.find_element_by_id("message")
    message_field.send_keys("This is a test message")

    submit_button = browser.find_element_by_id("submit_button")
    submit_button.click()

    # Переключение на alert
    alert = browser.switch_to.alert

    # Проверка, что alert текст содержит ожидаемое сообщение
    assert "Your message has been sent successfully" in alert.text

    # Закрытие alert
    alert.accept()