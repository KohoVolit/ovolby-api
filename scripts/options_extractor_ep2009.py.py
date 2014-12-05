import xmltodict
import slugify
import api
import common_functions as cf

election_id = 'europarl.europa.eu-cz-2009'
path = '../data/EP2009reg/'

with open(path + "eprkl_utf8.xml") as fd:
        obj = xmltodict.parse(fd.read())

parties = []
for item in obj['EP_RKL']['EP_RKL_ROW']:
    option = {
        'id': slugify.slugify(item['NAZEVCELK']),
        'identifier': item['VSTRANA'],
        'name': item['NAZEVCELK'],
        'type': 'organization',
    }
    cf.post_if_not_exist("options", option, {"identifier": option['identifier']})

    other_names = [
            {
                'name': item['NAZEV_STRE'],
                'note': 'short_name_60',
                'election_id': election_id
            },
            {
                'name': item['ZKRATKAE30'],
                'note': 'short_name_30',
                'election_id': election_id
            },
            {
                'name': item['ZKRATKAE8'],
                'note': 'abbreviation',
                'election_id': election_id    
            }
        ]
    for other_name in other_names:
        cf.put_property_if_not_exist("options", option, {"identifier": option['identifier']}, 'other_names', other_name) 

    identifier = {
        'identifier': item['ESTRANA'],
        'election_id': election_id
    }
    cf.put_property_if_not_exist("options", option, {"identifier": option['identifier']}, 'other_identifiers', identifier)
