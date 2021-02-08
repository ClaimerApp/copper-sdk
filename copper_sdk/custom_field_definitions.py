from copper_sdk.base import BaseResource


class CustomFieldDefinitions(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def list(self):
        return self.copper.get(f'/custom_field_definitions')

    def get(self, id):
        return self.copper.get(f'/custom_field_definitions/{id}')

    def delete(self, id):
        return self.copper.delete(f'/custom_field_definitions/{id}')

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f'/custom_field_definitions/{id}', body)

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/custom_field_definitions', body)
