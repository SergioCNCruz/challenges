"""Simple web scraper using Selenium to fetch page titles."""
from __future__ import annotations

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://selenium:4444/wd/hub")


def fetch_title(url: str) -> str:
    """Return the title of the given URL using a headless browser."""
    options = Options()
    options.add_argument("--headless")
    with webdriver.Remote(command_executor=SELENIUM_REMOTE_URL, options=options) as driver:
        driver.get(url)
        return driver.title
