import api
import common_functions as cf
import csv
 

# ORGANIZATIONS
organization = {
    "id": "psp.cz",
    "name": "Poslanecká sněmovna Parlamentu ČR",
    "classification": "lower house",
}
cf.post_if_not_exist("organizations", organization, {"id": organization['id']})

provinces = []
with open("../data/ps2013_dbf_20131026/kraje.csv") as infile:
    csvr = csv.reader(infile)
    for row in csvr:
        provinces.append(row)

for province in provinces:
    organization = {
        "id": "psp.cz-"+province[0],
        "name": "Poslanecká sněmovna Parlamentu ČR - " + province[1],
        "classification": "part of lower house",
    }
    cf.post_if_not_exist("organizations", organization, {"id": organization['id']})

# ELECTION
election = {
    "id": "psp.cz-2013",
    "name": "Volby do Poslanecké sněmovny 2013",
    "organization_id": "psp.cz",
    "start_date": "2004-10-25 15:00",
    "end_date": "2004-10-26 14:00"
}
cf.post_if_not_exist("elections", election, {"id": election['id']})

for province in provinces:
    election = {
        "id": "psp.cz-" + province[0] + "-2013",
        "name": "Volby do Poslanecké sněmovny 2013 - " + province[1],
        "organization_id": 'psp.cz-'+province[0],
        "start_date": "2004-10-25 15:00",
        "end_date": "2004-10-26 14:00",
        "number_of_posts": int(province[2]),
        "parent_id": "psp.cz-2013"
    }
    cf.post_if_not_exist("elections", election, {"id": election['id']})


# AREAS
area = {
    'id': 'cz',
    'name': 'Česká republika',
    'classification': 'country'
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
    "id": "psp.cz",
    "name": "Poslanecká sněmovna Parlamentu ČR",
    "classification": "lower house",
}
area = {
    "area_id": "psp.cz",
    "election_id": "psp.cz-2013"
}
cf.put_property_if_not_exist("organizations", organization, {"id": organization['id']}, 'areas', area)

for province in provinces:
    organization = {
        "id": "psp.cz-"+province[0],
        "name": "Poslanecká sněmovna Parlamentu ČR - " + province[1],
        "classification": "part of lower house",
    }
    area = {
        "area_id": province[0],
        "election_id": "psp.cz-" + province[0] + "-2013"
    }
    cf.put_property_if_not_exist("organizations", organization, {"id": organization['id']}, 'areas', area)




