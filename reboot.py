from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

# browser = webdriver.Chrome()
# chrome_options=Options()

# chrome_options.headless = True # also works
# driver = webdriver.Chrome(options=chrome_options)
options = webdriver.ChromeOptions()

options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


def website_open(url):
    driver.get(url)


def login_info(username, password):
    username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(
        By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input"
    )
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def rebooter():
    maintainence_field = driver.find_element(
        By.XPATH, '//*[@id="div_menu_left"]/ul[5]/li/a'
    )
    maintainence_field.click()
    reboot_device_field = driver.find_element(
        By.XPATH, '//*[@id="div_menu_left"]/ul[5]/li[5]'
    )
    reboot_device_field.click()
    driver.switch_to.frame(0)
    y = input("Do you want to reboot ? ")
    if y == "Y" or y == "y":
        do_reboot = driver.find_element(By.XPATH, '//*[@id="do_reboot"]')
        do_reboot.click()

        alert = Alert(driver)
        # accept the alert
        alert.accept()

        print("Done !")


def input_login():
    with open("login.txt", "r") as myfile:
        data = myfile.read().splitlines()
    return data


if __name__ == "__main__":
    data = input_login()
    website_open(data[0])
    login_info(data[1], data[2])
    rebooter()
