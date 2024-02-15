from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then

@given('User is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://app.createsmart.io/login")

@when('User enters valid username and password')
def step_impl(context):
    username_field = context.driver.find_element(By.ID, 'mui-489')
    password_field = context.driver.find_element(By.ID, 'mui-490')

    username_field.send_keys("testersqa123@gmail.com")
    password_field.send_keys("Hello@12345")

@when('User clicks on the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[2]/div/form/div/div[4]/button')
    #login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()

@then('User should be logged in successfully')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/header/div/div[1]/div[1]/div/h1'))
        )
        print("Login successful!")
    finally:
        context.driver.quit()
