import socket
import time
import threading
import ServerBackend as sb

HOST = 'localhost'
PORT = 5278




class DynamicServer(sb.Backend):
    def __init__(self,HOST,PORT):
        super(DynamicServer,self).__init__()
        self.HOST = HOST
        self.PORT = PORT
        self.thread_a = threading.Thread(target=self.ServerAccept,)
        self.thread_s = threading.Thread(target=self.ServerSend,)


    def ActivateServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen()
        print('Wait for connecting...')
        self.conn, addr = server.accept()
        print('New connection:', addr)
        self.thread_a.start()
        self.thread_s.start()
        server.close()

    def ServerAccept(self):
        while True:
            direction = self.conn.recv(1024)
            if not direction:
                print("Client break!")
                break
            d = direction.decode('utf-8')
            try:
                self.head.state = self._directions[d]
            except:
                pass
            #print('Recieve:', d)

    def ServerSend(self):
        self.init_game()
        while self._isAlive:
            self.slide_game()
            self.SnakeCoordSend()
            time.sleep(0.2)

    def SnakeCoordSend(self):
        Squeeze = [b[0] for b in self.body] + [b[1] for b in self.body] + self.food
        self.conn.send(bytearray(Squeeze))



Player1 = DynamicServer(HOST,PORT)
Player1.ActivateServer()