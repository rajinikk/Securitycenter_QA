from selenium.webdriver.common.by import By
from selenium import webdriver
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from utilities.ip_file import IP
# from utilities.custom_logger import customLogger as cl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os

from selenium.common.exceptions import *
import logging
import time
import pytest


class SeleniumDriver():
    # log = cl.customLogger(logging.DEBUG)
    # log = cl(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        test= self.driver.current_url
        print('test',test)
        return test

              
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
            # self.log.info("Locator type" + locatorType + "not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            
            element = self.driver.find_element(byType, locator)
            # print("Element Found")
            # self.log.info("Element found with locator: " + locator +
            #               " and locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator +
                           " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            print("element{} present after selecting".format(element))
            element.click()
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
            # self.log.info("clicked on element with locator: " + locator +
            #               " locatorType: " + locatorType)
        except:
            print("cannot click on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            elementList
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data, Keys.TAB)


            #self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            #self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeysEnter(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data, Keys.ENTER)
        except:
            print_stack()

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions= [NoSuchElementException,ElementNotVisibleException,
                                 ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_into_view(self, locator, locator_type=""):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            raise Exception("Element {0} is not visible".format(locator))

    def elementClear(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()


    def elementHover(self, locator="", locatorType="xpath", element=None,):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
                print("element ",element.text)
                hover = ActionChains(self.driver).move_to_element(element)
                hover.click().perform()
                time.sleep(2)
                print("hover to element with locator: " + locator +
                      " locatorType: " + locatorType)
        except:
            print("cannot hover to the element with locator: " + locator +
                       " locatorType: " + locatorType)
            print_stack()

    def pageBack(self):
        '''
        page back the browser
        '''
        self.driver.execute_script("window.history.go(-1)")

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def getText(self, element, info):
        """
        Get 'Text' on an element
        Required Parameters:
            element: Element Object
            info: Information about the element, text on the element
        Optional Parameters:
            None
        Returns:
            Text of element
        """
        if element is not None:
            try:
                text = element.text
                if len(text) == 0:
                    text = element.get_attribute("innerHTML")
                    print("values on text{}".format(text))
                if len(text) != 0:

                    print("Getting text on element {}:: " .format(info))
                    print("The text is ::{} '" .format( text )+ "'")

            except:
                text = None
                # self.log.error("Failed to get text on element " + info)
                # traceback.print_stack()
        else:
            return None
        return text.strip()

    def upload_file(self):
        test_file = os.getcwd()+"/U_RedHat_6_V1R10_STIG_SCAP_1-1_Benchmark.zip"
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",test_file)
        userName = self.driver.find_element_by_xpath("//span[@class='form-item-element']/descendant::div[@id='fileUpload']/descendant::span[@class='btn dummy-button']")
        test = self.driver.execute_script("arguments[0].focus();", userName)
        print("______________________________________")
        time.sleep(3)
        test.send_keys(os.getcwd()+"/U_RedHat_6_V1R10_STIG_SCAP_1-1_Benchmark.zip")

        # hover  = ActionChains(self.driver)
        # try:
        #     if locator:
        #         element = self.getElement(locator, locatorType)
        #         print("element ", element.text)
        #         hover = ActionChains(self.driver).move_to_element(element)
        #         hover.send_keys(os.getcwd()+"/U_RedHat_6_V1R10_STIG_SCAP_1-1_Benchmark.zip").perform()
        #         time.sleep(2)
        #         print("hover to element with locator: " + locator +
        #               " locatorType: " + locatorType)
        # except:
        #     print("cannot hover to the element with locator: " + locator +
        #           " locatorType: " + locatorType)
        #     print_stack()


        
        




        
            

        
            
                
                