import socket, threading #модуль потока

host=(socket.gethostname(),7976)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #инициализировали наш сокет для отправки сообщений на тср соединении
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #чтобы заново использовать тот же адрес
server.bind((host)) #инициализировали сервер связанный с заданными хостом и портом
server.listen() #сервер слушает/ожидает входящего соединения

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message) #метод для отправки send

def handle(client):
    while True:
        try:
            message = client.recv(1024) # это для размера сообщений клиента 1024
            broadcast(message) 
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast('{} ушел'.format(nickname).encode('utf-8')) 
            nicknames.remove(nickname)
            break

def receive(): #делаем ожидание тср соединения
    while True:
        client, address= server.accept() #принимаем входящее подключение от клиента
        print('Соединение с {}'.format(str(address)))
        client.send('NICKNAME'.encode('utf-8')) 
        nickname=client.recv(1024).decode('utf-8')
        clients.append(client)
        nicknames.append(nickname)
        print('Имя пользователя {}'.format(nickname))
        broadcast("{} присоединился".format(nickname).encode('utf-8'))
        client.send('Подключен к серверу '.encode('utf-8'))
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()




receive()
