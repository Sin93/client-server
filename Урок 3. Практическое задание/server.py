import argparse
import socket
import json
from select import select


tasks = []
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_addr, port))
    server_socket.listen()

    while True:
        yield 'read', server_socket
        client_socket, addr = server_socket.accept()
        print(f'connection from: {addr}')

        tasks.append(client(addr, client_socket))


def client(addr, client_socket):
    while True:
        yield 'read', client_socket
        request = client_socket.recv(1048576)
        data = json.loads(request.decode('utf-8'))
        if not request:
            break
        else:
            if data['action'] == 'presence':
                user = data['user']['account_name']
                print(f'is presence! user: {user}, addr: {addr}')
            else:
                text, user = data['text'], data['user']['account_name']
                print(f'Сообщение: {text}, было отправлено пользователем: {user}, адрес {addr}')

        answer = {'status': 200}
        response = json.dumps(answer).encode('utf-8')
        yield 'write', client_socket
        client_socket.send(response)

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            elif reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Нет активных подключений.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument('-p', '--port', help='Server port')
    parser.add_argument('-a', '--addr', help='Server ip address')
    args = parser.parse_args()
    port = int(args.port) if args.port else 7777
    server_addr = args.addr if args.addr else 'localhost'
    print(port, server_addr)

    tasks.append(server())
    event_loop()
