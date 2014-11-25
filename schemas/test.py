""" Test
"""

resource = {
    'schema': {
        'id': {
            # The area's unique identifier
            'type': 'string',
            'empty': False,
            'unique': True,
        },
        'name': {
            # A primary name
            'type': 'string',
            'nullable': True,
        },
        'identifier': {
            # An issued identifier
            'type': 'string',
            'nullable': True,
        },
        'parent_ids': {
            'type': 'list',
            'schema': {
                'parent_id': {
                    'type': 'string',
                    'nullable': True,
                    'data_relation': {
                        'resource': 'areas',
                        'field': 'id',
                    }
            }
                },
                'election_id': {
                    'type': 'string',
                    'required': True,
                    'empty': False
                }
        }
    }
}
