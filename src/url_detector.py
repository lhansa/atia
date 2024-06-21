from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import platform

class URLDetector:
    def __init__(self, chrome_driver_path='/usr/local/bin/chromedriver', firefox_driver_path='/usr/bin/geckodriver'):
        self.system = platform.system()
        self.driver = None
        self.chrome_driver_path = chrome_driver_path
        self.firefox_driver_path = firefox_driver_path

    def _setup_chrome_driver(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_service = ChromeService(executable_path="/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def _setup_firefox_driver(self):
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_service = FirefoxService(executable_path="/usr/bin/geckodriver")
        self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    def get_active_tab_url(self, browser="chrome"):
        if browser == "chrome":
            if not self.driver:
                self._setup_chrome_driver()
        elif browser == "firefox":
            if not self.driver:
                self._setup_firefox_driver()
        else:
            raise ValueError("Unsupported browser: only 'chrome' and 'firefox' are supported")

        self.driver.get("http://localhost:9222/json")
        tabs = self.driver.find_elements(By.CSS_SELECTOR, "body > pre")
        active_tab_url = None
        if tabs:
            for tab in tabs:
                if "active" in tab.text:
                    active_tab_url = tab.get_attribute("url")
                    break
        return active_tab_url

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

