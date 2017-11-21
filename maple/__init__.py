import pkg_resources

from maple.generator import generate_graphql_sdk
from maple.sdk import GraphQLBlock


__version__ = pkg_resources.get_distribution('maple').version
__all__ = [
    'generate_graphql_sdk',
    'GraphQLBlock'
]
