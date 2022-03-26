class CopperException(IOError):
    """Base Copper Exception."""
    def __init__(self, *args, **kwargs):
        response = kwargs.pop('response', None)
        self.response = response
        self.request = kwargs.pop('request', None)
        self.json_body = kwargs.pop('json_body', None)
        if response is not None and not self.request and hasattr(response, 'request'):
            self.request = self.response.request
        super(CopperException, self).__init__(*args, **kwargs)

class TooManyRequests(CopperException):
    """Too many requests in this time period, wait and retry."""
