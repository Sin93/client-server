# import asyncio
# import socketio
#
# sio = socketio.Client()
#
#
# @sio.event
# def connect():
#     print('connection established')
#
#
# @sio.event
# def my_message(data):
#     print('message received with ', data)
#     sio.emit('my_message', {'response': data})
#
#
# @sio.event
# def disconnect():
#     print('disconnected from server')
#
#
# sio.connect('http://localhost:5000')
# msg = input()
# my_message(msg)
# sio.wait()


import asyncio
import socketio
# from multiprocessing import Process, Pool

sio = socketio.AsyncClient()


# def wait_input():
#     return input('Введите сообщение: ')
#
#
# async def i_am_active():
#     while True:
#         await sio.call('my_message', {'response': 'active'})
#         await sio.sleep(15)


@sio.event
async def connect():
    print('connection established')


@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.call('my_message', {'response': data})


@sio.event
async def print_serv_msg(data):
    print(data)
    return "OK"


@sio.event
async def disconnect():
    print('disconnected from server')


async def main():
    await sio.connect('http://localhost:7777')
    while True:
        msg = input('Введите сообщение: ')
        if msg == 'exit':
            break
        else:
            await my_message(msg)


if __name__ == '__main__':
    asyncio.run(main())
