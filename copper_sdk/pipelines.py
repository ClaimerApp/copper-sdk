from copper_sdk.base import BaseResource

class Pipelines(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/pipelines/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/pipelines', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/pipelines/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/pipelines/{id}")

    def list(self):
        return self.copper.get('/pipelines')
