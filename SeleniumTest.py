import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pageobject
from locators import PageLocators



#List of books to be used for this test
BOOKS_LIST = ("Experiences of Test Automation: Case Studies of Software Test Automation",
              "Agile Testing: A Practical Guide for Testers and Agile Teams",
              "Selenium WebDriver 3 Practical Guide: End-to-end automation testing for web and mobile browsers with Selenium WebDriver, 2nd Edition")

class SeleniumTest(unittest.TestCase):
    '''Selenium test
    '''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.amazon.com")

    def test_search_add_modify_basket(self):
        '''
        Test to searching books from BOOKS_LIST,
        add them to a basket,
        save for later Experiences of Test Automation book,
        delete Agile Testing book
        increase quantity of Selenium WebDriver 3 book to 3
        mark all books as gift
        decrease quantity of Selenium WebDriver 3 book to 1
        '''
        # Check if opened page has Amazon in a title of page
        main_page = pageobject.MainPage(self.driver)
        self.assertTrue(main_page.check_title(), "Amazon doesn't appear in the title.")
        # Loop for searching and adding to the basket books from BOOKS_LIST
        for book in BOOKS_LIST:
            # Search book
            main_page.search_for = book
            main_page.do_search()
            # Save result page as a search_result
            search_results = pageobject.SearchResults(self.driver)
            # Check if book appears in result page
            self.assertFalse(search_results.is_no_result(), "Failed to find book: %s" %book)
            # Find the book and open more details page for this book
            search_results.select_book(book)
            book_details = pageobject.DetailsPage(self.driver)
            # Add to the basked selected book
            book_details.add_to_basket()
            self.assertTrue(book_details.is_book_added(), "Failed to add book %s to the basket"%book)
        # Check if amount in basket is as expected
        self.assertIn("3", main_page.items_in_basket(),"Wrong amount of items in the basket")
        # Go to basked page
        book_details.edit_basket()
            
        basket_page = pageobject.BasketPage(self.driver)
        # Check if all books are listed on cart page
        self.assertEqual(basket_page.AvailableElements(), 3, "Wrong amount of items in the basket")

        # Save for later 1st book from BOOKS_LIST
        basket_page.save_for_later(BOOKS_LIST[0])
        # Wait till item goes to Saved For Later state
        main_page.wait_for_element = PageLocators.SAVED_ITEMS
        self.assertIn("2", main_page.items_in_basket(),"Wrong amount of items in the basket")
        
        # Take a note of amount of books in basket before deleting
        main_page.text = self.driver.find_element(*PageLocators.BASKET).text
        # Delete 2nd book from BOOKS_LIST
        basket_page.delete(BOOKS_LIST[1])
        # Wait till deleted book appears as deleted item
        main_page.wait_for_element = PageLocators.DELETED_ITEMS
        # Wait for update of amount of basket items
        main_page.wait_for_text_change = PageLocators.BASKET
        self.assertIn("1", main_page.items_in_basket(),"Wrong amount of items in the basket")

        # Change quantity of the only one book in basket
        basket_page.add_quantity(3)
        main_page.wait_for_element = PageLocators.DATA_QUANTITY_3

        # Mark items in basket as a gift
        basket_page.mark_as_gift()
        main_page.wait_for_element = PageLocators.DATA_GIFT_WRAPPED
        
        # Change back quantity of book
        basket_page.add_quantity(1)
        main_page.wait_for_element = PageLocators.DATA_QUANTITY_1
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()