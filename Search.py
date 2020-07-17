import pandas as pd
import unittest
from selenium import webdriver
import sys
import logging
import time
from nose.tools import assert_equal

users = pd.read_excel('./Breed List.xlsx')


class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
            # create a new Firefox session
            inst.logger = logging.getLogger()
            inst.logger.level = logging.DEBUG
            inst.driver = webdriver.Chrome()
            inst.driver.implicitly_wait(30)
            inst.driver.maximize_window()
            # navigate to the application home page
            inst.driver.get("https://www.mytime.com/users/sign_in")
            inst.driver.title

    def test_mytime(self):
        """

        :return:
        """
        print(users)
        self.search_field = self.driver.find_element_by_xpath('//*[@id="user_login"]')
        self.search_field.send_keys("tim@scenthound.com")
        self.search_field = self.driver.find_element_by_xpath('//*[@id="user_password"]')
        self.search_field.send_keys("Vogel1234")
        self.driver.find_element_by_xpath('//*[@id="sign_in_form"]/div[7]/button').click()
        self.driver.find_element_by_xpath('// *[ @ id = "mytime_nav_bar"] / div / ul / li[3] / a').click()
        # this line closes the text box that shows new feature don't know why it's no longer showing up
        # self.driver.find_element_by_xpath('/ html / body / div[8] / div / div / div / div / div[1] / a').click()

        self.driver.find_element_by_xpath('//*[@id="ng-app"]/div[5]/div/div/div/div/div[2]/my-child-table/div/table/tbody[3]/tr/td[5]/ul/li[3]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="merchant-filter"]/ul/li/div[1]/a').click()
        self.driver.find_element_by_xpath('// *[ @ id = "merchant-filter"] / ul / li / div[2] / p[4] / a').click()
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/div[3]/div/div/div[3]/a').click()
        # self.driver.find_element_by_xpath().click()
        button = self.driver.find_element_by_xpath('//*[@id="variation42789067"]/div/div[4]/div/a[2]')
        self.driver.execute_script("arguments[0].click();", button)
        button = self.driver.find_element_by_xpath('// *[ @ id = "variation42789067"] / div[2] / div / div[8] / div[3] / a')
        self.driver.execute_script("arguments[0].click();", button)
        self.search_field = self.driver.find_element_by_xpath('/ html / body / div[8] / div / div / div / div / div / div[2] / div[1] / div[2] / div / div / div / input')
        self.search_field.send_keys("tim@scenthound.com")
        time.sleep(100)

        # goes to the vidoes tab on google
        self.driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()

        # clicks on the third link
        self.driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[3]/div/div/div[1]/a').click()

        # goes to the sign in button
        self.driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer').click()

        # clicks on the username and password types them both in to log into my account
        self.search_field = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        self.search_field.send_keys("kevkern3@gmail.com")
        self.driver.find_element_by_xpath('// *[ @ id = "identifierNext"]').click()
        self.search_field = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        self.search_field.send_keys("Teamdoritos4")
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()

        self.driver.find_element_by_xpath('// *[ @ id = "movie_player"] / div[21] / div[1] / div[1] / div[1]').click()

        # clicks the subsrcibe button
        # self.driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()
        time.sleep(100)
        self.pass_log()




    # def test_asearch_by_name(self):
    #         # get the search textbox
    #         self.search_field = self.driver.find_element_by_name("q")
    #         # enter search keyword and submit
    #         self.search_field.send_keys("Python class")
    #         self.search_field.submit()
    #         #get the list of elements which are displayed after the search
    #         #currently on result page using find_elements_by_class_name method
    #         list_new = self.driver.find_elements_by_class_name("r")
    #         assert_equal(13, len(list_new))
    #         self.driver.implicitly_wait(30)
    #         self.pass_log()

    def pass_log(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(stream_handler)
        logging.getLogger().info("Passed")
        self.logger.removeHandler(stream_handler)


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()





 # def test_aasearch(self):
    #
    #     # get the search textbox
    #     self.search_field = self.driver.find_element_by_name("q")
    #
    #     # clears the texbox
    #     self.search_field.clear()
    #
    #     # enter search keyword and submit
    #     self.search_field.send_keys("sound cloud")
    #     self.search_field.submit()
    #
    #     # goes to the vidoes tab on google
    #     self.driver.find_element_by_xpath('// *[ @ id = "rso"] / div[1] / div / div / div / div / div[1] / a').click()
    #
    #     # clicks on the third link
    #     self.driver.find_element_by_xpath('// *[ @ id = "content"] / div / div / div[1] / div / div / div[3] / button[1]').click()
    #
    #     self.driver.find_element_by_xpath('//*[@id="overlay_276"]/div/div/form/div/div[1]/div/div[1]/div[1]/div[3]').click()
    #     # self.search_field = self.driver.find_element_by_xpath('//*[@id="formControl_277"]')
    #     # self.search_field.send_keys("kevkern3@gmail.com")
    #
    #
    #
    #     # self.driver.find_element_by_xpath('// *[ @ id = "overlay_272"] / div / div / form / div / div[1] / div / button').click()
    #
    #     # self.search_field = self.driver.find_element_by_xpath('//*[@id="formControl_289"]')
    #     # self.search_field.send_keys("hihihi")
    #
    #     # self.driver.find_element_by_xpath('// *[ @ id = "overlay_272"] / div / div / form / div / div[2] / div / button').click()
    #
    #
    #     # self.driver.get('https://soundcloud.com/')
    #     # self.driver.navigate().refresh()