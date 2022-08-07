from warnings import catch_warnings
from locust import HttpUser, task, between
import json

class AETest( HttpUser): 
    wait_time = between(1,2)

    @task
    def get_mae( self): 
        payload = {"sequence": [[0.6237936375551048, 0.6126622676499771, 0.8134896393042048, 0.8077562326869803]]}
        headers = {'content-type': 'application/json'}

        self.client.post('/anomaly', data = json.dumps(payload), headers= headers)
