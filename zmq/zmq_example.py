#!/usr/bin/python
#-*-coding:utf-8-*-


# 1.Request-Reply模式：
#
# 客户端在请求后，服务端必须回响应

# import time
# import zmq
#
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")
#
# while True:
#     message = socket.recv()
#     print (message)
#     #time.sleep(1)
#     socket.send("server response!")


#!/usr/bin/python
#-*-coding:utf-8-*-

# import zmq
# import sys
#
# from pip._vendor.distlib.compat import raw_input
#
# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")
#
# while(True):
#     data = raw_input("input your data:")
#     if data == 'q':
#         sys.exit()
#
#     socket.send(data)
#
#     response = socket.recv();
#     print (response)


# 2.Publish-Subscribe模式:
#
# 广播所有client，没有队列缓存，断开连接数据将永远丢失。client可以进行数据过滤。

#!/usr/bin/python
#-*-coding:utf-8-*-

# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind("tcp://127.0.0.1:5000")
# while True:
#     msg = raw_input('input your data:')
#     socket.send(msg)

#!/usr/bin/python
#-*-coding:utf-8-*-

# import time
# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.SUB)
# socket.connect("tcp://127.0.0.1:5000")
# socket.setsockopt(zmq.SUBSCRIBE,'')
# while True:
#     print  (socket.recv())