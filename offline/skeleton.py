import random

window_x = 60
window_y = 20

random_location = lambda:[random.randrange(10,window_x-10),random.randrange(5,window_y-5)]
random_key = lambda:['w','s','a','d'][random.randrange(0,4)]

class block:
    def __init__(self,location,state):
        self.location = location
        self.state = state
        self.link = None
    def copy(self):
        x = block(self.location,self.state)
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
    def replace(self,b):
        self.location= b.location
        self.state = b.state


class snake:
    def __init__(self):
        self.__directions = {'w':'up','s':'down','a':'left','d':'right'}
        self.head = block(random_location(),self.__directions[random_key()])
        self.__tail = self.head

    def move(self):
        tmp = self.head
        state_buffer = tmp.state
        c = 0
        while tmp!=None:
            tmp.move_block()
            if c>0:
                prvs = state_buffer
                state_buffer = tmp.state
                tmp.state = prvs
            tmp = tmp.link
            c = c+1

    def get_list(self):
        tmp = self.head
        snake_list = []
        while tmp!=None:
            snake_list.append(tuple(tmp.location))
            tmp = tmp.link
        return snake_list

    def get_food(self):
        L = self.__tail.location
        S = self.__tail.state
        if S == 'up':
            self.__tail.link = block([L[0],L[1]+1],S)
        elif S == 'down':
            self.__tail.link = block([L[0],L[1]-1],S)
        elif S == 'left':
            self.__tail.link = block([L[0]+1,L[1]],S)
        elif S == 'right':
            self.__tail.link = block([L[0]-1,L[1]],S)
        self.__tail = self.__tail.link
