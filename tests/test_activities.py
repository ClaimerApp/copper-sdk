import vcr
from copper_sdk.activities import Activities

@vcr.use_cassette('tests/vcr_cassettes/activities-list.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
def test_activities_list(copper):
    '''Test list activities'''
    response = copper.activities().list({
        'page_size': 10,
    })

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert len(response) == 10

# @vcr.use_cassette('tests/vcr_cassettes/lead-activities.yml', filter_headers=['X-PW-AccessToken', 'X-PW-UserEmail'])
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
