from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# __________________ create driver __________________

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# ______________ element cookie to be clicked on website ______________

cookie = driver.find_element(By.ID, "cookie")

# ________________ all items to buy list __________________

containers = driver.find_elements(By.CSS_SELECTOR, "#store div")
buy_list = [item.get_attribute("id") for item in containers[0:8]]
print(buy_list)

# _______________ buy most expensive item from buy list _______________

timeout = time.time() + 5
five_min_time = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        user_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        # print(user_money)

        try:
            price_list = []
            for id in buy_list:
                all_item_price = driver.find_element(By.ID, f"{id}").text.split("\n")[0].split("-")[-1].replace(",", "")
                price_int = int(all_item_price)
                price_list.append(price_int)

            # print(price_list)

            select_items = [price for price in price_list if price < user_money]
            maximum_price = select_items[-1]    # line not doing anything in here but it is here so that if we want to get highest valued item every time we can use this ..

            # print(maximum_price)

            if user_money > 50000 and price_list[5] < 100000:  # alchemy lab
                driver.find_element(By.ID, f"{buy_list[5]}").click()
            elif user_money > 7000 and price_list[4] < 10300:  # shipment
                driver.find_element(By.ID, f"{buy_list[4]}").click()
            elif user_money > 2000 and price_list[3] < 3000:  # mine
                driver.find_element(By.ID, f"{buy_list[3]}").click()
            elif user_money > 500 and price_list[2] < 750:  # factory
                driver.find_element(By.ID, f"{buy_list[2]}").click()
            elif user_money > 100 and price_list[1] < 160:  # grandma
                driver.find_element(By.ID, f"{buy_list[1]}").click()
            else:
                # print("not selecting")
                pass
        except:
            print("can't find")

        timeout = time.time() + 5
        # print(timeout)

    if time.time() > five_min_time:
        cookie_per_second = driver.find_element(By.ID, "cps").text
        print(cookie_per_second)
        break

# driver.quit()