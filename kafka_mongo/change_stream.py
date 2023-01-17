from kafka_producer import send_message
from json import dumps
from multiprocessing import Process


class ChangeStream:
    def __init__(self,collection) -> None:    
        self.collection = collection
        p = Process(target=self.start_streaming)
        p.start()
        p.join()
        # self.start_streaming()
    
    def start_streaming(self):
        print(f"Started listening{str(self.collection)}")
        with self.collection.watch() as stream:
            for change in stream:
                data = dumps(change)
                print(data)
                send_message(data)
                print('') 