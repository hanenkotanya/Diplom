import socket, threading

nickname=input('Введите имя пользователя: ')
host=(socket.gethostname(),7976)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(host)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Ошибка')
            client.close()
            break


def write():
    while True:
        message='{}:{}'.format(nickname,input(''))
        client.send(message.encode('utf-8'))
receive_thread=threading.Thread(target=receive) #к потоку будет множественное подключение 
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

