class GraphQLSDK(object):

    def __init__(self, schema, query=None, mutation=None):
        self.schema = schema
        self.query = query
        self.mutation = mutation


class TypeInterface(object):

    def __init__(self, client):
        self._client = client


class Query(TypeInterface):
    pass


class Mutation(TypeInterface):
    pass
