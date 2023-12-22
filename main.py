from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


# testing
website1 = 'https://www.allticket.com/event/2024ROWOONFANMEETING'
website2 = 'https://www.allticket.com/event/Nova75Countdown'

target_website = ''
key_auth = 'ALLTICKET:authToken'
auth_token = ''

cookie = '/html/body/div[2]/div/a[2]'
buy_now = '/html/body/app-root/app-event-info/div/div[2]/div[2]/div/div[5]/div/button'
check_condition = '/html/body/app-root/app-consent-buy/div/div[2]/div/div/label/span'
confirm_next = '/html/body/app-root/app-consent-buy/div/div[3]/div/button[1]'
pick_date = '/html/body/app-root/app-booking/div[3]/div[1]/div[2]/div/label'
check_seat = '/html/body/app-root/app-booking/div[3]/div[2]/app-get-seat-available/div[1]/button'
select_zone = '/html/body/app-root/app-booking/div[3]/div[2]/app-get-seat-available/div[1]/div/div[2]/div/div[3]/div[1]'

target = webdriver.Chrome()
target.get(target_website)

target.execute_script(f"localStorage.removeItem('{key_auth}')")
target.execute_script(f"localStorage.setItem('{key_auth}', '{auth_token}')")

cookie_wait =  EC.presence_of_element_located((By.XPATH, cookie))
time.sleep(2)
close_button = WebDriverWait(target, 10).until(cookie_wait)
close_button.click()
time.sleep(1)

buy_wait = EC.presence_of_element_located((By.XPATH, buy_now))
buy_now_button = WebDriverWait(target, 10).until(buy_wait)
buy_now_button.click()
time.sleep(2)

target.execute_script("window.scrollTo(0, document.body.scrollHeight)")

check_wait = EC.presence_of_element_located((By.XPATH, check_condition))
checkbox = WebDriverWait(target, 10).until(check_wait)
checkbox.click()
confirm_wait = EC.presence_of_element_located((By.XPATH, confirm_next))
confirm_button = WebDriverWait(target, 10).until(confirm_wait)
confirm_button.click()
time.sleep(2)

date_wait = EC.presence_of_element_located((By.XPATH, pick_date))
date_button = WebDriverWait(target, 10).until(date_wait)
date_button.click()
time.sleep(10)


# seat_wait = EC.presence_of_element_located((By.XPATH, check_seat))
# seat_button = WebDriverWait(target, 10).until(seat_wait)
# seat_button.click()

# zone_wait = EC.presence_of_element_located((By.XPATH, select_zone))
# time.sleep(5)
# zone_button = WebDriverWait(target, 10).until(zone_wait)
# zone_button.click()
# time.sleep(10)

# 1 /html/body/app-root/app-booking/div[3]/div[1]/div[2]/div/label
# 2 /html/body/app-root/app-booking/div[3]/div[1]/div[2]/div/label

target.quit()