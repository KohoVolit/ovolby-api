""" Result
	Result of a single elections in one area
"""

resource = {
    'schema': {
        'election_id': {
            'type': 'string',
            'required': True,
            'empty': False,
            'data_relation': {
                'resource': 'elections',
                'field':'id'
             }
         },
        'area_id': {
            'type': 'string',
            'required': True,
            'empty': False,
            'data_relation': {
                'resource': 'areas',
                'field':'id'
            }
        },
        'area_classification': {
            'type': 'string'
        },
        'summary': {
            'type': 'list',
            'schema': {
                'name': {
                    'type': 'string',
                    'required': True,
                    'empty': False
                },
                'value': {
                    'type': 'number',
                    'required': True,
                    'empty': False
                }
            }
        },
        'counts': {
            'type': 'list',
            'schema': {
                'option_id': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'data_relation': {
                        'resource': 'options',
                        'field':'id'
                    }
                },
                'votes': {
                    'type': 'integer'
                },
                'representatives': {
                    'type': 'integer'
                }
            }
        }
    }
}
