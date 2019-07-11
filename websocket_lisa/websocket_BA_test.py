import time

import websocket


def on_message(ws, message):  # 服务器有数据更新时，主动推送过来的数据
    print(message)


def on_error(ws, error):  # 程序报错时，就会触发on_error事件
    print(error)


def on_close(ws):
    print("Connection closed ……")


def on_open(ws):  # 连接到服务器之后就会触发on_open事件，这里用于send数据
    req = '{"marketInfo":"open"}'
    t1 = time.time()
    print (t1)
    ws.send(req)
    t2 = time.time()
    print (t2)
    req = '{"contractInfo":"1-open"}'
    ws.send(req)
    t3 = time.time()
    print (t3)

if __name__ == "__main__":
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("wss://tws.bitasset.cc:7006/spot/v1/websocket",
                                     on_message=on_message,
                                     on_error=on_error,
                                     on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()