from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from layers.views import layers_list

# Create your tests here.
class LayersPagesTest(TestCase):

    def test_layers_url_resolves_to_layers_list_view(self):
        found = resolve('/layers/')
        self.assertEqual(found.func, layers_list)

    def test_layers_page_returns_the_public_layers_list(self):
        request = HttpRequest()
        response = layers_list(request)
