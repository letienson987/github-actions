from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import requests




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://gmail.



time.sleep(3)

# Total_Contract = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/span/span").text
# print(Total_Contract)
# elm= driver.find_element(By.XPATH,"//h5[contains(text(),'GLOBAL STATS')]")
# elm.click()


driver.quit()

