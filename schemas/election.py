""" Election
	A single election
"""

resource = {
    'schema': {
        'id': {
            'type':'string',
             'unique': True,
             'empty': False,
             'required': True
        },
        'name': {
            'type': 'string',
            'nullable': True
        },
        'organization_id':  {
            'type': 'string',
            'data_relation': {
                'resource': 'organizations',
                'field': 'id'
            }
        },
	    'start_date': {
            # The time at which the event begins
            'type': 'string',
            'format': 'partialdate',
            'nullable': True,
        },
	    'end_date': {
            # The time at which the event begins
            'type': 'string',
            'format': 'partialdate',
            'nullable': True,
        },
        'number_of_posts': {
            'type': 'number'
        },
        'parent_id': {
           'type': 'string',
            'data_relation': {
                'resource': 'elections',
                'field': 'id'
            } 
        }
    }
}
