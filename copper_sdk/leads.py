class Leads():
    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get('/leads/' + id)

    def create(self, body = {}):
        return self.copper.post('/leads', body)

    def update(self, id, body = {}):
        return self.copper.put('/leads/' + id, body)

    def delete(self, id):
        return self.copper.delete('/leads/' + id)

    def upsert(self, body = {}):
        return self.copper.put('/leads/upsert', body)

    def convert(self, id, body = {}):
        default_body = {
            'person': {}, # object	Details about the Person to be created by the Lead conversion. Valid fields are name, contact_type_id, and assignee_id.
            'company': {}, # object	Details about the Company to which the newly created Person will belong. Valid fields are id or name, and they are mutually exclusive. If a Company id is specified, the new Person will belong to that Company. If the name of an existing Company is specified, the new Person will belong to that Company. If a new name is specified, a new Company will be created with that name, and the new Person will belong to that Company. If you explicitly supply an empty string ("") for the company name, then no Company will be created. By default, fuzzy matching will return a list of candidate companies. An optional Boolean field "exact_match" can be specified if the exact company name is known.
            'opportunity': {}, # object	Details about the Opportunity to be created by the Lead conversion. Valid fields are name, pipeline_id, pipeline_stage_id, 'monetary_value, and assignee_id. If unspecified, no Opportunity will be created. If pipeline_stage_id is unspecified, it will default to the first stage in the pipeline.
        }

        return self.copper.post('/leads/' + id + '/convert', { **default_body, **body})

    def list(self, body = {}):
        default_body = {
            'page_number': 1,  # number	The page number (starting with 1) that you would like to view.
            'page_size': 20,  # number	The number of entries included in a page of results
            'sort_by': 'name',  # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }

        return self.copper.post('/leads/search', { **default_body, **body})

    def activities(self, id, body = {}):
        default_body = {
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
            'full_result': False, # boolean	(Optional) If set to true, search performance improves but duplicate activity logs may be returned (footnote 3).	false
        }

        return self.copper.post('/leads/' + str(id) + '/activities', {**default_body, **body})

    def customer_sources():
        return self.copper.get('/customer_sources')

    def statuses():
        return self.copper.get('/lead_statuses')
