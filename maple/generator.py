import types

from maple.sdk import GraphQLSDK, Query, Mutate, Subscribe
from maple.introspection import INTROSPECTION_QUERY
from maple.utils import get_required_params
from maple.docs import build_method_help_docs
from maple.contrib.clients.http.http import HTTPClient


def generate_graphql_sdk(graphql_url, http_adapter=HTTPClient, extra_headers={}):
    http_client = http_adapter(graphql_url, extra_headers=extra_headers)

    schema = http_client.schema(INTROSPECTION_QUERY)['__schema']

    mutation_type_name = schema["mutationType"]["name"]
    query_type_name = schema["queryType"]["name"]
    # TODO: Check of the type exists
    # subscription_type_name = schema["subscriptionType"]["name"]

    query = Query(http_client)
    mutate = Mutate(http_client)

    for graphql_type in schema['types']:
        type_name = graphql_type['name']

        if type_name == query_type_name:
            # TODO: Build queries from schema
            map(lambda f: generate_query_method(query, f), graphql_type['fields'])
        elif type_name == mutation_type_name:
            # TODO: Build mutations from schema
            pass

    return query


def generate_query_method(query, query_field):
    field_name = query_field['name']
    required_params = get_required_params(query_field.get('args', []))
    method_docs = build_method_help_docs(query_field)

    # TODO: Add deprecation warnings

    def query_method(self, query_string, **kwargs):

        # Make sure all required params are sent in
        for rp in required_params:
            if not rp in kwargs:
                raise TypeError("Missing required keyword paramater {}".format(rp))

        # How to build query_string? force them to send it in? always pull all the fields? or expect tuple of fields? Maybe build gql type
        # Leaning on taking in tuple of fields and auto-generating query
        return self.client.query(query_string, kwargs)

    query_method.__doc__ = method_docs

    method = types.MethodType(query_method, query, Query)
    setattr(query, field_name, method)
