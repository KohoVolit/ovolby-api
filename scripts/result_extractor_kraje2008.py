import xmltodict
import api
import common_functions as cf

#election_id = 'europarl.europa.eu-cz-2014'
path = '../data/kz2008_data_dbf/'

provinces = []
with open(path + "kraje.csv") as infile:
    csvr = csv.reader(infile)
    for row in csvr:
        provinces.append(row)

# SUMMARY
sums = []
with open(path + "KZT6.csv") as fd:
    csvr = csv.reader(fd)
    i = 0
    for row in csvr:
        if i > 0:
            sums.append(row)
        i = i + 1

def county2province(county):
    return county[0:2] + '00'

for row in sums:
    election_id = 'cz-kraje-'+county2province(row[3])+'-2008'
    result = {
        'election_id': election_id,
        'area_id': row[4]+'-'+row[5],
        'area_classification': 'district'
    }
    cf.post_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']})
    summary = [
        {'name': 'eligibles', 'value': int(row[7])},
        {'name': 'attendees', 'value': int(row[8])},
        {'name': 'received_ballots', 'value': int(row[9])},
        {'name': 'valid_votes', 'value': int(row[10])}
    ]
    cf.put_single_property_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']}, 'summary', summary)

# COUNTS
vts = []
with open(path + "KZT6p.csv") as fd:
    csvr = csv.reader(fd)
    i = 0
    for row in csvr:
        if i > 0:
            vts.append(row)
        i = i + 1

def n2(i):
    if i < 10:
        return '0' + str(i)
    else:
        return str(i)



for province in provinces:
    n2id = {}
    election_id = 'cz-kraje-'+province[0]+'-2008'
    ar = cf.get_all_items("options",where={"other_identifiers.election_id":election_id})
    parties = []
    for p in ar:
        for oi in p['other_identifiers']:
            if oi['election_id'] == election_id:
                n2id[oi['identifier']] = p['identifier']
                parties.append(oi['identifier'])

    last_district = '0'
    counts = []
    countsobj = {}
    for row in vts:
        if county2province(row[3]) == province[0]:
            if last_district != row[4]+'-'+row[5]:
                result = {
                    'election_id': 'cz-kraje-'+county2province(row[3])+'-2008',
                    'area_id': row[4]+'-'+row[5],
                    'area_classification': 'district'
                }
                cf.post_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']})
                
            if last_district != row[4]+'-'+row[5]:
                if last_district != '0':
                    #raise(Exception)
                    for party in parties:
                        try:
                            counts.append(countsobj[party])
                        except:
                            counts.append({'votes': 0, 'option_identifier': n2id[party]})
                    cf.put_single_property_if_not_exist("results", last_result, {"election_id": last_result['election_id'], "area_id": last_result['area_id']}, 'counts', counts)
                    countsobj = {}
                    counts = []
                last_district = row[4]+'-'+row[5]
            
            countsobj[row[7]] = {'votes': int(row[8]), 'option_identifier': n2id[row[7]]}
            last_result = result

    # put the last one
    for party in parties:
        try:
            counts.append(countsobj[party])
        except:
            counts.append({'votes': 0, 'option_identifier': n2id[party]})
    cf.put_single_property_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']}, 'counts', counts)
#    for k in n2id:
#        counts.append({'option': n2id[k],'votes': int(row['HLASY_' + k])})
#    cf.put_single_property_if_not_exist("results", result,  {"election_id": result['election_id'], "area_id": result['area_id']}, 'counts', counts)
        
