""" example: Sum up results for parent areas for single elections """

import slugify
import api
import math

election_id = "europarl.europa.eu-cz-2014"

def adding(result,area_id,data,parents,election_id):
    try:
        parents[area_id]
    except:
        areas = api.get('areas',where={"id":area_id,"parents.election_id":election_id})
        if len(areas["_items"]) > 0:
            parents[area_id] = areas["_items"][0]["parents"][0]['area_id']
            try:
                data[parents[area_id]]
            except:
                parent_areas = api.get('areas',where={"id": parents[area_id],"parents.election_id":election_id})
                data[parents[area_id]] = {'summary':{},'counts':{},'classification':parent_areas["_items"][0]['classification']}
    try:
        parent_id = parents[area_id]
        #print(area_id,parent_id)      
        try:
            for s in result['summary']:
                try:
                    data[parent_id]['summary'][s['name']] = data[parent_id]['summary'][s['name']] + int(s['value'])
                except:
                    data[parent_id]['summary'][s['name']] = int(s['value'])
            for s in result['counts']:
                try:
                    data[parent_id]['counts'][s['option_identifier']] = data[parent_id]['counts'][s['option_identifier']] + int(s['votes'])
                except:
                    data[parent_id]['counts'][s['option_identifier']] = int(s['votes']) 
            data = adding(result,parent_id,data,parents,election_id)
        except:
            nothing = 0
    except:
        nothing = 0
    #raise(Exception)
    return data
        
data = {}
parents = {}


results = api.get('results',where={"election_id":election_id})
max_results = results['_meta']['max_results']
total = results['_meta']['total']
for p in range(1,math.ceil(total/max_results)+1):
    print(p)
    results = api.get('results',where={"election_id":election_id},page=p)
    for result in results["_items"]:
        #print(result["area_id"])
        #if result["area_id"][0:6] == '559351':
        adding(result,result["area_id"],data,parents,election_id)
    #raise(Exception)

out = []
for area_id in data:
    item = {'summary':[],'counts':[],'area_classification':data[area_id]['classification'],'election_id': election_id, "area_id":area_id}
    for s in data[area_id]['summary']:
        item['summary'].append({'name':s,'value':data[area_id]['summary'][s]})
    for s in data[area_id]['counts']:
        item['counts'].append({'option_identifier':s,'votes':data[area_id]['counts'][s]})
    out.append(item)

api.post("results",out)        
   
#vpapi.get('memberships',where={"person_id":r_pers["_items"][0]["id"]},embed=["organization"])   
