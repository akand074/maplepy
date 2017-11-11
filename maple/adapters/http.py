
class HttpAdapter(object):

    def schema(self, schema):
        raise NotImplementedError()

    def query(self, query_string, params):
        raise NotImplementedError()

    def mutation(self, mutate_string, params):
        raise NotImplementedError()

    def execute(self, query, variables={}):
        raise NotImplementedError()
