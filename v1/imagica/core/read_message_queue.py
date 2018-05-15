import pika


message_queue_host = "localhost"
exchange_name = "logs"
routing_keys = list()

class WriteMessages:
    pass


class StoreMessages:
    def write_annotated_files(self):
        pass


class ConsumeMessages:
    def __init__(self):
        self.store_messages_object = StoreMessages()
        self.write_messages_object = WriteMessages()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=message_queue_host))
        self.channel = self.connection.channel()
        self.channel.declare(exchange=exchange_name, exchange_type="direct")
        result = self.channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        for routing_key in routing_keys:
            self.channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    def write_to_internal_queues(self):
        pass

    def callback_consuming_normalized(self, channel, method, properties, body):
        pass

    def callback_consuming_annotated(self, channel, method, properties, body):
        pass

    def callback_consuming_post_processing_changed(self, channel, method, properties, body):
        self.write_to_internal_queues(body)

    def callback_consuming_reconciled(self, channel, method, properties, body):
        pass

    def start_consuming(self, channel, method, properties, body):
        pass
