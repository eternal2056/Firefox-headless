#Firefox-headless
from selenium import webdriver
try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    browser = webdriver.Firefox(firefox_options=fireFoxOptions)

    browser.get('http://www.baidu.com')
    print(browser.page_source)
finally:
    try:
        browser.close()
    except:
        pass
