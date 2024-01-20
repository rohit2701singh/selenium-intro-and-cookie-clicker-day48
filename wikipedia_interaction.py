from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
# search.send_keys("python", Keys.ENTER)

search.send_keys("anaconda", Keys.SPACE)
# search.clear()
search.send_keys("python", Keys.ENTER)

# ______________challenge fill sign up form_______________

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("rohit")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("singh")

email = driver.find_element(By.NAME, "email")
email.send_keys("singh@gmail.com")

submit = driver.find_element(By.CLASS_NAME, "btn-primary")
# submit.click()
WebDriverWait(driver, 5)
submit.submit()
