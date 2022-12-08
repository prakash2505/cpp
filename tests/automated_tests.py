from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from cpplibrary1234 import cpplibrary1234  #custom library import

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("http://0.0.0.0:8000/")
headerText = driver.find_element(By.CLASS_NAME, "navbar-brand").text

print("verify if header text is correct : " + str(cpplibrary1234.verifyText(headerText,'School Management')))

