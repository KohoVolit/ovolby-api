  'results': {
    'schema': {
      'election_id': {'type': 'string','required': True,'empty': False,'required': True,'data_relation': {'resource': 'elections','field':'id'}},
      'area_id': {'type': 'string','required': True,'empty': False,'required': True,'data_relation': {'resource': 'areas','field':'id'}},
      'summary': {
        'type': 'dict',
        'schema': {
          'eligibles':{'type': 'integer'},
          'attendees':{'type': 'integer'},
          'all_ballots':{'type': 'integer'},
          'valid_votes':{'type': 'integer'}
        }
      },
      'counts': {
        'type': 'list',
        'schema': {
          'option': {'type': 'string'},
          'votes': {'type': 'integer'},
          'representatives': {'type': 'integer'}
        }
      }
    }
  }
