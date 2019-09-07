class People():
    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get('/people/' + id)

    def get_by_email(self, email):
        return self.copper.post('/people/fetch_by_email', { 'email': email })

    def create(self, body = {}):
        return self.copper.post('/people', body)

    def update(self, id, body = {}):
        return self.copper.put('/people/' + id, body)

    def delete(self, id):
        return self.copper.delete('/people/' + id)

    def list(self, body = {}):
        default_body = {
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
            'sort_by': 'first_name',  # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }

        return self.copper.post('/people/search', { **default_body, **body})

    def activities(self, id):
        return self.copper.get('/people/' + id + "/activities")

    def contact_types(self):
        return self.copper.get('/contact_types')