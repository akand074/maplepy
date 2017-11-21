class GraphQLSDK(object):

    def __init__(self, schema, query=None, mutation=None):
        self.schema = schema
        self.query = query
        self.mutation = mutation


class HTTPTypeInterface(object):

    def __init__(self, client):
        # TODO: Error if not of type http adapter
        self._client = client


class Query(HTTPTypeInterface):
    pass


class Mutation(HTTPTypeInterface):
    pass


class GraphQLBlock(object):

    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
