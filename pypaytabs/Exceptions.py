# -*- coding: utf-8 -*-

class PaytabsApiError(Exception):
    """Exception raised when an a RequestHandler indicates the request failed.

    Attributes:
        code         -- the error code returned from the API
        msg_english  -- explanation of the error
    """

    def __init__(self, code,  message):
        self.code = code
        self.massage = message
        super(PaytabsApiError, self).__init__(message, )


