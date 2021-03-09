import faust
import cv2
import time
import random
import sys
import numpy as np
import base64

app = faust.App(
    __name__,
    broker='kafka://localhost',
    store='memory://',
    value_serializer='raw',
)

raw_video_topic = app.topic('small_raw_video', value_type=bytes, value_serializer='raw', retention=0.06)

@app.task()
async def publish_greetings():
    video = cv2.VideoCapture(0)
    frame_no = 1
    while video.isOpened():
        _, frame = video.read()
        # pushing every 3rd frame
        frame_bytes = cv2.imencode(".jpg", frame)[1].tobytes()
        await raw_video_topic.send(value=frame_bytes, timestamp=frame_no)
        time.sleep(0.01)
        frame_no += 1