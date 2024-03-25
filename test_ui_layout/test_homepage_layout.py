from pom.home_page_elements import MyHomepage
from pom.shop_women_elements import ShopWomen
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.regression
def test_about_us_section_verbiage(set_up) -> None:
    
    # import from conftest
    page = set_up

    #assert page.is_visible(HomePage.celebrate_header)
    #print('Page is visible')
    #home_page = HomePage()
    #expect(ShopWomen.celebrating_beauty_header).to_be_visible()
    #expect(MyHomepage.myname).to_be_visible()

    expect(page.get_by_text("Shop Women Winter")).to_be_visible()
    #expect(home_page.celebrate_name).to_be_visible()
    #print('Test Completed')clear

def test_about_us_section_verbiage_2(set_up) -> None:

     # import from conftest
    page = set_up

    #assert page.is_visible(HomePage.celebrate_header)
    #print('Page is visible')
    #home_page = HomePage()
    #expect(ShopWomen.celebrating_beauty_header).to_be_visible()
    #expect(MyHomepage.myname).to_be_visible()

    expect(page.get_by_text("Shop Women Winterx123")).to_be_visible()
    #expect(home_page.celebrate_name).to_be_visible()
    #print('Test Completed')clear

def test_about_us_section_verbiage2(set_up) -> None:
    
     # import from conftest
    page = set_up

    #assert page.is_visible(HomePage.celebrate_header)
    #print('Page is visible')
    #home_page = HomePage()
    #expect(ShopWomen.celebrating_beauty_header).to_be_visible()
    #expect(MyHomepage.myname).to_be_visible()

    expect(page.get_by_text("Shop Women Winter")).to_be_visible()
    #expect(home_page.celebrate_name).to_be_visible()
    #print('Test Completed')clear


    

