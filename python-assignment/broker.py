from datetime import datetime
import socket
from threading import Thread
import time

# Communication constants
HOST = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 4096

# Message constants
ACK = "ACK"
FORMAT = "utf-8"
SEPERATOR = "$"


class Broker:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.topics = dict()  # key: topic name, value: data
        self.subscribers = dict()  # key: address, value: topic name

    def __log(self, msg):
        print("[BROKER] {} - {}".format(
            datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"), msg))

    def __extract_data(self, raw_data: bytes):
        # Initialization and decoding
        client_type = topic_name = data = None
        data_arr = raw_data.decode(FORMAT).split(SEPERATOR)

        # Message Format: TYPE$TOPIC$DATA (DATA is optional)
        client_type = data_arr[0]  # First element is client type (Publisher or Subscriber)
        topic_name = data_arr[1]  # Second element is topic name
        if len(data_arr) == 3:  # If there are three elements
            data = data_arr[2]  # Third element is data

        return client_type, topic_name, data

    def __process(self, addr: tuple[str, int], raw_data: bytes):
        client_type, topic_name, data = self.__extract_data(raw_data)

        if client_type.lower() == "pub":  # If the client is publisher
            self.topics.update({topic_name: data})
            self.__log("Data is published to the topic \'{}\'".format(topic_name))

        else:  # If the client is subscriber
            self.subscribers.update({addr: topic_name})
            self.__log("\'{}:{}\' is subscribed to the topic \'{}\'".format(
                addr[0], addr[1], topic_name))

    def __listen_thread(self):
        while True:  # Infinite loop
            try:
                raw_data, client_addr = self.socket.recvfrom(BUFFER_SIZE)  # Receive message
                self.__process(client_addr, raw_data)  # Handle the message
                self.socket.sendto(ACK.encode(FORMAT), client_addr)  # Send ACK
            except:
                # Error occurred because subscriber is left.
                time.sleep(0.25)
                pass

    def __speak_thread(self):
        while True:  # Infinite loop
            send_to_n_subs = 0  # number of subscribers notified

            # Search for updated topics
            for topic_name_search, data in self.topics.items():
                if data is not None:
                    
                    # Search for subscribers
                    for client_addr, topic_name in self.subscribers.items():
                        if topic_name == topic_name_search:
                            try:
                                self.socket.sendto(str(data).encode(FORMAT), client_addr)
                                send_to_n_subs += 1
                            except:
                                self.subscribers.pop(client_addr)
                                self.__log("Subscriber in {}:{} is dead, removed from the subscriber map".format(
                                    client_addr[0], client_addr[1]))

                    # Delete data if it is sent to a subscriber(s)
                    if send_to_n_subs != 0:
                        self.topics.update({topic_name_search: None})
                        self.__log("Subscribers of the topic \'{}\' are notified".format(topic_name_search))
                        send_to_n_subs = 0
            
            # Rest a bit
            time.sleep(1)

    def run(self):
        # Initialize socket
        self.__log("Broker is started")
        self.socket.bind((HOST, PORT))

        # Start threads
        Thread(target=self.__listen_thread).start()
        Thread(target=self.__speak_thread).start()


if __name__ == "__main__":
    broker = Broker()
    broker.run()
    