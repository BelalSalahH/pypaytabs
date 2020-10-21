# -*- coding: utf-8 -*-
import json
import urllib.parse
import http.client
from pypaytabs.Exceptions import PaytabsApiError
from pypaytabs.Utilities import PaytabsApiResponse

API_URL = 'www.paytabs.com'
ERROR_CODES = [0, 101, 102, 104, 110, 114, 150, 151, 152, 200, 201, 202, 203, 204, 205, 207, 208, 209, 210, 211, 220,
               221, 222, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240, 242, 244, 250, 301, 305, 306, 307, 308, 328,
               330, 331, 333, 334, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 360, 361,
               362, 363, 400, 401, 402, 403, 475, 476, 481, 482, 483, 484, 485, 486, 700, 800, 801, 802, 803, 804, 805,
               806, 807, 808, 4001, 4002, 4007, 4008, 4013, 4014, 4094, 4404]

class Paytabs(object):

    def __init__(self, email, key):
        self.email = email
        self.key = key
        self.content_type = 'json'

    def authenticate(self):
        data = {
            "merchant_email": self.email,
            "secret_key":  self.key
        }
        result = self._start_connection(API_URL, '/apiv2/validate_secret_key', **data)
        return self._parse_response(result)

    def create_payment(self, **kwargs):
        result = self._start_connection(API_URL, '/apiv2/create_pay_page', **kwargs)
        return self._parse_response(result)

    def verify_payment(self, **kwargs):
        result = self._start_connection(API_URL, '/apiv2/verify_payment', **kwargs)
        return self._parse_response(result)

    def _parse_response(self, data):
        json_dict = json.loads(data.decode('utf-8'), encoding='utf-8')
        is_error = int(json_dict['response_code']) in ERROR_CODES
        if is_error:
            raise PaytabsApiError(json_dict['response_code'], json_dict['result'])
        response = PaytabsApiResponse(json_dict['response_code'], json_dict['result'])
        for key, value in json_dict.items():
            response.add_data(key, value)
        return response

    def _start_connection(self, api_url, api_endpoint, **kwargs):
        params = urllib.parse.urlencode(kwargs)
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPSConnection(api_url)
        conn.request("POST", api_endpoint, params, headers)
        response = conn.getresponse()
        result = response.read()
        conn.close()
        return result