import requests, json
from .leads import Leads
from .activities import Activities

class Copper():
    # Constructor - authentication details
    def __init__(self, token, email, base_url = 'https://api.prosperworks.com/developer_api/v1'):
        self.token = token
        self.email = email
        self.base_url = base_url

        # init request
        self.session = requests.Session()
        self.session.headers = {}
        self.session.headers['X-PW-AccessToken'] = self.token
        self.session.headers['X-PW-Application'] = 'developer_api'
        self.session.headers['X-PW-UserEmail'] = self.email
        self.session.headers['Content-Type'] = 'application/json'

    def get(self, endpoint, opts):
        return self.api_call('get', endpoint, opts)

    def post(self, endpoint, opts):
        return self.api_call('post', endpoint, opts)

    def api_call(self, method, endpoint, opts):

        # dynamically call method to handle status change
        response = getattr(self.session, method)(self.base_url + endpoint, data=json.dumps(opts))

        return json.loads(response.text)

    def leads(self):
        return Leads(self)

    def activities(self):
        return Activities(self)
