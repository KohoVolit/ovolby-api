from schemas import organization, area, election, supelection, result, person, option, test

# Common settings for all applications corresponding to individual parliaments
common = {
	'DEBUG': True,

	'MONGO_HOST': 'localhost',
	'MONGO_PORT': 27017,
	'MONGO_QUERY_BLACKLIST': ['$where'],	# allows $regex operator in queries
	
	'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
	'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
	'PUBLIC_METHODS': ['GET'],
	'PUBLIC_ITEM_METHODS': ['GET'],

	'IF_MATCH': False,

	'DATE_FORMAT': '%Y-%m-%d %H:%M:%S',

	'CACHE_CONTROL': 'public, max-age=300',
	'CACHE_EXPIRES': 300,

    'DOMAIN': {
      'organizations': organization.resource,
      'areas': area.resource,
      'elections': election.resource,
      'results': result.resource,
      'options': option.resource,
      
      'test': test.resource
    }

}
