# -*- coding: utf-8 -*-
from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from home.views import home

# Create your tests here.


class HomePageTest(TestCase):

    """docstring for TestHomePage"""

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")
        