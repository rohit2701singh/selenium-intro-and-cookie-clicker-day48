from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

get_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
time_list = [time.text for time in get_time]
print(time_list)


event_div = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_list = [event.text for event in event_div]
print(event_list)

dict_data = {i: {"time": time_list[i], "name": event_list[i]} for i in range(len(time_list))}
print(dict_data)
driver.quit()

'''
output: 
{0: {'time': '2024-01-24', 'name': 'IndyPy: "Advanced Models & AI... For Dummies”'}, 1: {'time': 
'2024-01-25', 'name': 'PyLadies Amsterdam: An introduction to conformal prediction'}, 2: {'time': '2024-02-04', 
'name': 'Python Devroom @ FOSDEM 2024'}, 3: {'time': '2024-02-04', 'name': 'FOSDEM 2024: Python Devroom'}, 
4: {'time': '2024-02-24', 'name': 'Django Girls Ho'}}
'''