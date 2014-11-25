import api
import common_functions as cf
 

# ORGANIZATIONS
organization = {
    "id": "europarl.europa.eu",
    "name": "Evropský parlament",
    "classification": "supranational parliament",
}
cf.post_if_not_exist("organizations", organization, {"id": organization['id']})

organization = {
    "id": "europarl.europa.eu-cz",
    "name": "Evropský parlament, ČR",
    "classification": "part of supranational parliament",
}
cf.post_if_not_exist("organizations", organization, {"id": organization['id']})

# ELECTION
election = {
    "id": "europarl.europa.eu-2004",
    "name": "Volby do Evropského parlamentu 2004",
    "organization_id": "europarl.europa.eu",
    "start_date": "2004-06-10",
    "end_date": "2004-06-13 23:59"
}
cf.post_if_not_exist("elections", election, {"id": election['id']})

election = {
    "id": "europarl.europa.eu-cz-2004",
    "name": "Volby do Evropského parlamentu 2004 v České republice",
    "organization_id": "europarl.europa.eu-cz",
    "start_date": "2004-06-11 15:00",
    "end_date": "2004-06-12 14:00",
    "number_of_posts": 24,
    "parent_id": "europarl.europa.eu-2004"
}
cf.post_if_not_exist("elections", election, {"id": election['id']})


# AREAS
area = {
    'id': 'eu',
    'name': 'Evropská unie',
    'classification': 'union'
}
cf.post_if_not_exist("areas", area, {"id": area['id']})

area = {
    'id': 'cz',
    'name': 'Česká republika',
    'classification': 'country'
}
cf.post_if_not_exist("areas", area, {"id": area['id']})
parent = {
    'area_id': 'eu',
    'election_id': "europarl.europa.eu-cz-2004"
}
cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)

# ORGANIZATION 2nd
organization = {
    "id": "europarl.europa.eu",
    "name": "Evropský parlament",
    "classification": "supranational parliament",
}
area = {
    "area_id": "eu",
    "election_id": "europarl.europa.eu-cz-2004"
}
cf.put_property_if_not_exist("organizations", organization, {"id": organization['id']}, 'areas', area)

organization = {
    "id": "europarl.europa.eu-cz",
    "name": "Evropský parlament, ČR",
    "classification": "part of supranational parliament",
}
area = {
    "area_id": "cz",
    "election_id": "europarl.europa.eu-cz-2004"
}
cf.put_property_if_not_exist("organizations", organization, {"id": organization['id']}, 'areas', area)




