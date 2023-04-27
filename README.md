# PyPaytabs V2
## updated to work with paytabs api v2
PyPaytabs is a Python library for Paytabs Payment Gateway.

Features:
---------

-  Authentication by profile_id and secret_key
-  Payment Page Creation
-  Payment Process Verification

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyPaytabs.

```bash
pip install pypaytabs
```

## Usage
You are required to Login to obtain profile and secret_key from [Paytabs](https://www.paytabs.com/en/)

```python
 pay_data = {
     "profile_id": profile_id,
     "tran_type": "sale",
     "tran_class": "ecom",
     "cart_id": "cart_11111",
     "cart_currency": "SAR",
     "cart_amount": 100,
     "cart_description": "Description of the items/services",
     "paypage_lang": "en",
     "customer_details": {
         "name": "first last",
         "email": "email@domain.com",
         "phone": "0522222222",
         "street1": "address street",
         "city": "riyad",
         "state": "r",
         "country": "sa",
         "zip": "12345"
     },
     "shipping_details": {
        "name": "name1 last1",
         "email": "email1@domain.com",
         "phone": "971555555555",
         "street1": "street2",
         "city": "dubai",
         "state": "dubai",
         "country": "AE",
         "zip": "54321"
     },
     "callback": "",
     "return": "https://www.example.com/"
 }
 check_data = {
     "profile_id": profile_id,
     "tran_ref": "TST00000000000000"
 }
 paytabs = Paytabs(key="paytabs-key")
 payment_creation = paytabs.create_payment(pay_data)
 payment_check = paytabs.verify_payment(check_data)
 print(payment_creation)
 print(payment_creation)
```

## Maintainers
- Belal Salah (belalsalah140@gmail.com)
- Mohamed Hammad (https://mohamedhammad.info)
- marwanmohamed :  
    <a href="https://www.linkedin.com/in/marwan6569/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a> <a href="https://www.facebook.com/marwanmo7amed8"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" /></a>
