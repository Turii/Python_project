import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def set_token(self, token):
        """Встановлює токен авторизації в заголовки"""
        self.session.headers.update({'Cookie': f'token={token}'})

    def send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return response

    def get(self, endpoint, **kwargs):
        return self.send_request('GET', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.send_request('POST', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.send_request('PUT', endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.send_request('PATCH', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.send_request('DELETE', endpoint, **kwargs)

"""
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, params=params, headers=headers)

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=data, headers=headers)

"""
    #def get(self, endpoint, params=None):
    #    return requests.get(f"{self.base_url}{endpoint}", params=params)

    #def post(self, endpoint, data=None):
    #    return requests.post(f"{self.base_url}{endpoint}", json=data)
