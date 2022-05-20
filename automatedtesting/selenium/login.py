# #!/usr/bin/env python
#from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime


def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')

# Start the browser and login with standard_user
def login (driver,user, password):
    print (timestamp()+'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    time.sleep(10)
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_heading=driver.find_element_by_class_name("title").text
    assert "PRODUCTS" in product_heading
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))


def add_items_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element_by_css_selector(element).click()  
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()  
        product = driver.find_element_by_css_selector("div[class='inventory_details_name large_size']").text  
        print(timestamp() + product + " added to shopping cart.")  
        driver.find_element_by_id("back-to-products").click()  
    print(timestamp() + '{:d} items are all added to shopping cart successfully.'.format(n_items))

def remove_items(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element_by_css_selector(element).click()  
        driver.find_element_by_css_selector("button.btn_small.btn_inventory").click() 
        product = driver.find_element_by_css_selector("div[class='inventory_details_name large_size']").text  
        print(timestamp() + product + " removed from shopping cart.") 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()  
    print(timestamp() + '{:d} items are all removed from shopping cart successfully.'.format(n_items))


if __name__ == "__main__":
    print (timestamp() + 'Starting the browser...')
    num_items=6
    # --uncomment when running in Azure DevOps.
    options = Options()
    # options.binary_location = ""    #chrome binary location specified here
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox") #bypass OS security model
    options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    # driver.get('http://google.com/')
    # chromeOptions.add_argument(r"user-data-dir=.\cookies\\test") 
    # options.add_experimental_option("useAutomationExtension", false)
    driver = webdriver.Chrome(options=options)
# driver=webdriver.Chrome()
    login(driver,'standard_user', 'secret_sauce')
    add_items_cart(driver,num_items)
    remove_items(driver,num_items)
    print(timestamp() + 'Selenium tests are all successfully completed!')
    driver.quit()
    


