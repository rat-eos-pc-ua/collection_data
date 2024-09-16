import json
from confluent_kafka import Consumer, KafkaError

def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            print("Config loaded successfully: ", config)  # Debug statement
            return config
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        raise
    except FileNotFoundError as e:
        print(f"Configuration file not found: {e}")
        raise

def create_consumer():
    try:
        config = load_config()
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
        print("Consumer created and subscribed successfully")
        return consumer
    except Exception as e:
        print(f"Failed to create and subscribe consumer: {e}")
        raise

def consume():
    try:
        consumer = create_consumer()
        print("Starting message consumption...")
        try:
            while True:
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print("Reached end of partition")
                        continue
                    else:
                        print(f"Kafka error: {msg.error()}")
                        break
                message_value = msg.value().decode('utf-8')
                print(f"Received message: {message_value}\n")
        except KeyboardInterrupt:
            print("Interrupted by user")
        finally:
            consumer.close()
            print("Consumer closed")
    except Exception as e:
        print(f"Error during consumption: {e}")

if __name__ == "__main__":
    consume()
