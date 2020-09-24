from django.test import TestCase
from .models import Item
from . import views


class  ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(category='Sound', type='Speaker', model='TW Audio C15', serial_number='SKO5689o990')

    def test_say_hello(self):
        item = Item.objects.get(model='TW Audio C15')
        self.assertEqual(item.say_hello(), 'My type is Speaker my model is TW Audio C15.')

    def test__str__(self):
        item = Item.objects.get(model='TW Audio C15')
        self.assertEqual(item.__str__(), '(Sound) Speaker, TW Audio C15, [SN: SKO5689o990]')
