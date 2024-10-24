import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
def configure_chrome_options():
    print("Configuring Chrome options...")
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Required for running as root in some CI environments
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--window-size=1920x1080")  # Set window size for headless mode
    return options

# Create the driver
def create_driver():
    print("Creating WebDriver...")
    options = configure_chrome_options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("WebDriver created successfully.")
    return driver

def login(driver):
    print("Navigating to login page...")
    driver.get("https://bitnbinary.bnbrun.com/dashboard")
    time.sleep(4)

    print("Filling in email and password...")
    email_input = driver.find_element(By.XPATH, './/input[@name="email"]')
    email_input.send_keys("tirtha.shah@bitnbinary.com")

    password_input = driver.find_element(By.XPATH, './/input[@name="password"]')
    password_input.send_keys("Tirtha@12")

    print("Clicking the sign-in button...")
    sign_in = driver.find_element(By.XPATH, './/button[@id="kt_sign_in_submit"]')
    sign_in.click()

def navigate_to_attendance(driver):
    print("Navigating to Attendance section...")
    attendance_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Attendance"]'))
    )
    attendance_link.click()
    time.sleep(5)

def navigate_to_projects_management(driver):
    print("Navigating to Projects Management section...")
    projects_management_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Projects Management"]'))
    )
    projects_management_menu.click()

    print("Navigating to Projects menu...")
    projects_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/a[@class="menu-link without-sub" and .//span[@class="menu-title" and normalize-space(text())="Projects"]]'))
    )
    projects_menu.click()

    print("Clicking the View button for a project...")
    view_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="badge badge-light-primary fw-bold me-auto px-4 py-3" and normalize-space(text())="View"]'))
    )
    view_button.click()

def click_filter_select(driver):
    print("Selecting filter 'Bit & Binary'...")
    filter_select_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/a[contains(text(),"Bit & Binary")]'))
    )
    filter_select_button.click()
    time.sleep(5)

def navigate_to_public_data(driver):
    print("Navigating to Public Data section...")
    public_data_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="publicdata"]'))
    )
    public_data_link.click()
    time.sleep(5)

def navigate_to_overview(driver):
    print("Navigating to Organization Overview...")
    organization_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Organization"]'))
    )
    organization_menu.click()

    print("Navigating to Overview page...")
    overview = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/span[@class="menu-title" and normalize-space(text())="Overview"]'))
    )
    overview.click()

    print("Clicking Edit Profile...")
    edit_profile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_profile_details_view"]/div[1]/a'))
    )
    edit_profile.click()

    print("Filling in description field...")
    description = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, './/textarea[@formcontrolname="description"]'))
    )
    description.send_keys("about work")

    print("Clicking checkboxes...")
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

    print("Clicking the Save button...")
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/button[@type="submit" and normalize-space(text())="Save"]'))
    )
    save_button.click()

def main():
    print("Starting the Selenium automation script...")
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
        print("Closing the browser...")
        driver.quit()

if __name__ == "__main__":
    main()
