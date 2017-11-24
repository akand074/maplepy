
def get_required_params(params):
    return [
        p['name'] for p in params if is_field_required(p)
    ]


def get_field_type(field):
    if field['type'].get('ofType'):
        return field['type']['ofType']['name']

    return field['type']['name']


def is_field_required(field):
    return field.get('type', {}).get('kind') == 'NON_NULL'
