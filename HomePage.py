import unittest
from selenium import webdriver
import sys
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # create log to say if tests passed
        inst.logger = logging.getLogger()
        inst.logger.level = logging.DEBUG

        # create a driver instance
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

        # navigate to the application home page """
        inst.driver.get("http://www.google.com/")


    def test_algreen(self):
        """
        Watches al green videp
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

    # def test_search_box(self):
    #      # check search box exists on Home page
    #     self.assertTrue(self.is_element_present(By.NAME, "q"))
    #     self.driver.implicitly_wait(30)
    #     self.pass_log()
    #
    #     def test_language_settings(self):
    #         # check language options on Home page
    #         self.assertTrue(self.driver.find_element_by_link_text("Gmail"))
    #         self.driver.implicitly_wait(30)
    #         self.pass_log()
    #
    #     def test_images_link(self):
    #         # check images link on Home page
    #         images_link = self.driver.find_element_by_link_text("Images")
    #         images_link.click()
    #         # check search field exists on Images page
    #         self.assertTrue(self.is_element_present(By.NAME, "q"))
    #         self.driver.implicitly_wait(30)
    #         self.pass_log()
    #         self.search_field = self.driver.find_element_by_name("q")
    #         # enter search keyword and submit
    #         self.search_field.send_keys("Selenium Webdriver framework architecture diagram")
    #         self.search_field.submit()
    #
    #     def is_element_present(self, how, what):
    #         """
    #         Helper method to confirm the presence of an element on page
    #         :params how: By locator type
    #         :params what: locator value
    #         """
    #         try:
    #             self.driver.find_element(by=how, value=what)
    #         except NoSuchElementException:
    #             return False
    #         return True

    def pass_log(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(stream_handler)
        logging.getLogger().info("Passed")
        self.logger.removeHandler(stream_handler)

    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
