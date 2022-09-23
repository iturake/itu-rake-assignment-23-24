import random
import socket  # for communicating with the broker
import time  # for sleeping 0.5 seconds

# Communication constants
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 8000
BUFFER_SIZE = 4096

# Message constants
ACK = "ACK"
FORMAT = "utf-8"
SEPERATOR = "$"
TOPICS = ["image_processor", "robotic_arm", "path_finder"]

# Data formats
DATA_FORMATS = {"image_processor": [16, 16],
                "robotic_arm": [6, 3],
                "path_finder": [25, 2]}


def __get_random_topic():
    return random.choice(TOPICS)


def __generate_random_data_for_topic(topic_name: str):
    dimensions = DATA_FORMATS.get(topic_name)
    data = [[random.randint(0, 255) for _ in range(dimensions[1])] for _ in range(dimensions[0])]
    return data


def __generate_publish_message(topic_name: str = "default", data=[0]):
    return SEPERATOR.join(["PUB", topic_name, str(data)])


if __name__ == "__main__":
    """
        Description:
            - aim is to write a publisher client, which communicates in UDP
            - publishes data to a random topic in the broker in every 0.5 seconds
            - receives ACK from the broker after publishing data

        Sample Use:
            python pub.py
    """
    # write your code here
