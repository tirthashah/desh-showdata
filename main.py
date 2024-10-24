import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
def configure_chrome_options():
    options = Options()
    return options

# Create the driver
def create_driver():
    options = configure_chrome_options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def login(driver):
    driver.get("https://bitnbinary.bnbrun.com/dashboard")
    time.sleep(4)

    email_input = driver.find_element(By.XPATH, './/input[@name="email"]')
    email_input.send_keys("tirtha.shah@bitnbinary.com")

    password_input = driver.find_element(By.XPATH, './/input[@name="password"]')
    password_input.send_keys("Tirtha@12")

    sign_in = driver.find_element(By.XPATH, './/button[@id="kt_sign_in_submit"]')
    sign_in.click()

def navigate_to_attendance(driver):
    attendance_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Attendance"]'))
    )
    attendance_link.click()
    time.sleep(5)

def navigate_to_projects_management(driver):
    projects_management_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Projects Management"]'))
    )
    projects_management_menu.click()

    projects_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/a[@class="menu-link without-sub" and .//span[@class="menu-title" and normalize-space(text())="Projects"]]'))
    )
    projects_menu.click()

    view_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="badge badge-light-primary fw-bold me-auto px-4 py-3" and normalize-space(text())="View"]'))
    )
    view_button.click()

def click_filter_select(driver):
    filter_select_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/a[contains(text(),"Bit & Binary")]'))
    )
    filter_select_button.click()
    time.sleep(5)

def navigate_to_public_data(driver):
    public_data_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="publicdata"]'))
    )
    public_data_link.click()
    time.sleep(5)

def navigate_to_overview(driver):
    organization_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Organization"]'))
    )
    organization_menu.click()

    overview = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Overview"]'))
    )
    overview.click()

    edit_profile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_profile_details_view"]/div[1]/a'))
    )
    edit_profile.click()

    description = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, './/textarea[@formcontrolname="description"]'))
    )
    description.send_keys("about work")

    checkboxes = [
        './/input[@type="checkbox" and @formcontrolname="show_products_in_bnbmart "]',
        './/input[@type="checkbox" and @formcontrolname="show_price_in_bnbmart"]',
        './/input[@type="checkbox" and @formcontrolname="show_jobs_in_bnbhiring"]'
    ]

    for checkbox_xpath in checkboxes:
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, checkbox_xpath))
        )
        checkbox.click()

    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/button[@type="submit" and normalize-space(text())="Save"]'))
    )
    save_button.click()

def main():
    driver = create_driver()
    try:
        login(driver)
        navigate_to_attendance(driver)
        navigate_to_projects_management(driver)
        click_filter_select(driver)
        navigate_to_public_data(driver)
        navigate_to_overview(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
