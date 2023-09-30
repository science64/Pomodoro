from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import graph_chrome_correctly
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'/files/chromedriver.exe')
options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-gpu')
options.add_argument('--disable-setuid-sandbox')
options.add_argument("--start-maximized")
options.add_extension('ublock.crx')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("detach", True) # this prevent closing when it is complete!
options.add_experimental_option('prefs', {
    'credentials_enable_service': True,
    'profile': {
        'password_manager_enabled': True
    }
})

try:
    driver = webdriver.Chrome(options=options)

except Exception as e:
    print(e)
    graph_chrome_correctly.download_chromedriver('').download()
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(e)
        print('Error in chromedriver.')
        exit(1)

try:
    driver.get('https://asoftmurmur.com/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="App"]/div[3]/button[2]/div')))
    # driver.find_element_by_xpath('').click()
    driver.find_elements(By.XPATH, '//*[@id="App"]/div[3]/button[2]/div')[0].click()

    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])

    driver.get('https://rainymood.com/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pButton"]')))
    driver.find_elements(By.XPATH, '//*[@id="pButton"]')[0].click()

    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://soundcloud.com/relaxdaily/sets/deep-focus-music-studying-concentration-work')

    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[3])
    driver.get('https://nesto.cc/')
except Exception as e:
    print(f'error: {e}')





