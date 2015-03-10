# -*- coding:utf-8 -*-
# import unittest
from selenium.webdriver.firefox import webdriver
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
