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

    # User _ in paramater names to avoid name collisions
    def __init__(self, _name, _fields, _alias=None, **_arguments):
        self.name = _name
        self.fields = _fields
        self.alias = _alias
        self.arguments = _arguments
