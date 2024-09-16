import json
from confluent_kafka import Consumer, KafkaError

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def create_consumer():
    config = load_config()
    #credentials kafka
    conf = {
        'bootstrap.servers': config['bootstrap_servers'],
        'group.id': 'consumer-rat-eos-pc',
        'auto.offset.reset': 'latest',
        'security.protocol': config['security_protocol'],
        'sasl.mechanisms': config['sasl_mechanisms'],
        'sasl.username': config['sasl_username'],
        'sasl.password': config['sasl_password']    
        }
    consumer = Consumer(conf)
    consumer.subscribe(['rat-eos-pc'])  
    return consumer


def consume():
    consumer = create_consumer()
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            # Decode the message from bytes to string
            message_value = msg.value().decode('utf-8')
            #print it
            print(message_value + "\n")


    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume()
