import pytest
from constants import BASE_URL, REGISTERED_LOGIN, REGISTERED_PASSWORD, GET_WEB_ELEMENT_TIMEOUT
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,720")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, GET_WEB_ELEMENT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.logo))
    return driver


@pytest.fixture
def login_page(main_page):
    main_page.find_element(
        *MainPageLocators.login_and_registration_button).click()
    WebDriverWait(main_page, GET_WEB_ELEMENT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.login_title))
    return main_page


@pytest.fixture
def main_page_loged_in(login_page, existing_creds):
    login_page.find_element(
        *LoginPageLocators.email_input).send_keys(existing_creds.get('email'))
    login_page.find_element(
        *LoginPageLocators.password_input).send_keys(existing_creds.get('password'))
    login_page.find_element(
        *LoginPageLocators.login_button).click()
    WebDriverWait(login_page, GET_WEB_ELEMENT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.username))
    return login_page


@pytest.fixture
def registration_page(login_page):
    login_page.find_element(
        *LoginPageLocators.no_account_button).click()
    WebDriverWait(login_page, GET_WEB_ELEMENT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(RegistrationPageLocators.registration_title))
    return login_page


@pytest.fixture
def fake():
    fake = Faker()
    return fake


@pytest.fixture
def fake_creds(fake):
    return {"email": fake.email(), "password": fake.password()}


@pytest.fixture
def fake_listing(fake):
    return {"name": fake.pystr(), "description": fake.pystr(), "price": fake.random_int(min=1, max=999999)}


@pytest.fixture
def fake_string(fake):
    return fake.pystr()


@pytest.fixture
def existing_creds():
    return {"email": REGISTERED_LOGIN, "password": REGISTERED_PASSWORD}
