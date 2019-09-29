from selenium.webdriver.common.by import By


class PageLocators(object):
    ''''A class for general locators'''
    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[value=Go]")
    
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    SELECT_RESULT_0 = (By.ID, "result_0")
    
    SAVE_FOR_LATER = (By.CSS_SELECTOR, "input[value='Save for later']")
    DELETE = (By.CSS_SELECTOR, "input[value='Delete']")
    ACTIVE_ITEMS = (By.CSS_SELECTOR, "div[data-itemtype='active']")
    SAVED_ITEMS = (By.CSS_SELECTOR, "div[data-itemtype='saved']")
    DELETED_ITEMS = (By.CSS_SELECTOR, "div[data-removed='true']")
    
    QUANTITY_BUTTON = (By.CSS_SELECTOR, "span[data-a-class='quantity']")
    QUANTITY = (By.CSS_SELECTOR, "a[class='a-dropdown-link']")
    DATA_QUANTITY_3 = (By.CSS_SELECTOR, "div[data-quantity='3']")
    DATA_QUANTITY_1 = (By.CSS_SELECTOR, "div[data-quantity='1']")
    
    DATA_GIFT_WRAPPED = (By.CSS_SELECTOR, "div[data-giftwrapped='1']")
    GIFT_CHECKBOX = (By.ID, "sc-buy-box-gift-checkbox")
    
    BASKET = (By.ID, "nav-cart-count")
    ALERT_ICON = (By.ID, "huc-v2-order-row-icon")
    
    