import time
from selenium import webdriver
import xlrd 


chromedriver = 'D:/python/VSCode/projects/chromedriver'
# self.driver = webdriver.Chrome(chromedriver)

# self.driver.get("https://contacts.google.com/")
class Google:

    def __init__(self,username,password):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get('https://stackoverflow.com/users/login')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(5)
        try:
        # opening contacts
            self.driver.get("https://contacts.google.com/")
            time.sleep(5)
            for i in range(1,sn):

                name = sheet.cell_value(i, 2)
                number =  str(int(sheet.cell_value(i, 3)))
                # selecting create contact button
                self.driver.find_element_by_xpath("/html/body/div[7]/div[2]/header/div[4]/div[2]/div/c-wiz/div/div[1]/div/div/div/button").click()
                time.sleep(2)
                # selecting creating contacts
                self.driver.find_element_by_xpath("/html/body/div[7]/div[2]/header/div[4]/div[2]/div/c-wiz/div[2]/div/div/span[1]").click()
                time.sleep(1)

                # selecting name input field
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input").click()
                # entering name
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input").send_keys(name)
                
                # selecting last-name input field
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/input").click()
                # entering last-name
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/input").send_keys('Debater')
                
                # selcting number input field
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input").click()
                # entering number
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(number)
                time.sleep(1)

                # selecting save button
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[3]/div/button[2]/span").click()
                time.sleep(3)
                # selecting cross(x) button
                self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[1]/div/div[3]/div[4]").click()

                # # for deleting saved contacts
                # #selecting 3 dots
                # self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div/div[1]/div/div[3]/div[3]").click()
                # time.sleep(1)
                # #selecting delete buton
                # self.driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div[2]/span/div[2]/div/div/div/span[4]/span/div[3]/div").click()
                # time.sleep(1)
                # #confirmed delete
                # self.driver.find_element_by_xpath("/html/body/div[7]/div[5]/div/div[2]/div[3]/div/button[2]/span").click()
                # time.sleep(2)


            time.sleep(5)
        except Exception as e:
            # f = open("error.log", "a")
            # print("Error Occured.\n Check the error.log file")
            # f.write(str(e))
            # f.close()
            print(str(e))
        finally:
            self.driver.close()

name = ''
number = ''

wb = xlrd.open_workbook("D:\python\VSCode\projects\participants.xlsx") 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
sn = sheet.nrows   
password='debsoc123'   
username='debatingsociety.nitdgp@gmail.com'
mylike= Google(username,password)