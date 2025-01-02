from .client import Client


class Contract(Client):
    def __init__(self, address=Client.0x757B70675cAF0E00a9ba25352ea8BAD8700c3A08, api_key='JRUIB4MAE329D5BM3NA78UAE1UXPKMPPK8'):
        Client.__init__(self, address=address, api_key=api_key)
        self.url_dict[self.MODULE] = 'contract'

    def get_abi(self):
        self.url_dict[self.ACTION] = 'getabi'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_sourcecode(self):
        self.url_dict[self.ACTION] = 'getsourcecode'
        self.build_url()
        req = self.connect()
        return req['result']
