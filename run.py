from eve import Eve

import settings

instance_settings = settings.common
instance_settings.update({'URL_PREFIX': 'ovolby','MONGO_DBNAME': 'ovolby'})

app = Eve(settings=instance_settings)


if __name__ == '__main__':
    app.run()
