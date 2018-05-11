import skeleton as sk
import kbhit as kbh
import time,os,sys
import threading
import random

window_x = sk.window_x
window_y = sk.window_y
random_food = lambda:[random.randrange(1,window_x-1),random.randrange(1,window_y-1)]

class Backend:
    def __init__(self):
        self.windows_x = window_x
        self.windows_y = window_y
        self.snake = sk.snake()
        self.body = []
        self.food = random_food()
        self.__isAlive = True
        self.__starttime = time.time()

    def initializeGame(self):
        self.snake.get_food()
        wait_key = threading.Thread(target=control, args=(self.snake.head,))
        wait_key.start()

    def GameSlide(self):
        self.snake.move()
        self.body = self.snake.get_list()
        #print(snake.head.location, self.body, self.food)
        self.alive()
        if self.snake.head.location == self.food:
            self.snake.get_food()
            self.food = random_food()
    def endGame(self):
        time.sleep(1)
        self.summarize()
        sys.exit()

    def alive(self):
        head = self.snake.head
        if head.location[0] in [0,window_x-1] or head.location[1] in [0,window_y-1]:
            self.__isAlive = False
        if len(self.body)!=len(set(self.body)):
            self.__isAlive = False
    def summarize(self):
        t = time.time()-self.__starttime
        l = len(self.body)
        print('Playing time:%.2f'%t)
        print('snake length:',l)
        print('Press Esc to exit.')
        time.sleep(3)


def control(head):
    directions = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    keys = {v: k for k, v in directions.items()}
    illegal_key = {'w':'s','s':'w','a':'d','d':'a'}
    kb = kbh.KBHit()
    while True:
        if kb.kbhit():
            c = kb.getch()
            if ord(c)==27:
                break
            legal = directions.copy()
            del legal[illegal_key[keys[head.state]]]
            try:
                head.state = legal[c]
            except:
                pass
    kb.set_normal_term()







