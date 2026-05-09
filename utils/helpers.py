import time
import os

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def elapsed(self):
        return time.time() - self.start_time


def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def format_coordinates(lat, lon):
    return f"Latitude: {lat}, Longitude: {lon}"
