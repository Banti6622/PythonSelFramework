
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger() ##.......
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"]) ##mention only last name not email
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    ###@pytest.fixture(params=[{"firstname": "Sagar", "lastname":"Sarade", "Gender": "Male"}, {"firstname": "Yusuf", "lastname":"Tamboli", "Gender": "Male"}])
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):     #request is default object of fixture which automatically initilized when fixture is being executed
        return request.param


