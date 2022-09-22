import json  # for converting from string to list
import socket  # for communicating with the broker
import argparse  # for parsing the program argument(s)

# Communication constants
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 8000
BUFFER_SIZE = 4096

# Message constants
ACK = "ACK"
FORMAT = "utf-8"
SEPERATOR = "$"
TOPIC = "image_processor"


def __generate_subscribe_message(topic_name: str = "default"):
    return SEPERATOR.join(["SUB", topic_name])


def __string_to_array(string_data: str):
    return json.loads(string_data)


if __name__ == "__main__":
    """
        Description:
            - aim is to write a subscriber client, which communicates in UDP
            - the client subscribes to a topic in the broker, then receives ACK
            - afterwards, the client listens the topic forever

        Attention:
            - a subscriber client can only be subscribed to a single topic
            - topic name is given as a program argument
            
        Sample Use:
            python sub.py -topic=image_processor
    """
    # write your code here
