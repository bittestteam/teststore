#coding=utf-8
import zmq
import json
import time
import random





def getBigNumber(number):
    return str(int(number * 1000000000000000000))

def to_decimal(f, p = 6):
    i = round(f * pow(10, p))
    return str(round(i * pow(10, 18 - p)))


if __name__ == '__main__':
    TRADE_SERVER_URL = 'tcp://192.168.1.163:20050'
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    socket.connect(TRADE_SERVER_URL)
    py2json = {}



####websocket推送
# py2json['message_type'] = 1029
# py2json['appl_id'] = 2
# py2json['account_id'] = 666666
# py2json['type'] = 0

#####指数推送
# py2json['message_type'] = 5008
# py2json['appl_id'] = 2
# py2json['commodity_id'] = 3
# py2json['currency_id'] = 2
# py2json['index_price'] = '5000000000000000000000'
# aaaaaaaaaaaaaaaaaaaaaaaa = '1234567890123456789012'
# py2json['funding_basis'] = '0'
# py2json['market_id'] = 'idx'

# ######期货账号加钱
# for i in range(669000,670000):
#     py2json['message_type'] = 4005
#     py2json['account_id'] = i
#     py2json['currency_id'] = 2
#     py2json['from_appl_id'] = 5
#     py2json['to_appl_id'] = 2
#     py2json['quantity'] = getBigNumber(990000)
#     py2json['id'] = str(int(time.time()*1000))
#     #py2json['id'] = "1551950841879"
#     str_json = json.dumps(py2json).encode('utf-8')
#     print(str_json)
#     socket.send(str_json)
#     ret = socket.recv()
#     print(ret)
#     time.sleep(0.001)

######期货core_param_futrue更新
# py2json['message_type'] = 5004
# py2json['account_id'] = 666666
# py2json['type'] = 1   #1新增 2修改 3删除
# py2json['appl_id'] = 2
# py2json['variety_id'] = 2
# py2json['contract_id'] = 137
# py2json['taker_fee_ratio'] = getBigNumber(0.0006)
# py2json['maker_fee_ratio'] = getBigNumber(-0.0006)
# py2json['posi_limit'] = getBigNumber(1000)
# py2json['order_limit'] = getBigNumber(500)
# py2json['delivery_fee_ratio'] = getBigNumber(0.0009)

######期货core_param_orders_futrue更新
# py2json['message_type'] = 5009
# py2json['appl_id'] = 2


######保证金修改指令
# py2json['message_type'] = 5012
# py2json['appl_id'] = 2
# py2json['variety_id'] = 1
# py2json['contract_id'] = 0
# py2json['account_id'] = 666666

#####合约指令
# py2json['message_type'] = 5007
# py2json['appl_id'] = 2
# py2json['contract_id'] = 150
# py2json['symbol'] = "BTCUSDT21340101"
# py2json['price_tick'] = getBigNumber(0.01)
# py2json['lot_size'] = getBigNumber(1)
# py2json['taker_fee_ratio'] = getBigNumber(0.0003)
# py2json['maker_fee_ratio'] = getBigNumber(0)
# py2json['limit_max_level'] = 10
# py2json['market_max_level'] = 10
# py2json['max_num_orders'] = 50
# py2json['price_limit_rate'] = getBigNumber(0.025)
# py2json['commodity_id'] = 3
# py2json['currency_id'] = 2
# py2json['contract_status'] = 2
# py2json['perpetual_premium_limit'] = getBigNumber(0.0003)
# py2json['perpetual_fundingfee_limit'] = getBigNumber(0.075)
# py2json['perpetual_settle_frequency'] = 3
# py2json['risklessrate_goods'] = getBigNumber(0.0003)
# py2json['risklessrate_money'] = getBigNumber(0.0006)
# py2json['list_price'] = getBigNumber(3855)
# py2json['list_time'] = 1551940474000000
# py2json['last_trade_time'] = 5175388800000000
# py2json['delivery_time'] = 5175388800000000
# py2json['contract_unit'] = getBigNumber(0.1)
# py2json['contract_side'] = 1
# py2json['order_limit'] = getBigNumber(5000)
# py2json['posi_limit'] = getBigNumber(50000)
# py2json['contract_type'] = 2
# py2json['delivery_period'] = 2
# py2json['delivery_type'] = 1
# py2json['impact_margin_notional'] = getBigNumber(20000)
# py2json['fair_basis_interval'] = 600
# py2json['clear_price_interval'] = 600
# py2json['delivery_price_interval'] = 600
# py2json['variety_id'] = 15
# py2json['type'] = 2  #1新增 2修改 3刪除
# py2json['min_maintain_rate'] = getBigNumber(0.025)
# py2json['delivery_fee_ratio'] = getBigNumber(0.0003)


