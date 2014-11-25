import api
import custom_functions as cf

items = cf.get_all_items("areas",where={"parents.area_id":"5301","parents.election_id":"europarl.europa.eu-cz-2009"})

for item in items:
    ds = api.get("results",where={"area_id":item['id'],"election_id":"europarl.europa.eu-cz-2009"})
    print(ds['_items'][0]['area_id'],ds['_items'][0]['summary'][0]['value'])
    
    
items = cf.get_all_items("results",where={"area_classification":"municipality","election_id":"europarl.europa.eu-cz-2009"})

t3 = 0
for item in items:
    t3 = t3 + int(item['summary'][0]['value'])
    
items = cf.get_all_items("results",where={"area_classification":"county","election_id":"europarl.europa.eu-cz-2009"})

t3 = 0
for item in items:
    t3 = t3 + int(item['summary'][0]['value'])
    
for row in vts['EP_T2P']['EP_T2P_ROW']:
    if row['OBEC']+'-'+row['OKRSEK'] == "506320-2":
        print(row)

t3 = 0
for row in vts['EP_T2P']['EP_T2P_ROW']:
    t3 = t3 + int(row['POC_HLASU'])

t4 = 0
for row in sums['EP_T2']['EP_T2_ROW']:
    t4 = t4 + int(row['PL_HL_CELK'])

506320-3
529621-4
529753-1
530565-1
533921-5
534013-2
535427-6
535915-1
536415-1
540757-5
541001-1
541699-3
542059-1
542415-3
544591-3
545171-8
547999-13
548341-1
548499-1
549118-1
549142-3
551040-2
553191-1
553450-4
553654-6
555835-3
556041-2
556301-2
556467-5
556467-7
556734-2
557200-5
557536-2
557536-4
557587-8
558125-3

