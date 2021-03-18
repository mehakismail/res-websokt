import time
import json
import socketio
import time

sio = socketio.Client()
sio.connect('http://192.168.42.105:2494')


@sio.on('connect')
def connect():
    print('connection established')


@sio.on('__TEST')
def message(data):
    print(data)
