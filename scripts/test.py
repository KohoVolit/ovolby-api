import api

test = [
    {
        'id': '1',
    },
    {
        'id': '2',
    },
    {
        'id': '3',
        'parent_ids': [
            {
                'parent_id': '1',
                'election_id': 'a'
            }
        ]
    },
    {
        'id': '4',
        'parent_ids' : [
            {
                'parent_id': '1',
                'election_id': 'b'
            }
        ] 
    }   
]

api.post("test",test)

#r = api.get("test",where={"parent_ids.parent_id":"1"}_

