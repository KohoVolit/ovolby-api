from eve import Eve

import settings

def create_app(conf):
	# Merge parliament specific settings on top of common settings.
	instance_settings = settings.common
	instance_settings.update({'URL_PREFIX': 'ovolby','MONGO_DBNAME': 'ovolby'})
#	instance_settings.update({
#		'URL_PREFIX': parliament,
#		'MONGO_DBNAME': parliament.replace('/', '_').replace('-', '_'),
#		'AUTHORIZED_USERS': conf['authorized_users'],
#	})

	app = Eve(
		settings=instance_settings#,
		#validator=VpapiValidator,
		#auth=VpapiBasicAuth
	)

	return app


if __name__ == '__main__':
    app = create_app({'authorized_users': [['admin', 'secret']]})
    app.run()
