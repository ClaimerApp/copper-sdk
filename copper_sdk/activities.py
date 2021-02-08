from copper_sdk.base import BaseResource


class Activities(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get('/activities/' + id)

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/activities', body)

    def delete(self, id):
        return self.copper.delete('/activities/' + id)

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            # 'parent': {}, # hash	A hash describing the resource to which activities must belong (footnote 1).
            # 'activity_types': {}, # activity_type[]	The activity types to filter results on (footnote 1).	none
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
            # 'minimum_activity_date': "", # number	The Unix timestamp of the earliest activity date.	none
            # 'maximum_activity_date': "", # number	The Unix timestamp of the latest activity date.	none
            'full_result': False, # boolean	(Optional) If set to true, search performance improves but duplicate activity logs may be returned (footnote 3).	false
        }

        return self.copper.post('/activities/search', { **default_body, **body})

    def types(self):
        return self.copper.get('/activity_types')
