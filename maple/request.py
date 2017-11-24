from maple.utils import get_field_type, is_field_required
from maple.sdk import GraphQLBlock


def get_graphql_request(spec, request_type, fields, params, operation_name="MyRequest"):
    # TODO: This better
    if request_type not in {'query', 'mutation'}:
        raise

    # TODO: Add alias?
    return '''
    {type} {operation}({variables}) {{
        {name}({params}) {{
            {fields}
        }}
    }}
    '''.format(
        type=request_type,
        operation=operation_name,
        variables=build_variables(spec['args'], params),
        name=spec['name'],
        params=build_params(spec['args']),
        fields=build_fields(fields)
    )


def build_variables(args, params):
    argument_types = {
        arg['name']: get_field_type(arg) + ('!' if is_field_required(arg) else '') for arg in args
    }

    return ', '.join(
        "${arg}:{arg_type}".format(arg=arg['name'], arg_type=argument_types[arg['name']])
        for arg in args
    )


def build_params(args):
    return ', '.join(
        "{arg}:${arg}".format(arg=arg['name'])
        for arg in args
    )


def build_fields(fields):
    field_string = ''

    for field in fields:
        if isinstance(field, GraphQLBlock):
            field_string += '\n{}'.format(build_fields(field.fields))
        else:
            field_string += '{}\n'.format(field)

    return field_string
