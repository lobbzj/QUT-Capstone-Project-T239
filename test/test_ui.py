from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_home_ui():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000")
    assert "Testing in progress" in driver.page_source
    driver.quit()