######下单
# while True:
#     py2json['message_type'] = 1001
#     py2json['appl_id'] = 2
#     py2json['contract_id'] = 100  # 合约ID
#     py2json['account_id'] = 666666  # 用户ID
#     py2json['side'] = 1  # 1买，-1卖
#     #py2json['price'] = getBigNumber(4450 + round(10 * random.random(), 2))  # 委托价
#     py2json['quantity'] = getBigNumber(round(5 * random.random(), 2))  # 委托量
#     py2json['price'] = getBigNumber(4460)  # 委托价
#     #py2json['quantity'] = getBigNumber(1)  # 委托量
#     py2json['position_effect'] = 1  # 1开仓，2平仓
#     # py2json['margin_type'] = 2  # 逐仓
#     # py2json['margin_rate'] = getBigNumber(0.5)  # 保证金率
#     py2json['margin_type'] = 1  # 全仓
#     py2json['margin_rate'] = "0"  # 不改
#     py2json['client_order_id'] = ""
#     py2json['order_type'] = 1
#     py2json['stop_price'] = "0"
#     py2json['minimal_quantity'] = "0"
#     py2json['stop_condition'] = 0
#     py2json['time_in_force'] = 1
#     str_json = json.dumps(py2json).encode('utf-8')
#     print(str_json)
#     socket.send(str_json)
#     ret = socket.recv()
#     print(ret)
#     time.sleep(0.3)
#
#     py2json['message_type'] = 1001
#     py2json['appl_id'] = 2
#     py2json['contract_id'] = 100  # 合约ID
#     py2json['account_id'] = 666666  # 用户ID
#     py2json['side'] = -1  # 1买，-1卖
#     #py2json['price'] = getBigNumber(4450 + round(10 * random.random(), 2))  # 委托价
#     py2json['quantity'] = getBigNumber(round(5 * random.random(), 2))  # 委托量
#     py2json['price'] = getBigNumber(4460)  # 委托价
#     #py2json['quantity'] = getBigNumber(1)  # 委托量
#     py2json['position_effect'] = 1  # 1开仓，2平仓
#     # py2json['margin_type'] = 2  # 逐仓
#     # py2json['margin_rate'] = getBigNumber(0.5)  # 保证金率
#     py2json['margin_type'] = 1  # 全仓
#     py2json['margin_rate'] = "0"  # 不改
#     py2json['client_order_id'] = ""
#     py2json['order_type'] = 1
#     py2json['stop_price'] = "0"
#     py2json['minimal_quantity'] = "0"
#     py2json['stop_condition'] = 0
#     py2json['time_in_force'] = 1
#     str_json = json.dumps(py2json).encode('utf-8')
#     print(str_json)
#     socket.send(str_json)
#     ret = socket.recv()
#     print(ret)
#     time.sleep(0.3)

# {"message_type":4005,"account_id":666694,"currency_id":2,"from_appl_id":5,"to_appl_id":2,"
# quantity":"10000000000000000000","id":"1551404118721"}
##向期货划钱
# py2json['message_type'] = 4005
# py2json['account_id'] = 674087
# py2json['currency_id'] = 2
# py2json['from_appl_id'] = 5
# py2json['to_appl_id'] = 2
# py2json['quantity'] =  getBigNumber(1000)
# py2json['id'] = str(int(time.time()*1000))


# def getSpotTransferAddMessage(accountId, quantity, currencyId):
#     py2json = {}
#     py2json['message_type'] = 4005
#     py2json['currency_id'] = currencyId
#     py2json['account_id'] = accountId
#     py2json['from_appl_id'] = 5
#     py2json['to_appl_id'] = 1
#     py2json['quantity'] = getBigNumber(quantity)
#     py2json['id'] = int(time.time()) * 1000
#     return json.dumps(py2json).encode('utf-8')

###指数价格
# py2json['message_type'] = 5008
# py2json['appl_id'] = 2
# py2json['commodity_id'] = 3
# py2json['currency_id'] = 2
# py2json['index_price'] = getBigNumber(6500)
# py2json['funding_basis'] = '0'
# py2json['market_id'] = 'idx'

py2json['message_type']=5008
py2json['appl_id']=2
py2json['underlying_id'] ="6-2"
py2json['index_price'] = getBigNumber(90)
py2json['index_time'] = 1557995272564000

# py2json['message_type']=5008
# py2json['appl_id']=2
# py2json['underlying_id'] ="SZ399300"
# py2json['index_price'] = getBigNumber(2800)
# py2json['index_time'] = 1557995272564000

#
# # ##结算指令
# # #py2json['message_type'] = 5014
# #
str_json = json.dumps(py2json).encode('utf-8')
print(str_json)
socket.send(str_json)
ret = socket.recv()
print(ret)









