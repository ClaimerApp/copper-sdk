from copper_sdk.base import BaseResource


class Account(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self):
        return self.copper.get(f'/account')

