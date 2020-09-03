class Users():
    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/users/{id}")

    def list(self, body = {}):
        default_body = {
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
        }

        return self.copper.post('/users/search', { **default_body, **body})
