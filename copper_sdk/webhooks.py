from copper_sdk.base import BaseResource

class Webhooks(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/webhooks/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/webhooks', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/webhooks/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/webhooks/{id}")

    def list(self):
        return self.copper.get('/webhooks')
