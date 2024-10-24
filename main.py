from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome options
options = Options()

# Add the headless option
options.add_argument("--headless")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the webpage
driver.get("http://www.google.com")

# Close the browser window
driver.quit()
