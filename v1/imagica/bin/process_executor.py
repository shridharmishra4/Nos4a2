import pika

from pymongo import MongoClient

from v1.imagica.core.model_trainer import ModelTrainer
from v1.imagica.core.model_loader import ModelLoader
from v1.imagica.core.post_processor import PostProcessor
from v1.imagica.core.services.propeties_services import InternalMessageProperties


db_host = "localhost"
db_port = 27017
db_name = "MessageStore"

db_connection = MongoClient(host=db_host, port=db_port)
db = db_connection[db_name]


class WriteMessagesToDB:
    # For SDF Annotated, Reconciliation Completed, Document Cluster Generated,
    def __init__(self):
        self.write_db = db

    def write(self, message_type, message):
        self.write_db[message_type].insert_one(message)


class MessageProcessor:
    def __init__(self):
        self.model_trainer = ModelTrainer()
        self.model_loader = ModelLoader()
        self.db_message_writer = WriteMessagesToDB()
        self.post_processor = PostProcessor()

    def process(self, event, body):
        if event in ("SDFAnnotated", "ReconciliationCompleted", "DocumentClusterGenerated"):
            self.db_message_writer.write(message_type=event, message=body)
        elif event == "InitiateTraining":
            self.model_trainer.train()
        elif event == "InitializeModel":
            self.model_loader.load_model()
        elif event == "SDFNormalized":
            self.post_processor.post_process(self.model_loader.predict())
        elif event == "PostProcessingRulesUpdated":
            self.post_processor = PostProcessor()
        else:
            print(f"Unknown Event: {event}")


class ConsumeMessages:
    def __init__(self):
        self.config = InternalMessageProperties()
        self.message_processor = MessageProcessor()
        self.read_connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config.message_queue_host))
        self.read_channel = self.read_connection.channel()
        self.read_channel.exchange_declare(exchange=self.config.exchange_name, exchange_type="direct")
        read_result = self.read_channel.queue_declare(exclusive=True)
        self.read_queue_name = read_result.method.queue
        for read_routing_key in self.config.outing_keys.keys():
            self.read_channel.queue_bind(exchange=self.config.exchange_name, queue=self.read_queue_name,
                                         routing_key=read_routing_key)

    def callback(self, channel, method, properties, body):
        print("channel:", channel)
        print("method:", method.routing_key)
        print("properties:", properties)
        print("body:", body)
        self.message_processor.process(event=method.routing_key)
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.read_channel.basic_consume(self.callback, queue=self.read_queue_name, no_ack=False)
        self.read_channel.start_consuming()


ConsumeMessages().start_consuming()
