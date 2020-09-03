import requests, json
from .users import Users
from .leads import Leads
from .activities import Activities
from .companies import Companies
from .people import People
from .opportunities import Opportunities
from .customer_sources import CustomerSources
from .loss_reasons import LossReasons

class Copper():
    # Constructor - authentication details
    def __init__(self, token, email, base_url = 'https://api.prosperworks.com/developer_api/v1', debug = False, session = None):
        self.token = token
        self.email = email
        self.base_url = base_url
        self.debug = debug

        # init request
        if not session:
            session = requests.Session()

        self.session = session
        self.session.headers = {}
        self.session.headers['X-PW-AccessToken'] = self.token
        self.session.headers['X-PW-Application'] = 'developer_api'
        self.session.headers['X-PW-UserEmail'] = self.email
        self.session.headers['Content-Type'] = 'application/json'

    def get(self, endpoint):
        return self.api_call('get', endpoint)

    def post(self, endpoint, opts):
        return self.api_call('post', endpoint, opts)

    def put(self, endpoint, opts):
        return self.api_call('put', endpoint, opts)

    def delete(self, endpoint):
        return self.api_call('delete', endpoint)

    def api_call(self, method, endpoint, opts = None):
        optsJson = None
        if opts:
            optsJson = json.dumps(opts)
            if self.debug:
              print(optsJson)

        # dynamically call method to handle status change
        response = getattr(self.session, method)(self.base_url + endpoint, data=optsJson)

        if self.debug:
          print(response.text)

        return json.loads(response.text)

    def users(self):
        return Users(self)

    def leads(self):
        return Leads(self)

    def activities(self):
        return Activities(self)

    def opportunities(self):
        return Opportunities(self)

    def people(self):
        return People(self)

    def companies(self):
        return Companies(self)

    def customersources(self):
        return CustomerSources(self)

    def lossreasons(self):
        return LossReasons(self)
