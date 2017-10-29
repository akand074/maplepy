from maple.sdk import GraphQLSDK, Query, Mutate, Subscribe
from maple.introspection import INTROSPECTION_QUERY
from maple.contrib.clients.http.http import HTTPClient


def generate_graphql_sdk(graphql_url, http_adapter=HTTPClient, extra_headers={}):
    http_client = http_adapter(graphql_url, extra_headers=extra_headers)

    schema = http_client.schema(INTROSPECTION_QUERY)['__schema']

    mutation_type_name = schema["mutationType"]["name"]
    query_type_name = schema["queryType"]["name"]
    subscription_type_name = schema["subscriptionType"]["name"]

    query = Query(http_client)
    mutate = Mutate(http_client)

    for graphql_type in schema['types']:
        type_name = graphql_type['name']

        if type_name == query_type_name:
            # TODO: Build queries from schema
            pass
        elif type_name == mutation_type_name:
            # TODO: Build mutations from schema
            pass
        elif type_name == subscription_type_name:
            # TODO: Build subscriptions from schema
            pass

    return schema
