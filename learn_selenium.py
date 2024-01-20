import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

# -------- select using class_name ----------

some_text = driver.find_element(By.CLASS_NAME, value="widget-title").text
print(some_text)    # Get Started

# -------------select using name-------------

search_bar = driver.find_element(By.NAME, value="q")

print(search_bar.tag_name)  # input
print(search_bar.get_attribute("role"))   # textbox

# ______________select by id___________

button = driver.find_element(By.ID, value="submit")

print(button.text)      # GO
print(button.size)      # {'height': 40, 'width': 46}
print(button.get_attribute("title"))    # Submit this Search
print(button.tag_name)     # button

# __________ select by css selector__________

image = driver.find_element(By.CSS_SELECTOR, value=".container img")

print(image.tag_name)   # img
print(image.get_attribute("src"))   # https://www.python.org/static/img/python-logo@2x.png
print(image.get_attribute("class"))     # python-logo
print(image.accessible_name)    # python™
print(image.size)   # {'height': 82, 'width': 290}

# __________ search by xpath_________

time.sleep(5)
django = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[4]/div[2]/div/ul/li[1]/span/a[1]')
time.sleep(3)
print(django.text)  # Django
print(django.size)  # {'height': 20, 'width': 49}
print(django.tag_name)  # a
print(django.get_attribute("href"))  # http://www.djangoproject.com/

driver.quit()