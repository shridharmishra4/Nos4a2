import pika

message_queue_host = "localhost"
read_exchange_name = "incoming"
write_exchange_name = "outgoing"

read_routing_keys = {
    "SDFNormalized": 4,
    "SDFAnnotated": 2,
    "PostProcessingRules": 5,
    "ReconciliationCompleted": 1,
    "DocumentClusterGenerated": 0
}
write_routing_keys = {
    "InitiateTraining": 6,
    "InitializeModel": 8,
    "SDFNormalized": 4,
    "SDFAnnotated": 2,
    "PostProcessingRules": 5,
    "ReconciliationCompleted": 1,
    "DocumentClusterGenerated": 0
}


class ConsumeMessages:
    def __init__(self):
        self.read_connection = pika.BlockingConnection(pika.ConnectionParameters(host=message_queue_host))
        self.read_channel = self.read_connection.channel()
        self.read_channel.exchange_declare(exchange=read_exchange_name, exchange_type="direct")
        read_result = self.read_channel.queue_declare(exclusive=True)
        self.read_queue_name = read_result.method.queue
        for read_routing_key in read_routing_keys.keys():
            self.read_channel.queue_bind(exchange=read_exchange_name, queue=self.read_queue_name,
                                         routing_key=read_routing_key)

        self.write_connection = pika.BlockingConnection(pika.ConnectionParameters(host=message_queue_host))
        self.write_channel = self.write_connection.channel()
        self.write_channel.exchange_declare(exchange=write_exchange_name, exchange_type="direct")
        write_result = self.write_channel.queue_declare(exclusive=True, arguments={"x-max-priority": 10})
        self.write_queue_name = write_result.method.queue
        for write_routing_key in write_routing_keys.keys():
            self.write_channel.queue_bind(exchange=write_exchange_name,
                                          queue=self.write_queue_name,
                                          routing_key=write_routing_key)

    def write_to_internal_queues(self, routing_key, body):
        self.write_channel.basic_publish(exchange=write_exchange_name,
                                         routing_key=routing_key,
                                         properties=pika.BasicProperties(priority=write_routing_keys[routing_key]),
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
