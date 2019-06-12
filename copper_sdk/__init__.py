import os
import requests

COPPER_API_TOKEN = os.environ.get('COPPER_API_TOKEN', None)
COPPER_API_EMAIL = os.environ.get('COPPER_API_EMAIL', None)

class APIDetailsMissingError(Exception):
    pass

if COPPER_API_TOKEN is None or COPPER_API_EMAIL is None:
    raise APIDetailsMissingError(
        "All methods require an API email and token set in environment vars: "
        "COPPER_API_EMAIL and COPPER_API_TOKEN. "
        "See https://developer.copper.com/?version=latest#intro "
        "for how to retrieve an authentication token from your copper account."
    )
