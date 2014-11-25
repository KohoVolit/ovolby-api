import xmltodict
import api
import common_functions as cf

election_id = 'europarl.europa.eu-cz-2014'
path = 'EP2014ciselniky20140425/'

with open(path + "cnumnuts_utf8.xml") as fd:
    nuts = xmltodict.parse(fd.read())
with open(path + "epcoco_utf8.xml") as fd:
    towns = xmltodict.parse(fd.read())

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
for row in nuts['CNUMNUTS']['CNUMNUTS_ROW']:
    id2nuts[row['NUMNUTS']] = row

for row in towns['EP_COCO']['EP_COCO_ROW']:
    #provinces
    area = {
        'id': row['KRAJ'],
        'name': id2nuts[row['KRAJ']]['NAZEVNUTS'],
        'classification': 'province'
    }
        #correct for Praha
    if area['id'] == '1100':
        area['id'] = '1000'
    cf.post_if_not_exist("areas", area, {"id": area['id']})
    parent = {
        'area_id': 'cz',
        'election_id': election_id
    }
    cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    #counties
    area = {
        'id': row['OKRES'],
        'name': id2nuts[row['OKRES']]['NAZEVNUTS'],
        'classification': 'county'
    }    
    cf.post_if_not_exist("areas", area, {"id": area['id']})
    parent = {
        'area_id': row['KRAJ'],
        'election_id': election_id
    }
    #correct for Praha
    if parent['area_id'] == '1100':
        parent['area_id'] = '1000'
    cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    #special towns vs. normal
    special = special_towns(row['OKRES'], row['OBEC'])
    if special:
        area = {
            'id': special['id'],
            'name': special['name'],
            'classification': 'municipality'
        }    
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': row['OKRES'],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)  
        area = {
            'id': row['OBEC'],
            'name': row['NAZEVOBCE'],
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
            'id': row['OBEC'],
            'name': row['NAZEVOBCE'],
            'classification': 'municipality'
        }
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': row['OKRES'],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)
    mindistr = int(row['MINOKRSEK1'])
    maxdistr = int(row['MAXOKRSEK1'])
    for distr in range(mindistr, maxdistr+1):
        area = {
            'id': row['OBEC']+'-'+str(distr),
            'name': row['NAZEVOBCE']+' - '+str(distr),
            'classification': 'district'
        }
        cf.post_if_not_exist("areas", area, {"id": area['id']})
        parent = {
            'area_id': row['OBEC'],
            'election_id': election_id
        }
        cf.put_property_if_not_exist("areas", area, {"id": area['id']}, 'parents', parent)

