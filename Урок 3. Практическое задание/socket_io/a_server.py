import socketio
from aiohttp import web

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
async def chat_message(sid, data):
    print("message ", data)


@sio.event
async def my_message(sid, data):
    print('message ', data)
    await sio.emit('print_serv_msg', {'data': f'Принято сообщение: {data}'}, room=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    web.run_app(app, host='localhost', port=7777)
