from time import sleep
from flask import Flask
from flask_cors import CORS
import threading

app = Flask(__name__)
cors = CORS(app)


thread_event = threading.Event()


def backgroundTask():
    while thread_event.is_set():
        print('Background task running!')
        sleep(5)


@app.route("/start", methods=["POST"])
def startBackgroundTask():
    try:
        thread_event.set()
        thread = threading.Thread(target=backgroundTask)
        thread.start()

        return "Background task started!"
    except Exception as error:
        return str(error)


@app.route("/stop", methods=["POST"])
def stopBackgroundTask():
    try:
        thread_event.clear()
        return "Background task stopped!"
    except Exception as error:
        return str(error)
