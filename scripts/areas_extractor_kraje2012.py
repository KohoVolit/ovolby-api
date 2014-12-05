import xmltodict
import api
import common_functions as cf

#election_id = 'cz-kraje-2012'
path = '../data/ciselniky20121010/'

nuts = []
with open(path + "CNUMNUTS_utf8.csv") as fd:
    csvr = csv.reader(fd)
    i = 0
    for row in csvr:
        if i > 0:
            nuts.append(row)
        i = i + 1
towns = []
with open(path + "KZCOCO_utf8.csv") as fd:
    csvr = csv.reader(fd)
    i = 0
    for row in csvr:
        if i > 0:
            towns.append(row)
        i = i + 1

def special_towns(okres, obec):
    if okres in ['1100','6202','8106','3203']:
        if int(obec) not in [500291,506711,510882,554049, 568449,569119,569500,598739,598798, 598836,598879,599549, 539741, 540561, 540641, 553590, 557846, 558001, 558141, 558371, 558427, 558460, 558851, 558966, 559130, 578606]:
            special = {
                '1100': {'id':'554782','name':'Praha'},
                '6202': {'id':'582786','name':'Brno'},
                '8106': {'id':'554821','name':'Ostrava'},
                '3203': {'id':'554791','name':'Plzeň'}
            }
            return special[okres]
    return False

id2nuts = {}
for row in nuts:
    id2nuts[row[0]] = row

for row in towns:
    election_id = 'cz-kraje-'+row[0]+'-2012'
    #provinces
    area = {
        'id': row[0],
        'name': id2nuts[row[0]][2],
        'classification': 'province'
    }
        #correct for Praha
    if area['id'] == '1100':
        area['id'] = '1000'
    cf.post_if_not_exist("areas", area, {"id": area['id']})
    parent = {
        'area_id': 'cz-kraje',
        'election_id': election_id
    }
    cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    #counties
    area = {
        'id': row[1],
        'name': id2nuts[row[1]][2],
        'classification': 'county'
    }    
    cf.post_if_not_exist("areas", area, {"id": area['id']})
    parent = {
        'area_id': row[0],
        'election_id': election_id
    }
    #correct for Praha
    if parent['area_id'] == '1100':
        parent['area_id'] = '1000'
    cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    #special towns vs. normal
    special = special_towns(row[1], row[3])
    if special:
        area = {
            'id': special['id'],
            'name': special['name'],
            'classification': 'municipality'
        }    
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': row[1],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)  
        area = {
            'id': row[3],
            'name': row[4],
            'classification': 'municipal district'
        }
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': special['id'],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    else:   #normal
        area = {
            'id': row[3],
            'name': row[4],
            'classification': 'municipality'
        }
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': row[1],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
        if row[3] == '551376':
            print(row)
    mindistr = int(row[6])
    maxdistr = int(row[7])
    for distr in range(mindistr, maxdistr+1):
        area = {
            'id': row[3]+'-'+str(distr),
            'name': row[4]+' - '+str(distr),
            'classification': 'district'
        }
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': row[3],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    #raise(Exception)
