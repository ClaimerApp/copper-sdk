# Copper CRM SDK

Unofficial Copper CRM SDK written in Python

## Official API docs

[https://developer.copper.com/?version=latest#intro](https://developer.copper.com/?version=latest#intro)

## Running the test
```
# install depds
$ pipenv install
# enter shell
$ pipenv shell
# run tests
$ COPPER_API_TOKEN='<my copper token>' COPPER_API_EMAIL='<my copper email>' pytest
```

To force the API to make actual calls, delete the cached responses in the tests/vcr_cassettes directory.
