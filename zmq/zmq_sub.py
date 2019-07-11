#coding=utf-8
import zmq
import json
import time

quot_pub_context = zmq.Context()
quot_pub_socket = quot_pub_context.socket(zmq.SUB)
# quot_pub_socket.connect("tcp://47.75.136.2:20051")
#quot_pub_socket.connect("tcp://192.168.1.163:20051")
quot_pub_socket.connect("tcp://192.168.105.222:5000")
#quot_pub_socket.connect("tcp://192.168.1.150:20054")
#quot_pub_socket.connect("tcp://192.168.1.150:20051")
#quot_pub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
a = 1
data={}
t1=time.time()
topicfilter = "1"
quot_pub_socket.setsockopt(zmq.SUBSCRIBE, topicfilter.encode("utf-8"))
#socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
#####现货接收
while True:
    ##message_type=4为行情快照 message_type=7为k线 message_type=6成交数据
    #if a>1 and data["message_type"] == 7 and data["contract_id"] ==7 and data["range"]=="60000":
    # if a>1 and data["message_type"] == 4 and data["contract_id"] ==123 :
    #   t1 = time.time()
    message = quot_pub_socket.recv().decode('utf-8')
    #data = json.loads(message)
    print (message)

    #if data["message_type"]==7 and data["contract_id"] ==7 and data["range"]=="60000":

    #if data["message_type"] == 4 and data["contract_id"] ==1 :
    # if data["message_type"] == 4 and data["contract_id"] ==123:
    # #if a>0:
    #     print(data)
    #     t2 = time.time()
    #     print(t2)

