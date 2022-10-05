from time import sleep
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class TrendsSearcher:
    def __init__(self):
        self.display = Display(visible=False, size=(1100, 700))
        self.display.start()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    

    def getGoogleTrendsData(self, searchTerm: str):
        self.driver.get(f'https://trends.google.com.br/trends/?geo=BR')
        self.searchInGoogleTrendsAndPassPageToBs4(searchTerm)
    

    def getMostPopularSearchesInGoogleTrends(self):
        """ Get the most popular searches in the GoogleTrends """
        self.showPrincipalResults()


    def showPrincipalResults(self):
        selectOptionNumber = 42
        for selectLabelNumber in range(40, 29, -5):
            # Gets parent because the child have a more certain ID, and parent can be clicked
            ascentionAndPrincipalLabel = self.returnElementParentOrFalse(By.ID, 
            f'select_value_label_{selectLabelNumber}')

            self.selectPrincipalOptionIfLabelExists(ascentionAndPrincipalLabel, 
            f'select_option_{selectOptionNumber}')

            selectOptionNumber -= 5
    

    def getMostPopularSearches(self):
        pass


    def selectPrincipalOptionIfLabelExists(self, selectLabel, selectOptionID: str):
        if selectLabel:
                self.selectPrincipalOption(selectLabel, selectOptionID)


    def selectPrincipalOption(self, selectLabel, selectOptionID: int):
        self.clickOnElementInSelenium(self.returnElementOrFalse(selectLabel.attrs['id'], By.ID))
        sleep(0.5)
        self.clickOnElementInSelenium(self.returnElementOrFalse(selectOptionID, By.ID))


    def clickOnElementInSelenium(self, element: WebElement):
        self.driver.execute_script('arguments[0].click()', element)


    def searchInGoogleTrendsAndPassPageToBs4(self, searchTerm: str):
        sleep(1.5)
        searchBar = self.getSearchBar()
        searchBar.send_keys(searchTerm + Keys.RETURN)
        sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.soup = BeautifulSoup(self.driver.page_source, features='html.parser')


    def getSearchBar(self) -> WebElement:
        searchBar = self.returnElementOrFalse('input-254', By.ID)
        if not searchBar:
            return self.driver.find_element('input-1')
        return searchBar


    def returnElementParentOrFalse(self, param, elementParamValue: str):
        elementWasGotten = self.returnElementInBs4OrNone(param, elementParamValue)
        if elementWasGotten:
            print(elementWasGotten.prettify())
            return elementWasGotten.find_parent()
        return False


    def returnElementInBs4OrNone(self, param: str, elementParamValue: str, elementName=None):
        if elementName is not None:
            return self.soup.find(elementName ,attrs={param: elementParamValue})
        return self.soup.find(attrs={param: elementParamValue})


    def returnElementOrFalse(self, elementName: str, locator: str):
        try:
            return self.driver.find_element(locator, elementName)
        except:
            return False
    

    def stopAll(self):
        self.driver.quit()
        self.display.stop()


if __name__ == '__main__':
    searcher = TrendsSearcher()
    searcher.getGoogleTrendsData('example')
    searcher.getMostPopularSearchesInGoogleTrends()    
    searcher.stopAll()