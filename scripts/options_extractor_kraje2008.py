import xmltodict
import slugify
import api
import common_functions as cf

#election_id = 'cz-kraje-2008'
path = '../data/kz2008_data_dbf/'

provinces = []
with open(path+"kraje.csv") as infile:
    csvr = csv.reader(infile)
    for row in csvr:
        provinces.append(row)

li = []
with open(path + "KZRKL_utf8.csv") as fd:
    csvr = csv.reader(fd)
    i = 0
    for row in csvr:
        if i > 0:
            li.append(row)
        i = i + 1

parties = []
for item in li:
    option = {
        'id': slugify.slugify(item[3]),
        'identifier': item[2],
        'name': item[3],
        'type': 'organization'
    }
    cf.post_if_not_exist("options", option, {"identifier": option['identifier']})


    other_names = [
        {
            'name': item[4],
            'note': 'short_name_60',
            'election_id': 'cz-kraje-'+provinces[int(item[0])-1][0]+'-2008'
        },
        {
            'name': item[5],
            'note': 'short_name_30',
            'election_id': 'cz-kraje-'+provinces[int(item[0])-1][0]+'-2008'
        },
        {
            'name': item[6],
            'note': 'abbreviation',
            'election_id': 'cz-kraje-'+provinces[int(item[0])-1][0]+'-2008'
        }
    ]
    for other_name in other_names:
        cf.put_property_if_not_exist("options", option, {"identifier": option['identifier']}, 'other_names', other_name) 
    

    identifier = {
        'identifier': item[1],
        'election_id': 'cz-kraje-'+provinces[int(item[0])-1][0]+'-2008'
    }
    cf.put_property_if_not_exist("options", option, {"identifier": option['identifier']}, 'other_identifiers', identifier)

