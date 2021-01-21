from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        with open(self.input_file) as f:
            '''
            It was not possible to read each line, so the whole file had to be loaded into memory
            and then parsed using the json.loads function. Not the best approach for handling
            large JSON files that won't fit into memory, but it works for this case.
            '''
            json_content = json.loads(f.read())
            for json_object in json_content:
                message = self.dict_to_binary(json_object)
                self.send(self.topic, message)
                time.sleep(1)

    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
        