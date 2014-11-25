""" Area
	A geographic area whose geometry may change over time
	JSON schema: http://popoloproject.com/schemas/area.json#
"""

from . import link

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
		'classification': {
			# An area category, e.g. city
			'type': 'string',
			'nullable': True,
		},
		'parents': {
	        'type': 'list',
            'schema': {
                'area_id': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'data_relation': {
                        'resource': 'areas',
                        'field': 'id',
                    }
                },
                'election_id': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'data_relation': {
                        'resource': 'elections',
                        'field': 'id',
                    }
                }
            }       
		},
		'geometry': {
			# A geometry
			'nullable': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the area is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	}
}
