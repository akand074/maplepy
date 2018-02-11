import requests

from maple.adapters.http import HttpAdapter


class HTTPClient(HttpAdapter):

    def __init__(self, graphql_url, session=None, headers={}):
        self.graphql_url = graphql_url
        self.session = session or requests.Session()
        self.session.headers.update(headers)

    def schema(self, schema):
        return self.execute(schema)['data']

    def query(self, query_string, params):
        return self.execute(query_string, params)

    def mutation(self, mutate_string, params):
        return self.execute(mutate_string, params)

    def execute(self, query, variables={}):
        params = {
            'query': query,
            'variables': variables
        }

        response = self.session.post(self.graphql_url, json=params)

        # Always expecting a 2xx status code
        response.raise_for_status()

        return response.json()
