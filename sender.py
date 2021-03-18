import time
# import RPi.GPIO as GPIO
import json
import socketio
import time
import random

sio = socketio.Client()
sio.connect('http://192.168.42.105:5000')


# @sio.on('connect')
# def connect():
#     print('connection established')
#
#
# while True:
#     temp = random.randint(30, 90)
#     hum = random.randint(20, 100)
#     data = {'temp': temp, 'hum': hum}
#
#
#     @sio.on('__TEST')
#     def message(data):
#         sio.emit('__TEST', data)
#
#     time.sleep(3)
