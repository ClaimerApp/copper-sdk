import vcr, requests
from copper_sdk import copper

def test_init():
    # create own request object to test against
    session = requests.Session()

    # test init arguments
    test_args = {
        'token': 'test-token-144ec4kfew4559c1231233ifewfew',
        'email': 'foobarbaz@foobarbaz.io',
        'base_url': 'https://example-base.url',
        'session': session,
    }

    # init
    obj = copper.Copper(
        token=test_args['token'],
        email=test_args['email'],
        base_url=test_args['base_url'],
        session=test_args['session'],
    )

    # test!
    assert isinstance(session, requests.sessions.Session)

    # ensure required keys exist
    assert all(elem in list(session.headers.keys()) for elem in ['X-PW-AccessToken', 'X-PW-Application', 'X-PW-UserEmail', 'Content-Type'])

    # ensure key values are correct
    assert session.headers['X-PW-AccessToken'] == test_args['token']
    assert session.headers['X-PW-Application'] == 'developer_api'
    assert session.headers['X-PW-UserEmail'] == test_args['email']
    assert session.headers['Content-Type'] == 'application/json'

@vcr.use_cassette('tests/vcr_cassettes/core-tests-get.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
def test_get(copper):
    # test typical endpoint
    response = copper.get('/contact_types')

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert len(response) == 5

@vcr.use_cassette('tests/vcr_cassettes/core-tests-post.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
def test_post(copper):
    # test typical endpoint
    response = copper.post('/people/search', {
        'page_size': 10,
    })

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert len(response) == 10


# # endpoints
# endpointslist = [
#     { 'category': 'users', 'endpoint': 'search' },
#     { 'category': 'leads', 'endpoint': 'search' },
#     { 'category': 'leads', 'endpoint': 'customer_sources' },
#     { 'category': 'leads', 'endpoint': 'lead_statuses' },
# ]
#
# @vcr.use_cassette('tests/vcr_cassettes/test-list.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
# def test_leads_list(copper):
#     """Test list endpoints"""
#     response = copper.leads().list({
#         'page_size': 2,
#     })
#
#     assert isinstance(response, list)
#     assert isinstance(response[0], dict)
#     assert len(response) == 2
#
# def test_leads_crete():
#     '''Test creation of leads'''
#     pass
#
# def test_leads_update():
#     '''Test updating a lead'''
#     pass
#
# @vcr.use_cassette('tests/vcr_cassettes/leads-activities.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
# def test_leads_activities(copper):
#     '''Test getting activities from a lead'''
#
#     # get a lead id
#     response = copper.leads().list({
#         'page_size': 1,
#     })
#     lead_id = response[0]['id']
#
#     # get activity for the lead
#     response = copper.leads().activities(lead_id)
#
#     assert isinstance(response, list)
#
#     # Cannot guarentee a result
#     # assert isinstance(response[0], dict)
#     # assert len(response) == 1
