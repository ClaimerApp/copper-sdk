import vcr
from copper_sdk import Copper, Leads, COPPER_API_TOKEN, COPPER_API_EMAIL

# @vcr.use_cassette('tests/vcr_cassettes/lead-list.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
@vcr.use_cassette('tests/vcr_cassettes/lead-list.yml')
def test_leads_list():
    """Test list leads"""

    copper = Copper(COPPER_API_TOKEN, COPPER_API_EMAIL)
    response = copper.leads().list({
        'page_size': 2,
    })

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert len(response) == 2

def test_leads_crete():
    '''Test creation of leads'''
    pass

def test_leads_update():
    '''Test updating a lead'''
    pass
