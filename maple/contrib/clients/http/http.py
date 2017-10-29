import requests

from maple.adapters.http import HttpAdapter


class HTTPClient(HttpAdapter):

    def __init__(self, graphql_url, session=None, extra_headers={}):
        self.graphql_url = graphql_url
        self.session = session or requests.Session()
        self.session.headers.update(extra_headers)

    def schema(self, schema):
        # TODO: handle data/errors in body somehow?
        return self.execute(schema)['data']

    def query(self, query_string, params):
        raise NotImplementedError()

    def mutate(self, mutate_string, params):
        raise NotImplementedError()

    def execute(self, query, variables={}):
        params = {
            'query': query,
            'variables': variables
        }

        # TODO: Handle error codes?
        return self.session.post(self.graphql_url, json=params).json()
