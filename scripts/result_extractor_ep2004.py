import xmltodict
import api
import common_functions as cf

election_id = 'europarl.europa.eu-cz-2004'
path = 'EP2004okrsky/'

# SUMMARY
with open(path + "ept2.xml") as fd:
    sums = xmltodict.parse(fd.read())

for row in sums['EP_T2']['EP_T2_ROW']:
    result = {
        'election_id': election_id,
        'area_id': row['OBEC']+'-'+row['OKRSEK'],
        'area_classification': 'district'
    }
    cf.post_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']})
    summary = [
        {'name': 'eligibles', 'value': int(row['VOL_SEZNAM'])},
        {'name': 'attendees', 'value': int(row['VYD_OBALKY'])},
        {'name': 'received_ballots', 'value': int(row['ODEVZ_OBAL'])},
        {'name': 'valid_votes', 'value': int(row['PL_HL_CELK'])}
    ]
    cf.put_single_property_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']}, 'summary', summary)

# COUNTS
with open(path + "ept2p.xml") as fd:
    vts = xmltodict.parse(fd.read())


n2id = {}

ar = cf.get_all_items("options",where={"other_identifiers.election_id":election_id})
parties = []
for p in ar:
    for oi in p['other_identifiers']:
        if oi['election_id'] == election_id:
            n2id[oi['identifier']] = p['id']
            parties.append(oi['identifier'])

last_district = '0'
counts = []
countsobj = {}
for row in vts['EP_T2P']['EP_T2P_ROW']:
    if last_district != row['OBEC']+'-'+row['OKRSEK']:
        result = {
            'election_id': election_id,
            'area_id': row['OBEC']+'-'+row['OKRSEK'],
            'area_classification': 'district'
        }
        cf.post_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']})
        
    if last_district != row['OBEC']+'-'+row['OKRSEK']:
        if last_district != '0':
            #raise(Exception)
            for party in parties:
                try:
                    counts.append(countsobj[party])
                except:
                    counts.append({'votes': 0, 'option_id': n2id[party]})
            cf.put_single_property_if_not_exist("results", last_result, {"election_id": last_result['election_id'], "area_id": last_result['area_id']}, 'counts', counts)
            countsobj = {}
            counts = []
        last_district = row['OBEC']+'-'+row['OKRSEK']
    
    countsobj[row['ESTRANA']] = {'votes': int(row['POC_HLASU']), 'option_id': n2id[row['ESTRANA']]}
    last_result = result

# put the last one
for party in parties:
    try:
        counts.append(countsobj[party])
    except:
        counts.append({'votes': 0, 'option_id': n2id[party]})
cf.put_single_property_if_not_exist("results", result, {"election_id": result['election_id'], "area_id": result['area_id']}, 'counts', counts)
#    for k in n2id:
#        counts.append({'option': n2id[k],'votes': int(row['HLASY_' + k])})
#    cf.put_single_property_if_not_exist("results", result,  {"election_id": result['election_id'], "area_id": result['area_id']}, 'counts', counts)
        
