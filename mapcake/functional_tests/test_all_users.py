# -*- coding:utf-8 -*-
# import unittest
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.keys import Keys
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase


class HomeNewVisitorTest(LiveServerTestCase):

    """docstring for HomeNewVisitorTest"""

    def setUp(self):
        self.browser = webdriver.WebDriver()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Satisfied, he goes out to meet some friends
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        # Thales was listen last nigth about a new cool map service named
        # MapCake. He goes to the home page to view the homepage
        self.browser.get(self.get_full_url("home"))
        # He show the page title and header mention maps and MapCake
        self.assertIn('MapCake', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('MapCake', header_text)

        # He founds a navigation bar
        nav_bar = self.browser.find_element_by_tag_name('nav').text
        self.assertTrue(nav_bar)
        # At the nav bar he found a layers link and 2 buttons
        # one to sing up and other to log in
        layers_link = self.browser.find_element_by_link_text('Layers')
        # layers_link = self.browser.find_element_by_link_text('Login')
        # layers_link = self.browser.find_element_by_link_text('Register')
        # He selects the Layers Link and goes to public layers index.
        
        # He shows a very prety layer with dots and clicks in the title.

        # The single layer view opens.
