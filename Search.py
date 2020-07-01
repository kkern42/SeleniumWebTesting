
import unittest
from selenium import webdriver
import sys
import logging
import time
from nose.tools import assert_equal




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
            inst.driver.get("http://www.google.com/")
            inst.driver.title
    def test_algreen(self):
        """
        Will go to youtube login into my account and subscribe to the channel
        :return:
        """
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # clears the texbox
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("Al Green Simply Beautiful")
        self.search_field.submit()

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