import types

from maple.sdk import GraphQLSDK, Query, Mutation
from maple.introspection import INTROSPECTION_QUERY
from maple.utils import get_required_params
from maple.request import get_graphql_request
from maple.docs import build_method_help_docs
from maple.contrib.clients.http.http import HTTPClient


def generate_graphql_sdk(graphql_url, http_adapter=HTTPClient, http_headers={}):
    http_client = http_adapter(graphql_url, headers=http_headers)

    schema = http_client.schema(INTROSPECTION_QUERY)['__schema']

    mutation_type_name = schema['mutationType']['name'] if schema.get('mutationType') else None
    query_type_name = schema['queryType']['name'] if schema.get('queryType') else None

    query = Query(http_client)
    mutation = Mutation(http_client)

    for graphql_type in schema['types']:
        type_name = graphql_type['name']

        if query_type_name and type_name == query_type_name:
            map(lambda f: generate_type_method(query, f, 'query', Query), graphql_type['fields'])
        elif mutation_type_name and type_name == mutation_type_name:
            map(lambda f: generate_type_method(mutation, f, 'mutation', Mutation), graphql_type['fields'])

    sdk = GraphQLSDK(schema, query=query, mutation=mutation)

    return sdk


def generate_type_method(instance, field, action, obj_type):
    field_name = field['name']
    required_params = get_required_params(field.get('args', []))
    method_docs = build_method_help_docs(field)

    # TODO: Add deprecation warnings

    def field_method(self, fields, **variables):

        # Make sure all required params are sent in
        for rp in required_params:
            if rp not in variables:
                raise TypeError("Missing required keyword paramater {}".format(rp))

        query_string = get_graphql_request(field, action, fields, variables)
        return getattr(self._client, action)(query_string, variables)

    field_method.__doc__ = method_docs
    field_method.__name__ = str(field_name)

    method = types.MethodType(field_method, instance, obj_type)
    setattr(instance, field_name, method)
