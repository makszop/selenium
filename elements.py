from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class text_change():
    '''This method when is called, checks actual tet of element.
        returns True or False which is passed to WaitForElementTextChange method
    '''
    def __init__(self, locator, text):
        self.text = text
        self.locator = locator
        
    def __call__(self, driver):
        actual_text = driver.find_element(*self.locator).text
        return self.text != actual_text
        
class SearchBar():
    ''' This class is for search baron web page.'''

    def __set__(self, instance, value):
        '''Clean up input field and sets it to the value supplied'''
        
        driver = instance.driver
        instance.wait_for_element = self.search_locator
        driver.find_element(*self.search_locator).clear()
        driver.find_element(*self.search_locator).send_keys(value)

    def __get__(self, instance, owner):
        '''Gets the text of the input field'''
        driver = instance.driver
        instance.wait_for_element = self.search_locator
        element = driver.find_element(*self.search_locator)
        return element.get_attribute("value")
    
    
class WaitForElement():
    '''Method to wait for element appears on page'''

    def __set__(self, instance, value):
        driver = instance.driver
        try:
                WebDriverWait(driver, 100).until(lambda driver: driver.find_element(*value))
        except TimeoutException:
                print("Warning! Failed to find element %s" %str(value))
                pass

class WaitForElementTextChange():
    '''Method to wait till text changes for element on page'''

    def __set__(self, instance, value):
        driver = instance.driver
        text = instance.text
        try:
                WebDriverWait(driver, 100).until(text_change(value,text))
        except TimeoutException:
                print("Warning! Failed to spot changes for %s, Actual: %s, Expected: %s" %(str(value), value.text, text))
                pass
        
