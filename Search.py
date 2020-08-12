import pandas as pd
import unittest
from selenium import webdriver
import sys
import logging
import time
from selenium.webdriver.common.action_chains import ActionChains
from nose.tools import assert_equal
from selenium.webdriver.common.keys import Keys

special = pd.read_excel('./Breed List.xlsx', 'Special')
one = pd.read_excel('./Breed List.xlsx', '1')
two = pd.read_excel('./Breed List.xlsx', '2')
three = pd.read_excel('./Breed List.xlsx', '3')

tables = [one, two, three, special]


class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.logger = logging.getLogger()
        inst.logger.level = logging.DEBUG
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("https://www.mytime.com/users/sign_in")
        inst.driver.title
        # print(list(breeds))
        inst.search_field = inst.driver.find_element_by_xpath('//*[@id="user_login"]')
        time.sleep(.25)
        inst.search_field.send_keys("tim@scenthound.com")
        time.sleep(.25)
        inst.search_field = inst.driver.find_element_by_xpath('//*[@id="user_password"]')
        time.sleep(.25)
        inst.search_field.send_keys("Vogel1234")
        time.sleep(.25)

        # sign in button press
        inst.driver.find_element_by_xpath('//*[@id="sign_in_form"]/div[7]/button').click()
        time.sleep(.25)

        # clicks location management
        inst.driver.find_element_by_xpath('// *[ @ id = "mytime_nav_bar"] / div / ul / li[3] / a').click()
        time.sleep(.25)

        # this line closes the text box that shows new feature don't know why it's no longer showing up
        # self.driver.find_element_by_xpath('/ html / body / div[8] / div / div / div / div / div[1] / a').click()

        # clicks admin on the test2 location
        inst.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/div[5]/div/div/div/div/div[2]/my-child-table/div/table/tbody[2]/tr/td[5]/ul/li[3]/a').click()
        time.sleep(5)

        # clicks drop down for test 2
        inst.driver.find_element_by_xpath('//*[@id="merchant-filter"]/ul/li/div[1]/a').click()
        time.sleep(.25)

        # clicks on buisness set up from that drop down
        inst.driver.find_element_by_xpath('// *[ @ id = "merchant-filter"] / ul / li / div[2] / p[4] / a').click()
        time.sleep(.25)

        # clicks on services
        inst.driver.find_element_by_xpath('//*[@id="ng-app"]/div[3]/div/div/div[3]/a').click()
        time.sleep(.25)

        # edit button to the left of service card
        button = inst.driver.find_element_by_xpath(
            '// *[ @ id = "ng-app"] / div[7] / div / div / div / div / div / div / div / div[1] / div / div / button')
        inst.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)

        # path for drop down location
        button = inst.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/div[7]/div/div/div/div/div/div/div/div[1]/div/div/ul/my-mt-location-search-select/div/span/div/div/div[2]/span/ul/li[2]')
        inst.driver.execute_script("arguments[0].click();", button)

        time.sleep(10)

    def test_faceTrim(self):
        """
        add dog breeds to services in mytime
        :return: void
        """

        time.sleep(2)

        # clicks edit button for blow
        button = self.driver.find_element_by_xpath(
            '//*[@id="variation43618954"]/div/div[4]/div/a')
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(.25)

        for table in tables:
            time.sleep(2)
            # add new button on pop up
            button = self.driver.find_element_by_xpath(
                '//*[@id="variation43618954"]/div[2]/div/div[7]/div[3]/a')
            self.driver.execute_script("arguments[0].click();", button)

            time.sleep(.5)
            # breed input field
            self.search_field = self.driver.find_element_by_xpath(
                '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
            time.sleep(2)
            for index, row in table.iterrows():
                print(row.Breed)
                # this clicks addnew i think
                self.search_field.send_keys(str(row.Breed))
                time.sleep(.5)
                # clicks on the right one
                self.search_field.send_keys(Keys.DOWN + Keys.ENTER)

            time.sleep(.5)
            # fills out time
            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
            self.search_field.send_keys("10")

            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
            self.search_field.send_keys("10")

            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
            self.search_field.send_keys("10")

            time.sleep(.5)
            # saves new thing
            button = self.driver.find_element_by_xpath(
                '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
            self.driver.execute_script("arguments[0].click();", button)

        # presses save button for everyhting
        button = self.driver.find_element_by_xpath(
            '//*[@id="variation43618954"]/div[2]/div/div[8]/div[2]/input')
        self.driver.execute_script("arguments[0].click();", button)
        self.pass_log()

    def test_sanitaryTrim(self):
        """
        add dog breeds to services in mytime
        :return: void
        """

        time.sleep(2)

        # clicks edit button for blow
        button = self.driver.find_element_by_xpath(
            '//*[@id="variation43619006"]/div/div[4]/div/a')
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(.25)

        for table in tables:
            time.sleep(2)
            # add new button on pop up
            button = self.driver.find_element_by_xpath(
                '//*[@id="variation43619006"]/div[2]/div/div[7]/div[3]/a')
            self.driver.execute_script("arguments[0].click();", button)

            time.sleep(.5)
            # breed input field
            self.search_field = self.driver.find_element_by_xpath(
                '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
            time.sleep(2)
            for index, row in table.iterrows():
                print(row.Breed)
                # this clicks addnew i think
                self.search_field.send_keys(str(row.Breed))
                time.sleep(.5)
                # clicks on the right one
                self.search_field.send_keys(Keys.DOWN + Keys.ENTER)

            time.sleep(.5)
            # fills out time
            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
            self.search_field.send_keys("10")

            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
            self.search_field.send_keys("10")

            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
            self.search_field.send_keys("10")

            time.sleep(.5)
            # saves new thing
            button = self.driver.find_element_by_xpath(
                '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
            self.driver.execute_script("arguments[0].click();", button)

        # presses save button for everyhting
        button = self.driver.find_element_by_xpath(
            '//*[@id="variation43619006"]/div[2]/div/div[8]/div[2]/input')
        self.driver.execute_script("arguments[0].click();", button)
        self.pass_log()

    def test_padTrim(self):
        """
        add dog breeds to services in mytime
        :return: void
        """

        time.sleep(2)

        # clicks edit button for blow
        button = self.driver.find_element_by_xpath(
            '//*[@id="variation43619049"]/div/div[4]/div/a')
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(.25)

        for table in tables:
            time.sleep(2)
            # add new button on pop up
            button = self.driver.find_element_by_xpath(
                '//*[@id="variation43619049"]/div[2]/div/div[7]/div[3]/a')
            self.driver.execute_script("arguments[0].click();", button)

            time.sleep(.5)
            # breed input field
            self.search_field = self.driver.find_element_by_xpath(
                '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
            time.sleep(2)
            for index, row in table.iterrows():
                print(row.Breed)
                # this clicks addnew i think
                self.search_field.send_keys(str(row.Breed))
                time.sleep(.5)
                # clicks on the right one
                self.search_field.send_keys(Keys.DOWN + Keys.ENTER)

            time.sleep(.5)
            # fills out time
            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
            self.search_field.send_keys("10")

            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
            self.search_field.send_keys("10")

            self.search_field = self.driver.find_element_by_xpath(
                '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
            self.search_field.send_keys("10")

            time.sleep(.5)
            # saves new thing
            button = self.driver.find_element_by_xpath(
                '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
            self.driver.execute_script("arguments[0].click();", button)

        # presses save button for everyhting
        button = self.driver.find_element_by_xpath(
            '//*[@id="variation43619049"]/div[2]/div/div[8]/div[2]/input')
        self.driver.execute_script("arguments[0].click();", button)
        self.pass_log()

    # def test_barber(self):
    #     """
    #     add dog breeds to services in mytime
    #     :return: void
    #     """
    #
    #     time.sleep(2)
    #
    #     # clicks edit button for blow
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41487597"]/div/div[4]/div/a')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     time.sleep(.25)
    #
    #     for table in tables:
    #         time.sleep(2)
    #         # add new button on pop up
    #         button = self.driver.find_element_by_xpath(
    #             '//*[@id="variation41487597"]/div[2]/div/div[8]/div[3]/a')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #         time.sleep(.5)
    #         # breed input field
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
    #         time.sleep(2)
    #         for index, row in table.iterrows():
    #             print(row.Breed)
    #             # this clicks addnew i think
    #             self.search_field.send_keys(str(row.Breed))
    #             time.sleep(.5)
    #             # clicks on the right one
    #             self.search_field.send_keys(Keys.DOWN + Keys.ENTER)
    #
    #         time.sleep(.5)
    #         # fills out time
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         time.sleep(.5)
    #         # saves new thing
    #         button = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #     # presses save button for everyhting
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41487597"]/div[2]/div/div[9]/div[2]/input')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     self.pass_log()
    #
    # def test_blowOut(self):
    #     """
    #     add dog breeds to services in mytime
    #     :return: void
    #     """
    #
    #     time.sleep(2)
    #
    #     # clicks edit button for blow
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41490194"]/div/div[4]/div/a')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     time.sleep(.25)
    #
    #     for table in tables:
    #         time.sleep(.5)
    #         # add new button on pop up
    #         button = self.driver.find_element_by_xpath(
    #             '//*[@id="variation41490194"]/div[2]/div/div[8]/div[3]/a')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #         time.sleep(.5)
    #         # breed input field
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
    #         time.sleep(2)
    #         for index, row in table.iterrows():
    #             print(row.Breed)
    #             # this clicks addnew i think
    #             self.search_field.send_keys(str(row.Breed))
    #             time.sleep(.5)
    #             # clicks on the right one
    #             self.search_field.send_keys(Keys.DOWN + Keys.ENTER)
    #
    #         time.sleep(.5)
    #         # fills out time
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         time.sleep(.5)
    #         # saves new thing
    #         button = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #     # presses save button for everyhting
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41490194"]/div[2]/div/div[9]/div[2]/input')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     self.pass_log()
    #
    # def test_essentialBarb(self):
    #     """
    #     add dog breeds to services in mytime
    #     :return: void
    #     """
    #
    #     time.sleep(2)
    #
    #     # clicks edit button for barber
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41490270"]/div/div[4]/div/a')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     time.sleep(.25)
    #
    #     for table in tables:
    #         time.sleep(.5)
    #         # add new button on pop up
    #         button = self.driver.find_element_by_xpath(
    #             '//*[@id="variation41490270"]/div[2]/div/div[8]/div[3]/a')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #         time.sleep(2)
    #         # breed input field
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
    #         time.sleep(2)
    #         for index, row in table.iterrows():
    #             print(row.Breed)
    #             # this clicks addnew i think
    #             self.search_field.send_keys(str(row.Breed))
    #             time.sleep(.5)
    #             # clicks on the right one
    #             self.search_field.send_keys(Keys.DOWN + Keys.ENTER)
    #
    #         time.sleep(.5)
    #         # fills out time
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         time.sleep(.5)
    #         # saves new thing
    #         button = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #     # presses save button for everyhting
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41490270"]/div[2]/div/div[9]/div[2]/input')
    #     self.driver.execute_script("arguments[0].click();", button)
    #
    #     self.pass_log()
    #
    # def test_brushOut(self):
    #     """
    #     add dog breeds to services in mytime
    #     :return: void
    #     """
    #
    #     time.sleep(2)
    #
    #     # clicks edit button for blow
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41487365"]/div/div[4]/div/a')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     time.sleep(.25)
    #
    #     for table in tables:
    #         time.sleep(.5)
    #         # add new button on pop up
    #         button = self.driver.find_element_by_xpath(
    #             '//*[@id="variation41487365"]/div[2]/div/div[8]/div[3]/a')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #         time.sleep(.5)
    #         # breed input field
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
    #         time.sleep(2)
    #         for index, row in table.iterrows():
    #             print(row.Breed)
    #             # this clicks addnew i think
    #             self.search_field.send_keys(str(row.Breed))
    #             time.sleep(.5)
    #             # clicks on the right one
    #             self.search_field.send_keys(Keys.DOWN + Keys.ENTER)
    #
    #         time.sleep(.5)
    #         # fills out time
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         time.sleep(.5)
    #         # saves new thing
    #         button = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #     # presses save button for everyhting
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41487365"]/div[2]/div/div[9]/div[2]/input')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     self.pass_log()
    #
    # def test_furMinator(self):
    #     """
    #     add dog breeds to services in mytime
    #     :return: void
    #     """
    #
    #     time.sleep(2)
    #
    #     # clicks edit button for blow
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41489380"]/div/div[4]/div/a')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     time.sleep(.25)
    #
    #     for table in tables:
    #         time.sleep(.5)
    #         # add new button on pop up
    #         button = self.driver.find_element_by_xpath(
    #             '//*[@id="variation41489380"]/div[2]/div/div[7]/div[3]/a')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #         time.sleep(.5)
    #         # breed input field
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
    #         time.sleep(2)
    #         for index, row in table.iterrows():
    #             print(row.Breed)
    #             # this clicks addnew i think
    #             self.search_field.send_keys(str(row.Breed))
    #             time.sleep(.5)
    #             # clicks on the right one
    #             self.search_field.send_keys(Keys.DOWN + Keys.ENTER)
    #
    #         time.sleep(.5)
    #         # fills out time
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         time.sleep(.5)
    #         # saves new thing
    #         button = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #     # presses save button for everyhting
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41489380"]/div[2]/div/div[8]/div[2]/input')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     self.pass_log()
    #
    # def test_fleaTick(self):
    #     """
    #     add dog breeds to services in mytime
    #     :return: void
    #     """
    #
    #     time.sleep(5)
    #
    #     # clicks edit button for blow
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41489442"]/div/div[4]/div/a')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     time.sleep(.25)
    #
    #     for table in tables:
    #         time.sleep(.5)
    #         # add new button on pop up
    #         button = self.driver.find_element_by_xpath(
    #             '//*[@id="variation41489442"]/div[2]/div/div[7]/div[3]/a')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #         time.sleep(.5)
    #         # breed input field
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/input')
    #         time.sleep(2)
    #         for index, row in table.iterrows():
    #             print(row.Breed)
    #             # this clicks addnew i think
    #             self.search_field.send_keys(str(row.Breed))
    #             time.sleep(.5)
    #             # clicks on the right one
    #             self.search_field.send_keys(Keys.DOWN + Keys.ENTER)
    #
    #         time.sleep(.5)
    #         # fills out time
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[2] / div[2] / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[1] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         self.search_field = self.driver.find_element_by_xpath(
    #             '/ html / body / div[8] / div / div / div / div / div / div[2] / div[3] / div[2] / div / div[2] / div / input')
    #         self.search_field.send_keys("10")
    #
    #         time.sleep(.5)
    #         # saves new thing
    #         button = self.driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/div/div/div[3]/div/a[2]')
    #         self.driver.execute_script("arguments[0].click();", button)
    #
    #     # presses save button for everyhting
    #     button = self.driver.find_element_by_xpath(
    #         '//*[@id="variation41489442"]/div[2]/div/div[8]/div[2]/input')
    #     self.driver.execute_script("arguments[0].click();", button)
    #     self.pass_log()

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