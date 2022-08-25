# PyPaytabs

PyPaytabs is a Python library for Paytabs Payment Gateway.

Features:
---------

-  Authentication by merchant_email and secret_key
-  Payment Page Creation
-  Payment Process Verification

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyPaytabs.

```bash
pip install pypaytabs
```

## Usage
You are required to Login to obtain merchant_email and secret_key from [Paytabs](https://www.paytabs.com/en/)

```python
from pypaytabs import Paytabs
from pypaytabs import Utilities as util
paytab = Paytabs(merchant_email, secret_key) # return an object of paytabs
#authenticate with returned object
result = paytab.authenticate() # returns PaytabsApiResponse object with response_status and status or exception error (PaytabsApiError: Invalid)
print('Result', result.data) #Result {'result': 'valid', 'response_code': '4000'} or pypaytabs.Exceptions.PaytabsApiError: invalid
#Prepare product names list to be passed to create_pay_page method
products = {'names':['product_1','product_2','product_3'],'quantities':['5','2.5','10'],'prices':['5','8','9']}
invoice_products = util.prepare_invoice(products)
print('Invoice Details: ', invoice_products)  #{'names': 'product_1 || product_2 || product_3', 'prices': '5 || 8 || 9', 'quantities': '5 || 2.5 || 10'}
#to create pay page, you have to prepare data as dictionary as like:
pay_data = {"merchant_email":paytab.email, 'secret_key':paytab.key,
            "site_url" : "https://www.yourwebsite.com",
            "return_url" : "https://www.yourwebsite.com/return",
            "title": "JohnDoe And Co.",
            "cc_first_name": "John",
            "cc_last_name": "Doe",
            "cc_phone_number": "00973",
            "phone_number": "123123123456",
            "email": "johndoe@example.com",
            "products_per_title": invoice_products['names'], #by using invoice_products dictionary returned from prepare_invoice method,
            "unit_price": invoice_products['prices'],
            "quantity": invoice_products['quantities'],
            "other_charges": "12.123",
            "amount": "136.082",
            "discount": "10.123",
            "currency": "BHD",
            "reference_no": "ABC-123",
            "ip_customer": "1.1.1.0",
            "ip_merchant": "1.1.1.0",
            "billing_address": "Flat 3021 Manama Bahrain",
            "city": "Manama",
            "state": "Manama",
            "postal_code": "12345",
            "country": "BHR",
            "shipping_first_name": "John",
            "shipping_last_name": "Doe",
            "address_shipping": "Flat 3021 Manama Bahrain",
            "state_shipping": "Manama",
            "city_shipping": "Manama",
            "postal_code_shipping": "1234",
            "country_shipping": "BHR",
            "msg_lang": "English",
            "cms_with_version": "WordPress4.0-WooCommerce2.3.9"
            }
#Creation of Payment Page
result = paytab.create_payment(**pay_data) #to create payment page, return PaytabsApiResponse with data dict contains payment_url and p_id
print('Result:', result.data) #Result {'result': 'The Pay Page is created.', 'response_code': '4012', 'payment_url': 'https://www.paytabs.com/osdh3SCmEYoD5trKc4oz2VmE91mmQCtqop-PgmsGyFHj9zE/dCetYxYV8qi0XIBl49Y9dMAFPGNTkb6Yot-wgKYKCo94jE8/DTKnWzcrnK65jwoj2X6pmtvj8UI-3YmGDuJ6vDD8FizQOYE/CkdveIWwKhMDPXsuU8vJysaf1ccsOG1XYOZF8O15JInD28z1pER29OEX27E10GXQAI7FCzUJgSyp-6XRgYeejOPf7g', 'p_id': 333348}
#Verify Payment
verifying_data = {
    "payment_reference": result.data['p_id']
 }
return_obj = paytab.verify_payment(**verifying_data) #verify payment process by using payment reference code, returns PaytabsApiResponse with data dict contains
print('Payment Status', return_obj.data) #{"result": "The payment is completed successfully!","response_code": "100","pt_invoice_id": "2124779","amount": 11.45,"currency": "OMR","reference_no": "12","transaction_id": "1720833"} or Raise Exceptions
```


## Maintainers
- Belal Salah (belalsalah140@gmail.com)
- Mohamed Hammad (https://mohamedhammad.info)
