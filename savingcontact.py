import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

profile = webdriver.FirefoxProfile('C:\\Users\\Bhavy\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\e44c19vs.default-1566071678818')
driver = webdriver.Firefox(executable_path='./geckodriver.exe',
                               firefox_profile=profile)

name = 'test'
number = "+91 87654 76595"
try:
    # opening contacts
    driver.get("https://contacts.google.com/")
    for _ in range(3):
        # selecting create contact button
        driver.find_element_by_xpath("/html/body/div[7]/div[2]/header/div[4]/div[2]/div/c-wiz/div/div[1]/div/div/button").click()
        time.sleep(2)
        # selecting name input field
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input").click()
        # entering name
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input").send_keys(name)
        # selcting number input field
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input").click()
        # entering number
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(number)
        time.sleep(0.5)
        # selecting save button
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[3]/div/button[2]/span").click()
        time.sleep(1)
        # selecting cross(x) button
        # # driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[1]/div/div[3]/div[4]").click()
        # for deleting saved contacts
        #selecting 3 dots
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[1]/div/div[3]/div[3]").click()
        time.sleep(0.5)
        #selecting delete buton
        driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div[2]/div/div/div/span[4]/span/div[3]/div").click()
        time.sleep(0.5)
        #confirmed delete
        driver.find_element_by_xpath("/html/body/div[7]/div[5]/div/div[2]/div[3]/div/button[2]/span").click()
        time.sleep(1.5)



    driver.find_element_by_css_selector
    time.sleep(5)
except Exception as e:
    # f = open("error.log", "a")
    # print("Error Occured.\n Check the error.log file")
    # f.write(str(e))
    # f.close()
    print(str(e))
finally:
    driver.close()