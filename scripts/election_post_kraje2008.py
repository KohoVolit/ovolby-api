import api
import common_functions as cf
import csv
 

# ORGANIZATIONS
organization = {
    "id": "cz-kraje",
    "name": "Krajská zastupitelstva",
    "classification": "provincial assemblies",
}
cf.post_if_not_exist("organizations", organization, {"id": organization['id']})

provinces = []
with open("../data/kz2008_data_dbf/kraje.csv") as infile:
    csvr = csv.reader(infile)
    for row in csvr:
        provinces.append(row)

for province in provinces:
    organization = {
        "id": province[0],
        "name": "Zastupitelstvo - " + province[1],
        "classification": "provincial assembly",
    }
    cf.post_if_not_exist("organizations", organization, {"id": organization['id']})

# ELECTION
election = {
    "id": "cz-kraje-2008",
    "name": "Volby do krajských zastupitelstev 2008",
    "organization_id": "cz-kraje",
    "start_date": "2004-10-12 15:00",
    "end_date": "2004-10-13 14:00"
}
cf.post_if_not_exist("elections", election, {"id": election['id']})

for province in provinces:
    election = {
        "id": "cz-kraje-" + province[0] + "-2008",
        "name": "Volby do krajského zastupitelstva 2008 - " + province[1],
        "organization_id": province[0],
        "start_date": "2004-10-12 15:00",
        "end_date": "2004-10-13 14:00",
        "number_of_posts": int(province[2]),
        "parent_id": "cz-kraje-2008"
    }
    cf.post_if_not_exist("elections", election, {"id": election['id']})


# AREAS
area = {
    'id': 'cz-kraje',
    'name': 'Kraje ČR',
    'classification': 'provinces'
}
cf.post_if_not_exist("areas", area, {"id": area['id']})

#area = {
#    'id': 'cz',
#    'name': 'Česká republika',
#    'classification': 'country'
#}
#cf.post_if_not_exist("areas", area, {"id": area['id']})
#parent = {
#    'area_id': 'eu',
#    'election_id': "europarl.europa.eu-cz-2004"
#}
#cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)

# ORGANIZATION 2nd
organization = {
    "id": "cz-kraje",
    "name": "Krajská zastupitelstva",
    "classification": "regional assemblies",
}
area = {
    "area_id": "cz-kraje",
    "election_id": "cz-kraje-2008"
}
cf.put_property_if_not_exist("organizations", organization, {"id": organization['id']}, 'areas', area)

for province in provinces:
    organization = {
        "id": province[0],
        "name": "Zastupitelstvo - " + province[1],
        "classification": "provincial assembly",
    }
    area = {
        "area_id": province[0],
        "election_id": "cz-kraje-" + province[0] + "-2008"
    }
    cf.put_property_if_not_exist("organizations", organization, {"id": organization['id']}, 'areas', area)




