import api
import math

def get_all_items(resource, **kwargs):
    resp = api.get(resource, **kwargs)
    out =[]
    try:
        npages = math.ceil(int(resp['_meta']['total'])/int(resp['_meta']['max_results']))
        for p in range(1,npages+1):
            newkwargs = kwargs
            newkwargs['page'] = str(p)
            r = api.get(resource, **newkwargs)
            try:
                out = out + r['_items']
            except:
                nothing = 0
    except:
        print("no meta:", resource)
        print(kwargs)
    return out   


def post_if_not_exist(resource, obj, w):
    r = api.get(resource,where=w)
    try:
        if len(r['_items']) == 0:
            api.post(resource, obj)
    except:
        pass


# into list of properties, as next item
def put_property_if_not_exist(resource, obj, w, property_name, prop):
    r = api.get(resource, where=w)
#    print(r)
#    print(obj)
#    print(w)
#    print(property_name)
#    print(prop)
    if len(r['_items']) == 0:
        obj[property_name] = [prop]
        r = api.post(resource, obj)
        obj_old = r['_items'][0]
    else:
        obj_old = r['_items'][0]
        for pr in obj_old:
            if pr[0] != '_':
                try:
                    obj[pr]
                except:
                    obj[pr] = obj_old[pr]
        try:
            properties = r['_items'][0][property_name]
        except:
            properties = []
        already_in = False
        for pr in properties:
            if pr == prop:
                already_in = True
        if not already_in:
            properties.append(prop)
            obj[property_name] = properties
            r = api.put(resource + "/" + r["_items"][0]["_id"], obj)

# no list of properties, directly:
def put_single_property_if_not_exist(resource, obj, w, property_name, prop):
    r = api.get(resource, where=w)
    if len(r['_items']) == 0:
        obj[property_name] = prop
        r = api.post(resource, obj) 
        obj_old = r['_items'][0]
    else:
        obj_old = r['_items'][0]
        for pr in obj_old:
            if pr[0] != '_':
                try:
                    obj[pr]
                except:
                    obj[pr] = obj_old[pr]
        try:
            properti = r['_items'][0][property_name]
        except:
            obj[property_name] = prop
            r = api.put(resource + "/" + r["_items"][0]["_id"], obj)
