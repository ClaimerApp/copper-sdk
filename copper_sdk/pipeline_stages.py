from copper_sdk.base import BaseResource

class PipelineStages(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/pipeline_stages/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/pipeline_stages', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/pipeline_stages/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/pipeline_stages/{id}")

    def list(self):
        return self.copper.get('/pipeline_stages')
