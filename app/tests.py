# coverage run --source=. manage.py test -v 2
# coverage html
# google-chrome htmlcov/index.html &

# http://www.realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/#.UxCHdFSx0wK

import unittest

from django.core.urlresolvers import reverse
from django.test import TestCase
from setuptools.compat import unicode

from app.models import Cliente

from selenium import webdriver


class ClienteTest(TestCase):

    # models
    def create_cliente(self, nome="raul"):
        return Cliente.objects.create(nome=nome)

    def test_cliente_creation(self):
        c = self.create_cliente()
        self.assertTrue(isinstance(c, Cliente))
        self.assertEqual('raul', c.nome)


    # views (uses reverse)
    def test_cliente_list_view(self):
        c = self.create_cliente()
        url = reverse("app.views.index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(unicode.encode(c.nome), resp.content)

# views (uses Selenium)

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/start/")
        self.driver.find_element_by_id('id_nome').send_keys("test nome")
        # self.driver.find_element_by_id('submit').click()
        # self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit


    # testing FORMS
    # def test_valid_form(self):
    #     w = Whatever.objects.create(title='Foo', body='Bar')
    #     data = {'title': w.title, 'body': w.body,}
    #     form = WhateverForm(data=data)
    #     self.assertTrue(form.is_valid())
    #
    # def test_invalid_form(self):
    #     w = Whatever.objects.create(title='Foo', body='')
    #     data = {'title': w.title, 'body': w.body,}
    #     form = WhateverForm(data=data)
    #     self.assertFalse(form.is_valid())


    # from tastypie.test import ResourceTestCase
    #
    # class EntryResourceTest(ResourceTestCase):
    #
    #     def test_get_api_json(self):
    #         resp = self.api_client.get('/api/whatever/', format='json')
    #         self.assertValidJSONResponse(resp)
    #
    #     def test_get_api_xml(self):
    #         resp = self.api_client.get('/api/whatever/', format='xml')
    #         self.assertValidXMLResponse(resp)

if __name__ == '__main__':
    unittest.main()