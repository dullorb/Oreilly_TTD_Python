from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from TDD_learn.views import home_page


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'home.html')



