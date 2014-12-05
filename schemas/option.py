""" Option
    Available options to vote for
"""

from . import identifier
from . import other_name
from . import person
from . import organization

resource = {
    'schema': {
        'id': {
            'type':'string',
             'empty': False,
             'required': True
        },
        'name': {
            'type': 'string',
            'nullable': True
        },
        'identifier': {
            # An issued identifier
            'type': 'string',
            'nullable': True,
        },
        'other_names': {
            # Alternate or former names
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'name': {
                        # An alternate or former name
                        'type': 'string',
                        'required': True,
                        'empty': False,
                    },
                    'note': {
                        # A note, e.g. 'Birth name'
                        'type': 'string',
                        'nullable': True,
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
            'unique_elements': True,
        },
        'type': {
            # person or party/organization
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'person': person.resource['schema'],
        'organization': organization.resource['schema'],
        'other_identifiers': {
            # Alternate or former names
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'identifier': {
                        'type': 'string',
                        'required': True,
                        'empty': False,
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
            'unique_elements': True,
        },
    }
}     
