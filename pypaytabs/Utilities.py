# -*- coding: utf-8 -*-
import json


class PaytabsApiResponse(object):
    def __init__(self, status, response_status):
        self.status = status
        self.response_status = response_status.lower()
        self.data = {}

    def add_data(self, key, value):
        self.data.update({key:value})

    def get(self, key):
        return self.data[key] if key in self.data else None


def list_splitter(lst):
    return ' || '.join(lst)


def prepare_invoice(products):
    if isinstance(products, dict) and len(products.keys()) == 3 and \
            'names' in products.keys() and \
            'quantities' in products.keys() and \
            'prices' in products.keys() and \
            isinstance(products['names'], list) and \
            isinstance(products['quantities'], list) and \
            isinstance(products['prices'], list):
        products.update({'names': list_splitter(products['names'])})
        products.update({'prices': list_splitter(products['prices'])})
        products.update({'quantities': list_splitter(products['quantities'])})
        return products
    else:
        raise Exception("Products dictionary isn't in right format")