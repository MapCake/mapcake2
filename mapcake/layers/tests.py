from django.test import TestCase
from django.core.urlresolvers import resolve
from layers.views import layers_list

# Create your tests here.
class LayersPagesTest(TestCase):

    def test_layers_url_resolves_to_layers_list_view(self):
        found = resolve('/layers/')
        self.assertEqual(found.func, layers_list)
