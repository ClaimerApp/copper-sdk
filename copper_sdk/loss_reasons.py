from copper_sdk.base import BaseResource


class LossReasons(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self):
        return self.copper.get(f'/loss_reasons')
