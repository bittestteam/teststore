import json
from ws4py.client.threadedclient import WebSocketClient


class CG_Client(WebSocketClient):

    def opened(self):
        req = '{"marketInfo":"open"}'
        self.send(req)
        req = '{"contractInfo":"1-open"}'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, m):
        print(m)

        # resp = json.loads(str(resp))
        # data = resp['data']
        # if type(data) is dict:
        #     ask = data['asks'][0]
        #     print('Ask:', ask)
        #     bid = data['bids'][0]
        #     print('Bid:', bid)


if __name__ == '__main__':
    ws = None
    try:
        ws = CG_Client('wss://ws.bitasset.com/spot/v1/websocket')
        ws.connect()
        ws.run_forever()

    except KeyboardInterrupt:
        ws.close()
