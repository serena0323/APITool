import requests
import json


class SessionManager:
    def __init__(self, url, session=None):
        self.url = url
        self._session_id = None
        if session is None:
            self.session = requests.session()
        else:
            self.session = session
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
                   'X-CENTRIFY-NATIVE-CLIENT': 'Web'}

    def request(self, request_api, data=None, extra_headers=None, method="POST", uri_params=None,
                   client_cert=None, **kwargs):

        combined_headers = self.header if extra_headers is None else {**self.headers, **extra_headers}
        if 'files' in kwargs:
            file_header = {'X-CENTRIFY-NATIVE-CLIENT': 'true'}
            combined_headers = {**file_header, **combined_headers}

        if data is not None:
            data = json.dumps(data)

        final_url = self.url if request_api is None else self.url + request_api
        response = self.session.request(method, final_url, data=data, headers=combined_headers, params=uri_params,
                                        cert=client_cert, **kwargs)
        return response

    def post(self, request_api, data=None, **kwargs):
        return self.request(self, request_api, method="POST", data=data, **kwargs)

    def get(self, request_api, data = None, ** kwargs):
        return self.request(self, request_api, method="POST", data=data, **kwargs)