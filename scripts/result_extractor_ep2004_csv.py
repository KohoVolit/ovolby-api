import csv
import api
import common_functions as cf

election_id = 'europarl.europa.eu-cz-2004'

n2id = {}
ar = cf.get_all_items("options",where={"other_identifiers.election_id":election_id})
parties = []
for p in ar:
    for oi in p['other_identifiers']:
        if oi['election_id'] == election_id:
            n2id[oi['identifier']] = p['identifier']
            parties.append(oi['identifier'])

summary_items = ['eligibles','attendees','received_ballots','valid_votes']

i = 0
data = []
names = []
with open("../data/ep_2004_okrsky.csv") as infile:
    csv_reader = csv.reader(infile)
    for row in csv_reader:
        item = {}
        j = 0
        for it in row:
            if i == 0:
                names.append(it)
            else:
                item[names[j]] = it
            j = j + 1
        if i > 0:
            data.append(item)
        i = i + 1

results = []
check = 0
for row in data:
    summary = []
    for item in summary_items:
        summary.append({'name':item,'value':int(row[item])})
    counts = []
    for party in parties:
        counts.append({'votes': int(row[party]), 'option_identifier': n2id[party]})
    result = {
        "election_id": election_id,
        "area_id": row['municipality']+'-'+row['district'],
        'area_classification': 'district',
        'summary': summary,
        'counts': counts
    }
    check = check + int(row['1'])
#    r = api.post("results",result)
    results.append(result)
#    if r['_status'] == 'ERR':
#        #print(result['area_id'],r['_issues'])
#        parent_id = result['area_id'][0:6]
#        q = api.get("areas",where={"parents.area_id":parent_id,"parents.election_id":"europarl.europa.eu-cz-2004"})
#        print(parent_id,q['_items'][0]['id'])
#        #raise(Exception)
    
api.post("results",results)
