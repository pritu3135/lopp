import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
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
driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-18euqpt' and text()='History by Store']").click()
time.sleep(5)
driver.close()
