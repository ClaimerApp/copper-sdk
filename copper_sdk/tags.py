from copper_sdk.base import BaseResource


class Tags(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def list(self):
        return self.copper.get(f'/tags')
