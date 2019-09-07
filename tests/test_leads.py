import vcr
from copper_sdk.leads import Leads

@vcr.use_cassette('tests/vcr_cassettes/leads-list.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
def test_leads_list(copper):
    '''Test list leads'''
    response = copper.leads().list({
        'page_size': 2,
    })

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert len(response) == 2

def test_leads_create():
    '''Test creation of leads'''
    pass

def test_leads_update():
    '''Test updating a lead'''
    pass

# @vcr.use_cassette('tests/vcr_cassettes/leads-activities.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
def test_leads_activities(copper):
    '''Test getting activities from a lead'''

    # get all activity and grab the first lead
    response = copper.activities().list({
        'page_size': 1,
    })

    print(response)

    # get a lead id
    # response = copper.leads().list({
    #     'page_size': 1,
    # })
    # lead_id = response[0]['id']
    #
    # # get activity for the lead
    # response = copper.leads().activities(lead_id)

    assert False
    # assert isinstance(response, list)

    # Cannot guarentee a result
    # assert isinstance(response[0], dict)
    # assert len(response) == 1
