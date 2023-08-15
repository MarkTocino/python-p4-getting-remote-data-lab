import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(URL)
        return response.content

    def load_json(self):
        list = []
        # here my_request is a json dictionary and we ran the method def_response_body for the response and we have the response content and now the response is a dict. then we appended it to an empty list
        my_requests = json.loads(self.get_response_body())
        for my_request in my_requests:
            list.append(my_request)
        return list