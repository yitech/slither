import random
import sys, time

window_x = 60
window_y = 20

random_location = lambda: [random.randrange(10, window_x - 10), random.randrange(5, window_y - 5)]
random_key = lambda: ['w', 's', 'a', 'd'][random.randrange(0, 4)]


class Snake:

    def __init__(self):
        self._directions = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
        self.head = Block(random_location(), self._directions[random_key()])
        self._tail = self.head

    def move(self):
        tmp = self.head
        state_buffer = tmp.state
        c = 0
        while tmp != None:
            tmp.move_block()
            if c > 0:
                prvs = state_buffer
                state_buffer = tmp.state
                tmp.state = prvs
            tmp = tmp.link
            c = c + 1

    def get_list(self):
        tmp = self.head
        snake_list = []
        while tmp != None:
            snake_list.append(tuple(tmp.location))
            tmp = tmp.link
        return snake_list

    def get_food(self):
        L = self._tail.location
        S = self._tail.state
        if S == 'up':
            self._tail.link = Block([L[0], L[1] + 1], S)
        elif S == 'down':
            self._tail.link = Block([L[0], L[1] - 1], S)
        elif S == 'left':
            self._tail.link = Block([L[0] + 1, L[1]], S)
        elif S == 'right':
            self._tail.link = Block([L[0] - 1, L[1]], S)
        self._tail = self._tail.link


random_food = lambda: [random.randrange(1, window_x - 1), random.randrange(1, window_y - 1)]


class Backend(Snake):

    def __init__(self):
        super(Backend, self).__init__()
        self.window_x = window_x
        self.window_y = window_y
        self.body = []
        self.food = random_food()
        self._isAlive = True

    def init_game(self):
        self.get_food()

    def slide_game(self):
        self.move()
        self.body = self.get_list()
        self.is_alive()
        if self.head.location == self.food:
            self.get_food()
            self.food = random_food()

    def end_game(self):
        time.sleep(1)
        self.summarize()
        sys.exit()

    def is_alive(self):
        head = self.head
        if head.location[0] in [0, window_x - 1] or head.location[1] in [0, window_y - 1]:
            self._isAlive = False
        if len(self.body) != len(set(self.body)):
            self._isAlive = False

    def summarize(self):
        t = time.time()
        l = len(self.body)
        print('Playing time:%.2f' % t)
        print('snake length:', l)
        print('Press Esc to exit.')
        time.sleep(3)


class Block:
    def __init__(self, location, state):
        self.location = location
        self.state = state
        self.link = None

    def copy(self):
        x = Block(self.location, self.state)
        return x

    def move_block(self):
        L = self.location
        S = self.state
        if S == 'up':
            self.location = [L[0], L[1] - 1]
        elif S == 'down':
            self.location = [L[0], L[1] + 1]
        elif S == 'left':
            self.location = [L[0] - 1, L[1]]
        elif S == 'right':
            self.location = [L[0] + 1, L[1]]

    def replace(self, b):
        self.location = b.location
        self.state = b.state


