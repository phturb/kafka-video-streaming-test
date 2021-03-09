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
    stream_buffer_maxsize=2
)

updated_video_topic = app.topic('updated_video', value_type=bytes, value_serializer='raw', retention=0.06)

@app.agent(updated_video_topic)
async def greet(greetings):
    async for greeting in greetings:
        # jpeg-encoded byte array into numpy array
        np_array = np.frombuffer(greeting, dtype=np.uint8)
        # decode jpeg-encoded numpy array 
        image = cv2.imdecode(np_array, 1)

        # show image
        cv2.imshow("updated", image)
        cv2.waitKey(1)