import skeleton as sk
import kbhit as kbh
import printing as ptg
import time,os,sys
import threading
import random

window_x = sk.window_x
window_y = sk.window_y
random_food = lambda:[random.randrange(1,window_x-1),random.randrange(1,window_y-1)]

class playing_inform:
    def __init__(self):
        self.snake = sk.snake()
        self.body = []
        self.food = random_food()
        self.__env = ptg.envir(window_x,window_y)
        self.__alive = True
        self.__starttime = time.time()
    def game(self,fps=1):
        self.initializing()
        snake = self.snake
        leading = snake.head
        snake.get_food()
        wait_key = threading.Thread(target=control, args=(leading,))
        wait_key.start()
        while self.__alive:
            snake.move()
            self.body = snake.get_list()
            self.__env.window(self.body, self.food)
            #print(snake.head.location,self.body,self.food)
            time.sleep(fps)

            self.alive()
            if snake.head.location==self.food:
                snake.get_food()
                self.food = random_food()
        time.sleep(1)
        self.summarize()
        sys.exit()
    def initializing(self):
        s = 'initializing'
        for i in range(0,3):
            s = s + '.'
            print(s)
            time.sleep(0.5)
            os.system('clear')
        print('Press wasd to control the slither.')
        time.sleep(1)

    def alive(self):
        head = self.snake.head
        if head.location[0] in [0,window_x-1] or head.location[1] in [0,window_y-1]:
            self.__alive = False
        if len(self.body)!=len(set(self.body)):
            self.__alive = False
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







