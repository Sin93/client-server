from socket import *
import sys
import argparse
import json

from datetime import datetime

PRESENCE_MSG = {
    "action": "presence",
    "time": datetime.timestamp(datetime.now()),
    "type": "status",
    "user": {
            "account_name": "Sin93",
            "status": "Yep, I am here!"
    }
}

MESSAGE = {
            'action': 'message',
            'user': {
                "account_name": "Sin93"
            },
            'text': ''
        }


def main():
    sock = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    sock.connect((server_addr, port))  # Соединиться с сервером
    sock.send(json.dumps(PRESENCE_MSG).encode('utf-8'))
    data = json.loads(sock.recv(10000).decode('utf-8'))
    assert data['status'] == 200
    while True:
        msg_text = input()
        message = MESSAGE
        message['text'] = msg_text
        if msg_text == 'exit':
            sock.close()
            sys.exit()
        else:
            sock.send(json.dumps(message).encode('utf-8'))
            data = json.loads(sock.recv(1000000).decode('utf-8'))
            status = data['status']
            if status == 200:
                print(f'Сообщение доставлено, ответ сервера: {status}, длина сообщения: {len(data)} байт')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument('-p', '--port', help='Server port')
    parser.add_argument('-a', '--addr', help='Server ip address')
    args = parser.parse_args()
    port = int(args.port) if args.port else 7777
    server_addr = args.addr if args.addr else 'localhost'
    print(port, server_addr)
    main()
