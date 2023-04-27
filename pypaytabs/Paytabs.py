# -*- coding: utf-8 -*-
import json
import requests


API_URL = 'https://secure.paytabs.sa'
ERROR_CODES = [0, 101, 102, 104, 110, 114, 150, 151, 152, 200, 201, 202, 203, 204, 205, 207, 208, 209, 210, 211, 220,
               221, 222, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240, 242, 244, 250, 301, 305, 306, 307, 308, 328,
               330, 331, 333, 334, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 360, 361,
               362, 363, 400, 401, 402, 403, 475, 476, 481, 482, 483, 484, 485, 486, 700, 800, 801, 802, 803, 804, 805,
               806, 807, 808, 4001, 4002, 4007, 4008, 4013, 4014, 4094, 4404]


class Paytabs(object):

    def __init__(self, key):
        self.key = key
        self.content_type = 'json'

    def create_payment(self, data):
        json_data = json.dumps(data)
        result = self._start_connection(API_URL, '/payment/request', json_data)
        return self._parse_response(result)

    def verify_payment(self, data):
        json_data = json.dumps(data)
        result = self._start_connection(API_URL, '/payment/query', json_data)
        return self._parse_response(result)

    def _start_connection(self, api_url, api_endpoint, data):
        headers = {"authorization": self.key, "Content-Type": "application/json", }
        response = requests.request('POST', api_url+api_endpoint, headers=headers, data=data)

        return response

    @staticmethod
    def _parse_response(response):
        data = json.loads(response.text)
        status = response.status_code
        return status, data
