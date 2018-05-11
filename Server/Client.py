import socket
import os
import kbhit
import threading
import ServerBackend as sb

HOST = 'localhost'
PORT = 5278


class DynamicClient:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.kb = kbhit.KBHit()
        self.thread_s = threading.Thread(target=self.ClientSend, )
        self.thread_a = threading.Thread(target=self.ClientAccept, )
        self.body = []
        self.food = []
        self.Graphic = GraphicGUI()

    def ActivateClient(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        self.thread_s.start()
        self.thread_a.start()

    def ClientSend(self):
        while True:
            direction = self.kb.getch()
            self.client.send(direction.encode('utf-8'))

    def ClientAccept(self):
        while True:
            byte_state = self.client.recv(1024)
            if not byte_state:
                print('Client Break!')
                break
            sqzState = list(byte_state)
            self.food = sqzState[-2:]
            sqzState = sqzState[0:-2]
            n = len(sqzState) // 2
            state = [(sqzState[i], sqzState[n + i]) for i in range(0, n)]
            self.body = state
            self.Graphic.termin(self.body,self.food)
            #print('recv:', self.body, self.food)


class GraphicGUI(sb.Backend):
    os.system('clear')

    def __init__(self):
        super(GraphicGUI,self).__init__()
        self.unit = {'ceiling': '#', 'wall': '#', 'empty': ' ', 'snake': 'O', 'food': '@'}


    def termin(self,body,food):
        for j in range(0,self.window_y):
            row = ''
            for i in range(0,self.window_x):
                if i==0 or i==self.window_x-1:
                    row = row + self.unit['wall']
                elif j==0 or j==self.window_y-1:
                    row = row + self.unit['ceiling']
                else:
                    if (i,j) in body:
                        row = row + self.unit['snake']
                    elif (i,j)==tuple(food):
                        row = row + self.unit['food']
                    else:
                        row = row + self.unit['empty']
            print(row)


Player1 = DynamicClient(HOST, PORT)
Player1.ActivateClient()
