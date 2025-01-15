from django.test import TestCase
from django.urls import reverse

class AddViewTests(TestCase):
    def test_empty_string_returns_zero(self):
        response = self.client.post(reverse('add'), {'numbers': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 0})

    def test_single_number(self):
        response = self.client.post(reverse('add'), {'numbers': '1'})
        self.assertEqual(response.json(), {'result': 1})

    def test_two_numbers(self):
        response = self.client.post(reverse('add'), {'numbers': '1,2'})
        self.assertEqual(response.json(), {'result': 3})

    def test_multiple_numbers(self):
        response = self.client.post(reverse('add'), {'numbers': '1,2,3,4'})
        self.assertEqual(response.json(), {'result': 10})

    def test_newline_as_delimiter(self):
        response = self.client.post(reverse('add'), {'numbers': '1\n2,3'})
        self.assertEqual(response.json(), {'result': 6})

    def test_custom_delimiter(self):
        response = self.client.post(reverse('add'), {'numbers': '//;\n1;2'})
        self.assertEqual(response.json(), {'result': 3})

    def test_multiple_negative_numbers(self):
        response = self.client.post(reverse('add'), {'numbers': '1,-1,-2'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Negative numbers not allowed: -1, -2'})
