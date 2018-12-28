import opendht, time, json
from flask import make_response

PEER="bootstrap.ring.cx"

_node = opendht.DhtRunner()
_node.run()
_node.bootstrap(PEER, "4222")
#_node.put(opendht.InfoHash.get("yyLK2PhXrwLRNUh9"), opendht.Value(b'Daku'))

def get(key):
    results = _node.get(opendht.InfoHash.get(str(key)))
    values = {}
    values[key] = {}

    for i, value in enumerate(results):
        
        values[key][i] = {}
        values[key][i]['id'] = value.id
        values[key][i]['data'] = value.data.decode("utf-8")
        values[key][i]['size'] = value.size
    #import pdb; pdb.set_trace()
    return values

def put(key, value):
    _node.put(opendht.InfoHash.get(str(key)), opendht.Value(value.encode()))
    return make_response("Successfully updated key-value\n", 201)

#if __name__ == '__main__':

    #get("yyLK2PhXrwLRNUh9")