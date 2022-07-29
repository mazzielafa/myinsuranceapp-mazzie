from cgitb import text
import json
import unittest
from urllib import response
import requests

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1'

    def test_1_post(self):
        url=f"{self.base_url}/token"
        test_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"}
        response = requests.post(url, json=test_data)         
        self.assertTrue(response.status_code,200)
        data = response.json     
        self.headers = {"Authorization": f"Bearer {self.token}"}

    # def test_2_user_products(self):
    #     url=f'{self.base_url}/users/1/products'
    #     headers = {"Authorization":f"Bearer {TestApp.token}"}
    #     response = requests.get(url)
    #     data = response.json
    #     self.assertEqual(response.status_code,200)
      


