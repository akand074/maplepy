from maple.adapters.http import HttpAdapter


class GraphQLSDK(object):

    def __init__(self, schema, query=None, mutation=None):
        self.schema = schema
        self.query = query
        self.mutation = mutation


class HTTPTypeInterface(object):

    def __init__(self, client):

        # Any client provided for this type must support the HttpAdapter interface
        if not isinstance(client, HttpAdapter):
            raise TypeError('Invalid client provided, expected client of type {}'.format(type(HttpAdapter)))

        self._client = client


class Query(HTTPTypeInterface):
    pass


class Mutation(HTTPTypeInterface):
    pass


class GraphQLBlock(object):

    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
