import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://app.tryloop.ai/login/password')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq']").send_keys("qa-engineer-assignment@test.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']").send_keys("QApassword123$")
time.sleep(4)
driver.find_element(By.XPATH, "//button[@data-testid='login-button']").click()
time.sleep(8)
driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-18euqpt' and text()='3P Chargebacks']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-18euqpt' and text()='Transactions']").click()
time.sleep(10)
driver.find_element(By.XPATH, "//button[@data-testid='selectBtn']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeLarge MuiButton-textSizeLarge MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeLarge MuiButton-textSizeLarge css-vqrxrl-MuiButtonBase-root-MuiButton-root']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//p[text()='Artisan Alchemy']/preceding-sibling::span/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "//p[text()='Blissful Buffet']/preceding-sibling::span/input").click()
time.sleep(3)
button = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1p58fjm-MuiButtonBase-root-MuiIconButton-root']")))
# Click the button
button.click()