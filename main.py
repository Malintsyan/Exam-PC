import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from setUp import SetUp
from login import Login
from hotel import Hotel
from yerevan import Yerevan
# from  details import Details
from  selectRum import SelectRoom
from  fill import Fill

class Exam(unittest.TestCase):
    def setUp(self):
        print('Start')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_sign(self):
        self.driver.get('https://www.phptravels.net/signup')
        url1 = self.driver.current_url
        self.driver.find_element(By.XPATH, SetUp.first_Name).send_keys('Hermine')
        sleep(1)
        self.driver.find_element(By.XPATH, SetUp.last_Name).send_keys('Malintsyan')
        sleep(1)
        self.driver.find_element(By.XPATH, SetUp.phon).send_keys('094123456')
        sleep(1)
        self.driver.find_element(By.XPATH, SetUp.mail).send_keys('hermine.malintsyan@gmail.com')
        sleep(1)
        self.driver.find_element(By.XPATH, SetUp.passW).send_keys('Malintsyan')
        sleep(1)
        self.driver.find_element(By.XPATH, SetUp.login).click()
        sleep(1)
        self.driver.find_element(By.XPATH, Login.mail).send_keys('hermine.malintsyan@gmail.com')
        sleep(1)
        self.driver.find_element(By.XPATH, Login.passW).send_keys('Malintsyan')
        sleep(1)
        self.driver.find_element(By.XPATH, Login.login1).click()
        sleep(1)
        self.driver.find_element(By.XPATH, Hotel.choice).click()
        sleep(1)
        self.driver.find_element(By.XPATH, Yerevan.search).click()
        sleep(1)
        self.driver.find_element(By.XPATH, Yerevan.esearch).send_keys('Yerevan')
        sleep(1)
        self.driver.find_element(By.XPATH, Yerevan.vsearch).click()
        sleep(1)
        self.driver.find_element(By.XPATH, Yerevan.cleck).click()
        sleep(1)
        self.driver.get(SelectRoom.url)
        sleep(1)
        sleep(1)
        self.driver.get(SelectRoom.url)
        sleep(2)
        self.driver.find_element(By.XPATH, SelectRoom.view).click()
        sleep(2)
        self.driver.find_element(By.XPATH, Fill.name).send_keys('Malintsyan Hermine')
        sleep(1)
        self.driver.find_element(By.XPATH, Fill.mail).send_keys('hermine.malintsyan@gmail.com')
        sleep(1)
        self.driver.find_element(By.XPATH, Fill.remail).send_keys('hermine.malintsyan@gmail.com')
        sleep(1)
        self.driver.find_element(By.XPATH, Fill.phone).send_keys('094015114')
        sleep(1)
        self.driver.find_element(By.XPATH, Fill.final).click()
        sleep(1)
        check = 0
        if self.driver.current_url:
            check += 1

        self.assertEqual(1,check)

    def tearDown(self):
        print("end")
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
