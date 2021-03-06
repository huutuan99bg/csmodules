import subprocess
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from csmodules.cswait import SWait


def open_driver(chrome_profile,binary_location = None,images = True, headless = False, chrome_agrs = None):
    driver_path = 'E:/tools/webdriver/chromedriver.exe'
    options = Options()
    img_option = 1 if images == True else 2
    prefs = {"profile.managed_default_content_settings.images": img_option}
    options.add_experimental_option("prefs", prefs)
    if headless == True:
        options.add_argument('--headless')
    if binary_location != None:
        options.binary_location = binary_location
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")
    if chrome_agrs != None:
        options.add_argument(chrome_agrs)
    options.add_argument("user-data-dir="+chrome_profile)
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.implicitly_wait(5)
    cswait = SWait(driver)
    return (driver,cswait)

def open_driver_wire(chrome_profile,binary_location = None,images = True, headless = False, chrome_agrs = None):
    driver_path = 'E:/tools/webdriver/chromedriver.exe'
    options = Options()
    img_option = 1 if images == True else 2
    prefs = {"profile.managed_default_content_settings.images": img_option}
    options.add_experimental_option("prefs", prefs)
    if headless == True:
        options.add_argument('--headless')
    if binary_location != None:
        options.binary_location = binary_location
    if chrome_agrs != None:
        options.add_argument(chrome_agrs)
    options.add_argument("user-data-dir="+chrome_profile)
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    driver = webdriver.Chrome(desired_capabilities=capabilities,executable_path=driver_path, options=options)
    driver.implicitly_wait(5)
    cswait = SWait(driver)
    return (driver,cswait)

def clear_cookies(driver):
    # Clear cookie
    try:
        cswait = SWait(driver)
        driver.get("https://api.binance.com")
        btn_clear = cswait.get_element_by_xpath(5,'//img[@class="inserted-btn mtz"]')
        sleep(.5)
        btn_clear.click()
        sleep(.5)
    except:
        pass
def kill_chrome():
    subprocess.call("TASKKILL /f /im chrome.exe")
