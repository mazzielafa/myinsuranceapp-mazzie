import json
from lib2to3.pgen2 import token
import unittest
from urllib import response
from project import app 

class TestApp(unittest.TestCase):

    token=''
   
    def test_1_getToken(self):
        self.client = app.test_client(self)
        test_data = {"email":"client@clienttoken.com","password":"thisisapassword"}
        response = self.client.post('/api/v1/token',content_type="application/json", json=test_data)         
        self.assertTrue(response.status_code,200)
        data = response.json     
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def test_2_get_user_products_valid_token(self):
        tester = app.test_client(self)        
        headers = {"Authorization": f"Bearer {TestApp.token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data=response.json      
        self.assertTrue(response.status_code,200)
        self.assertTrue(len(data)>0)

    def test_3_get_user_products_invalid_token(self):
        tester = app.test_client(self)
        ivalid_fake_token='CfDJ8OW5OI0CPGJBgSNlGwO0x4YF7qbYKVv7KOO-N0eFtDUzXOrL7F9Xd9W1otVi4ueJOkAmAhuoHFWNkqRaFD7zvAMHMSKncl6Vo5QXKmpvy6vqxOKxSURdIey8aZPRi3Nnhp2p9la-Al5xrVKz0lignRdcCHf3O7pF9zv_sNx_c_T7pUe3WsxaJEPX3t_9FO2Wjw'
        headers = {"Authorization": f"Bearer {ivalid_fake_token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data=response.json   
        self.assertTrue(response.status_code > 400)