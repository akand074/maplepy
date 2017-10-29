class GraphQLSDK(object):

    def __init__(self, query, mutate, subscribe):
        self.query = query
        self.mutate = mutate
        self.subscribe = subscribe


class TypeInterface(object):

    def __init__(self, client):
        self.client = client


class Query(TypeInterface):
    pass


class Mutate(TypeInterface):
    pass


class Subscribe(TypeInterface):
    pass
