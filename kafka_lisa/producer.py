# coding:utf-8
import kafka as kfk
import json
KAFAKA_TOPIC = "wallet-transaction-success-topic"
def kfk_producer_send():
    print (1)
    producer = kfk.KafkaProducer(bootstrap_servers=['192.168.1.152:9092'])
    print(2)
    data={"transactionType":"WWOU", "orderNumber":"520", "serialNumber":"2922443460730470403"}
    jsondata=bytes(json.dumps(data), encoding = "utf8")
    producer.send(KAFAKA_TOPIC, jsondata)
    # 一定要记得 刷新 producer 否则的话 真正的消息不能入 kafka_lisa
    producer.flush()
    producer.close()
if __name__ == "__main__":
    print("a")
    kfk_producer_send()