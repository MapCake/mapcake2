# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    """docstring for NewVisitorTest"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_the_homepage(self):
        # Thales was listen last nigth about a new cool map service named
        # MapCake. He goes to the home page to view the homepage
        self.browser.get('http://localhost:8000')

        # He show the page title and header mention maps and MapCake
        self.assertIn('MapCake', self.browser.title)
        self.fail('Finish the test')

        # Satisfied, he goes out to meet some friends

if __name__ == '__main__':
    unittest.main()
