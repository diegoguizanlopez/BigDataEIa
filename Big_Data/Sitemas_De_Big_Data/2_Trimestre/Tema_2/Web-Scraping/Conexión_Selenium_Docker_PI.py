import time
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
command_executor='http://192.168.86.82:4444/wd/hub',
options=options
)

driver.get("https://www.browserstack.com/")
print(driver.current_url)
time.sleep(10)
driver.quit()