from elements import *
from locators import *

class SearchLocator(SearchBar):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    search_locator = PageLocators.SEARCH

class BasePage():
    '''General base object will be called from all pages'''

    wait_for_element = WaitForElement()
    wait_for_text_change = WaitForElementTextChange()
    text = ''

    def __init__(self, driver):
        self.driver = driver
        

class MainPage(BasePage):
    '''Main page object. Use this class to add new methods for main page only'''

    #Declares a variable that will contain the retrieved text
    search_for = SearchLocator()

    def check_title(self):
        '''Check if "Amazon" appears in the page title'''
        return "Amazon" in self.driver.title
    
    def do_search(self):
        '''Find search button and click it'''
        self.wait_for_element = PageLocators.SEARCH_BUTTON
        element = self.driver.find_element(*PageLocators.SEARCH_BUTTON)
        element.click()
    
    def items_in_basket(self):
        '''Method to return amount of items in a basket'''
        self.wait_for_element = PageLocators.BASKET
        element = self.driver.find_element(*PageLocators.BASKET)
        return element.text
        
class SearchResults(BasePage):
    '''Search page object. Use this class to add new methods for search page results only'''
    
    def select_the_book(self):
        '''Method to select the book that contains provided title'''
        self.wait_for_element = PageLocators.ADD_TO_CART
        element = self.driver.find_element(*PageLocators.ADD_TO_CART)
        element.click()

    def select_book(self, book):
        '''Find search button and click it'''
        self.wait_for_element = PageLocators.SELECT_RESULT_0
        element = self.driver.find_element(*PageLocators.SELECT_RESULT_0)
        element.find_element_by_partial_link_text(book).click()
        
    def is_no_result(self):
        '''Check if item could not be found'''
        elements = self.driver.find_elements_by_id("noResultsTitle")
        if len(elements) == 0:
            return False
        else:
            return True
        
class BasketPage(BasePage):
    '''Basket page object. Use this class to add new methods for basket only'''
    
    def AvailableElements(self):
        ''' Return amount of items that are only acrive. Skip if it's active and saved or deleted'''
        self.wait_for_element = PageLocators.ACTIVE_ITEMS
        elements = self.driver.find_elements(*PageLocators.ACTIVE_ITEMS)
        for element in elements:
            if element.get_attribute("data-removed") or element.get_attribute("data-removed") == "saved":
                elements.pop(elements.index(element))
        return len(elements)
    
    def save_for_later(self, item):
        '''Save provided item for later'''
        self.wait_for_element = PageLocators.SAVE_FOR_LATER
        elements = self.driver.find_elements(*PageLocators.SAVE_FOR_LATER)
        for element in elements:
            if item in element.get_attribute("aria-label"):
                element.click()
                return
        return
    
    def delete(self, item):
        '''Delete provided item from the basket'''
        self.wait_for_element = PageLocators.DELETE
        elements = self.driver.find_elements(*PageLocators.DELETE)
        for element in elements:
            if item in element.get_attribute("aria-label"):
                element.click()
                return
        return
    
    def add_quantity(self, quantity):
        '''Method to change quantity of item in the basket'''
        self.wait_for_element = PageLocators.QUANTITY_BUTTON
        self.driver.find_element(*PageLocators.QUANTITY_BUTTON).click()
        elements = self.driver.find_elements(*PageLocators.QUANTITY)
        for element in elements:
            if str(quantity) in element.text:
                element.click()
                return
        return
    
    def mark_as_gift(self):
        '''Method to mark items as a gift'''
        self.wait_for_element = PageLocators.GIFT_CHECKBOX
        element = self.driver.find_element(*PageLocators.GIFT_CHECKBOX)
        element.click()
    
class DetailsPage(BasePage):
    '''Details page object. This page appears after adding item to basket.
        Use this class to add new methods for details page only'''
    
    def add_to_basket(self):
        '''Method to add item to the basket'''
        self.wait_for_element = PageLocators.ADD_TO_CART
        element = self.driver.find_element(*PageLocators.ADD_TO_CART)
        element.click()
        return
    
    def edit_basket(self):
        '''Method to navigate to the basket page'''
        self.wait_for_element = PageLocators.BASKET
        element = self.driver.find_element(*PageLocators.BASKET)
        element.click()
        return
    
    def is_book_added(self):
        ''' Check if book is added to the basket.'''
        self.wait_for_element = PageLocators.ALERT_ICON
        element = self.driver.find_element(*PageLocators.ALERT_ICON)
        return "a-alert-success" in element.get_attribute("class")
    
