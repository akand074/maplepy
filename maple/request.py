from maple.utils import get_field_type, is_field_required
from maple.sdk import GraphQLBlock


def get_graphql_request(spec, request_type, fields, params, operation_name=None, alias=None):
    VALID_TYPES = {'query', 'mutation'}
    if request_type not in VALID_TYPES:
        raise TypeError('Invalid request type {request_type}, must be one of {valid_types}'.format(
            request_type=request_type,
            valid_types=', '.join(VALID_TYPES)
        ))

    return '''
    {type} {operation_name} {{
        {operation}
    }}
    '''.format(
        type=request_type,
        operation_name=operation_name or 'MyRequest',
        operation=build_operation(spec['name'], params, fields, alias)
    )


def build_operation(name, params, fields, alias):
    return '''
    {alias}{name}{params} {{
        {fields}
    }}
    '''.format(
        alias='{}:'.format(alias) if alias else '',
        name=name,
        params=build_params(params),
        fields=build_fields(fields)
    )


def build_params(params):
    if not params:
        return ''

    generated_params = ', '.join(
        "{name}:{value}".format(name=name, value=value)
        for name, value in params.items()
    )

    return '({})'.format(generated_params)


def build_fields(fields):
    field_string = ''

    for field in fields:
        if isinstance(field, GraphQLBlock):
            field_string += '\n{}'.format(build_operation(field.name, field.arguments, field.fields, field.alias))
        else:
            field_string += '{}\n'.format(field)

    return field_string
