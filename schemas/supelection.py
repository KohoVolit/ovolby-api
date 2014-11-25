""" Supelection
	A group of elections to the same organizations (same classification) at the same time
	e.g., local elections in a country
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
    }
}
