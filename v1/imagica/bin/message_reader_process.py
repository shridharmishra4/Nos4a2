import pika

from v1.imagica.core.services.propeties_services import InternalMessageProperties, ExternalMessageProperties


class ConsumeMessages:
    def __init__(self):
        self.read_config = ExternalMessageProperties()
        self.write_config = InternalMessageProperties()

        self.read_connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.read_config.message_host))
        self.read_channel = self.read_connection.channel()
        self.read_channel.exchange_declare(exchange=self.read_config.exchange_name, exchange_type="direct")
        read_result = self.read_channel.queue_declare(exclusive=True)
        self.read_queue_name = read_result.method.queue
        for read_routing_key in self.read_config.routing_keys.keys():
            self.read_channel.queue_bind(exchange=self.read_config.exchange_name, queue=self.read_queue_name,
                                         routing_key=read_routing_key)

        self.write_connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.write_config.message_host))
        self.write_channel = self.write_connection.channel()
        self.write_channel.exchange_declare(exchange=self.write_config.exchange_name, exchange_type="direct")
        write_result = self.write_channel.queue_declare(exclusive=True, arguments={"x-max-priority": 10})
        self.write_queue_name = write_result.method.queue
        for write_routing_key in self.write_config.routing_keys.keys():
            self.write_channel.queue_bind(exchange=self.write_config.exchange_name,
                                          queue=self.write_queue_name,
                                          routing_key=write_routing_key)

    def write_to_internal_queues(self, routing_key, body):
        self.write_channel.basic_publish(exchange=self.write_config.exchange_name,
                                         routing_key=routing_key,
                                         properties=pika.BasicProperties(
                                             priority=self.write_config.routing_keys[routing_key]),
                                         body=body)

    def callback(self, channel, method, properties, body):
        print("channel:", channel)
        print("method:", method.routing_key)
        print("properties:", properties)
        print("body:", body)
        self.write_to_internal_queues(routing_key=method.routing_key, body=body)
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.read_channel.basic_consume(self.callback, queue=self.read_queue_name, no_ack=False)
        self.read_channel.start_consuming()


ConsumeMessages().start_consuming()
