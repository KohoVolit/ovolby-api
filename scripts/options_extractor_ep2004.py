import xmltodict
import slugify
import api
import common_functions as cf

election_id = 'europarl.europa.eu-cz-2004'
path = '../data/EP2004reg/'

with open(path + "eprkl_utf8.xml") as fd:
        obj = xmltodict.parse(fd.read())

parties = []
for item in obj['EP_RKL']['EP_RKL_ROW']:
    option = {
        'id': slugify.slugify(item['NAZEVCELK']),
        'identifier': item['VSTRANA'],
        'name': item['NAZEVCELK'],
        'type': 'organization',
        'other_names': [
            {
                'name': item['NAZEV_STRE'],
                'note': 'short_name_60'
            },
            {
                'name': item['ZKRATKAE30'],
                'note': 'short_name_30'
            },
            {
                'name': item['ZKRATKAE8'],
                'note': 'abbreviation'        
            }
        ]
    }
    cf.post_if_not_exist("options", option, {"id": option['id']})

    identifier = {
        'identifier': item['ESTRANA'],
        'election_id': 'europarl.europa.eu-cz-2004'
    }
    cf.put_property_if_not_exist("options", option, {"id": option['id']}, 'other_identifiers', identifier)
