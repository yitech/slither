import skeleton as sk
import kbhit as kbh
import printing as ptg
import time
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
        self.env = ptg.envir(window_x,window_y)
    def game(self,fps=1):
        snake = self.snake
        leading = snake.head
        snake.get_food()
        wait_key = threading.Thread(target=control, args=(leading,))
        wait_key.start()
        while True:
            self.env.window(self.body,self.food)
            self.body = snake.get_list()
            time.sleep(fps)
            snake.move()
            if snake.head.location==self.food:
                snake.get_food()
                self.food = random_food()




def control(head):
    directions = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    keys = {v: k for k, v in directions.items()}
    illegal_key = {'w':'s','s':'w','a':'d','d':'a'}
    kb = kbh.KBHit()
    print('Use wsad to control the snake')

    while True:
        if kb.kbhit():
            c = kb.getch()
            legal = directions.copy()
            del legal[illegal_key[keys[head.state]]]
            try:
                head.state = legal[c]
            except:
                pass
    kb.set_normal_term()







