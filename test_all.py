
""" Тест 3 Домашнее Задание 
Добавить в тестовый проект шаг добавления
поста после входа. Должна выполняться
проверка на наличие названия поста на странице
сразу после его создания."""


from testpage import OperationsHelper
import logging
import yaml
import time

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)

def test_step1(browser):
    logging.info("Test 1 started")
    testpage = OperationsHelper(browser) #делаем страницу экземпляром класса и передаем браузер
    testpage.go_to_site() #открывваем страницу
    testpage.enter_login('test') #вводим логин
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()
    test_page.get_blog()
    assert test_page.get_blog() == "Blog"


def test_step3(browser):
    logging.info("Test 3 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()
    test_page.click_button_create_post()
    test_page.input_title_post(testdata['title'])
    test_page.click_button_save_post()
    time.sleep(5)
    test_page.new_post()
    assert test_page.new_post() == "Check Text Post"


#Добавить в проект тест (test_step4) по проверке механики
#работы формы Contact Us. Должно проверятся
#открытие формы, ввод данных в поля, клик
#по кнопке и появление всплывающего alert.
#Совет:
#Переключиться на alert можно
#командой alert = self.driver.switch_to.alert
#Вывести текст alert.text


def test_step4(browser):
    logging.info("Test 4 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()

    test_page.click_contact()
    test_page.input_name(testdata["name"])
    test_page.input_email(testdata["email"])
    test_page.input_content(testdata["content"])
    time.sleep(3)
    test_page.click_button_contact_us()
    time.sleep(3)
    test_page.alert()

    assert test_page.alert() == "Form successfully submitted"