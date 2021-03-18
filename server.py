import socketio
import eventlet
import json
import os
import time

sio = socketio.Server(cors_allowed_origins=[])
app = socketio.WSGIApp(sio)


@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)
    time.sleep(1)


@sio.on('__TEST')
def message(sid, data):
    print(sid, data)
    sio.emit('__TEST', data)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('192.168.42.105', 2494)), app)
