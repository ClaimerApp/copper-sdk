from copper_sdk.base import BaseResource

class Tasks(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/tasks/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/tasks', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/tasks/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/tasks/{id}")

    def relate(self, id, entity_id, entity_type):
        """Relate this task to another entity (e.g. person). Note: tasks cannot be unrelated later."""
        body = {
          'resource': {
              'id': entity_id,
              'type': entity_type
          }
        }
        return self.copper.post(f'/tasks/{id}/related', body)

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            'page_number': 1,         # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20,          # number	The number of entries included in a page of results	20
            'sort_by': 'name',        # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }

        return self.copper.post('/tasks/search', {**default_body, **body})
