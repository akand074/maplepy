from maple.utils import get_field_type, is_field_required


def build_method_help_docs(graphql_type):
    doc = '''
    Name: {name}

    Description: {description}
    {deprecation}

    Arguments:
    {arguments}

    Return
    '''.format(
        name=graphql_type['name'],
        description=graphql_type.get('description') or 'No description available',
        deprecation=build_method_deprecation_warning(graphql_type),
        arguments=build_method_argument_docs(graphql_type.get('args') or [])
    )

    return doc


def build_method_deprecation_warning(graphql_type):
    return '''
    Deprecated: {is_deprecated}
    Deprecation reason: {reason}
    '''.strip().format(
        is_deprecated=graphql_type.get('isDeprecated') or False,
        reason=graphql_type.get('deprecationReason') or 'No reason available'
    )


def build_method_argument_docs(type_args):
    if not len(type_args):
        return 'No arguments available'

    arg_docs = []
    for ta in type_args:
        arg_doc = '''
        Name: {name}
        - Description: {description}
        - Type: {type}
        - Required: {required}
        '''.rstrip().format(
            name=ta['name'],
            description=ta.get('description') or 'No description',
            type=get_field_type(ta),
            required=is_field_required(ta)
        )
        arg_docs.append(arg_doc)

    return '\n'.join(arg_docs)
