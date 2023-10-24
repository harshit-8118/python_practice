from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--disabled-cookies')
chrome_options.add_experimental_option("detach", True)
svc = webdriver.ChromeService(executable_path=binary_path)
browser = webdriver.Chrome(service=svc)

browser.get("http://www.codechef.org")
login = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'm-login-button-no-border'))
)
login.click()
# browser.find_element(By.CLASS_NAME, value='m-login-button-no-border')

username = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/section/div[2]/div/div[3]/div[2]/form/div/div[1]/div/div/input'))
)
username.send_keys('hharshit8118@gmail.com')

password = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/section/div[2]/div/div[3]/div[2]/form/div/div[2]/div/div[2]/input'))
)
password.send_keys('Harshit@8118')

submit = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/section/div[2]/div/div[3]/div[2]/form/div/div[3]/input'))
)
submit.click()
browser.get('https://www.codechef.com/problems/TEST')

with open('sol.cpp', 'r') as f:
    code = f.read()

textarea = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[2]/textarea'))
)

textarea.send_keys(code)

submitcode = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/div[2]/div[3]/div[2]/div[2]/div/button[2]'))
)
submitcode.click()

while True:
    pass
