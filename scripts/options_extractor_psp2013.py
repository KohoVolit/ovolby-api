import xmltodict
import slugify
import api
import common_functions as cf


path = '../data/ps2013_dbf_20131026/'

provinces = []
with open(path+"kraje.csv") as infile:
    csvr = csv.reader(infile)
    for row in csvr:
        provinces.append(row)

li = []
with open(path + "PSRKL_utf8.csv") as fd:
    csvr = csv.reader(fd)
    i = 0
    for row in csvr:
        if i > 0:
            li.append(row)
        i = i + 1

parties = []
for province in provinces:
    for item in li:
        option = {
            'id': slugify.slugify(item[2]),
            'identifier': item[1],
            'name': item[2],
            'type': 'organization'
        }
        cf.post_if_not_exist("options", option, {"identifier": option['identifier']})


        other_names = [
            {
                'name': item[3],
                'note': 'short_name_60',
                'election_id': 'psp.cz-'+province[0]+'-2013'
            },
            {
                'name': item[4],
                'note': 'short_name_30',
                'election_id': 'psp.cz-'+province[0]+'-2013'
            },
            {
                'name': item[5],
                'note': 'abbreviation',
                'election_id': 'psp.cz-'+province[0]+'-2013'
            }
        ]
        for other_name in other_names:
            cf.put_property_if_not_exist("options", option, {"identifier": option['identifier']}, 'other_names', other_name) 
        

        identifier = {
            'identifier': item[0],
            'election_id': 'psp.cz-'+province[0]+'-2013'
        }
        cf.put_property_if_not_exist("options", option, {"identifier": option['identifier']}, 'other_identifiers', identifier)

