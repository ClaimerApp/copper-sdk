import requests
from retry import retry
from json import JSONDecodeError
from copper_sdk.users import Users
from copper_sdk.leads import Leads
from copper_sdk.account import Account
from copper_sdk.activities import Activities
from copper_sdk.companies import Companies
from copper_sdk.people import People
from copper_sdk.opportunities import Opportunities
from copper_sdk.customer_sources import CustomerSources
from copper_sdk.loss_reasons import LossReasons
from copper_sdk.custom_field_definitions import CustomFieldDefinitions
from copper_sdk.tags import Tags

BASE_URL = 'https://api.copper.com/developer_api/v1'


class Copper:

    # Constructor - authentication details
    def __init__(self, token, email, base_url=BASE_URL, debug=False, session=None):
        self.token = token
        self.email = email
        self.base_url = base_url
        self.debug = debug

        # init request
        if not session:
            session = requests.Session()

        self.session = session
        self.session.headers = {
            'X-PW-AccessToken': self.token,
            'X-PW-Application': 'developer_api',
            'X-PW-UserEmail': self.email,
            # 'Content-Type': 'application/json',
        }

    def get(self, endpoint):
        return self.api_call('get', endpoint)

    def post(self, endpoint, opts):
        return self.api_call('post', endpoint, opts)

    def put(self, endpoint, opts):
        return self.api_call('put', endpoint, opts)

    def delete(self, endpoint, json_body=None):
        return self.api_call('delete', endpoint, json_body=json_body)

    @retry(JSONDecodeError, delay=1, backoff=2, max_delay=4, tries=3)
    def api_call(self, method, endpoint, json_body=None):
        if self.debug:
            print("json_body:", json_body)

        # dynamically call method to handle status change
        response = self.session.request(method, self.base_url + endpoint, json=json_body)

        if self.debug:
            print(response.text)

        return response.json()

    @property
    def users(self):
        return Users(self)

    @property
    def leads(self):
        return Leads(self)

    @property
    def account(self):
        return Account(self)

    @property
    def activities(self):
        return Activities(self)

    @property
    def opportunities(self):
        return Opportunities(self)

    @property
    def people(self):
        return People(self)

    @property
    def companies(self):
        return Companies(self)

    @property
    def customersources(self):
        return CustomerSources(self)

    @property
    def lossreasons(self):
        return LossReasons(self)

    @property
    def tags(self):
        return Tags(self)

    @property
    def customfielddefinitions(self):
        return CustomFieldDefinitions(self)
