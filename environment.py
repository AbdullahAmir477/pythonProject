from selenium import webdriver

def before_all(context):
    # Set up Selenium WebDriver
    context.driver = webdriver.Chrome()

def after_all(context):
    # Quit Selenium WebDriver
    context.driver.quit()
