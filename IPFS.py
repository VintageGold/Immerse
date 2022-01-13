#https://docs.ipfs.io/reference/http/api/#getting-started
import requests
class IPFS:

    def get_peers():

        return requests.post("http://127.0.0.1:5001/api/v0/swarm/peers",).json()

    #Flags aren't working
    def add(fn):

        params = {'progress':True,
                 "silent":False
                 }

        files = {
        'file': ('myfile', open(fn, 'rb')),
        }

        response = requests.post('http://127.0.0.1:5001/api/v0/add', json=params, files=files)

        print("Added",fn,"to IPFS - ","Response",response.status_code)

        return response

    def get_file(key):
        params = (('arg', key),)

        response = requests.post('http://127.0.0.1:5001/api/v0/block/get', params=params)

        print("Retrieved file hash",key,"from IPFS -","Response",response.status_code)

        return response