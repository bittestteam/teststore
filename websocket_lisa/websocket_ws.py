import websocket
from threadpool import ThreadPool, makeRequests
import multiprocessing
import time

WS_URL = "wss://ws.bitasset.com.cn/spot/v1/websocket"


processes = 10

thread_num = 50

t_queryTickTradeList = 0
t_snapshotList = 0
t_querySnapshot = 0


def on_message(ws, message):
    print()
    # print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("Connection closed ……")


def on_open(ws):
    req = '{"marketInfo":"open"}'
    tcon1 = time.time()
    ws.send(req)
    tcon2 = time.time()
    tcon = tcon2 - tcon1
    req = '{"contractInfo":"1-open"}'
    tsend1 = time.time()
    ws.send(req)
    tsend2 = time.time()
    tsend = tsend2 - tsend1
    # print(tcon1)
    # print(tcon2)
    # print (tsend1)
    # print(tsend2)
    # print(tcon)
    # print(tsend)
    print("open")
    return tcon, tsend


def on_start(thread):
    print(thread)
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp(WS_URL, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


# def ws_thread(self):
#     thread = [1]
#     pool = threadpool.ThreadPool(1)
#     requests = threadpool.makeRequests(self.ws, thread)

def thread_web_socket():
    pool = ThreadPool(thread_num)
    num = list()

    for ir in range(thread_num):
        num.append(ir)
    requests = makeRequests(on_start, num)
    [pool.putRequest(req) for req in requests]
    pool.wait()


if __name__ == "__main__":

    pool = multiprocessing.Pool(processes=processes)

    for i in range(processes):
        pool.apply_async(thread_web_socket)
    pool.close()
    pool.join()







