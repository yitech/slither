import os,sys
import random

window_x = 60
window_y = 30

random_location = lambda:[random.randrange(10,window_x-10),random.randrange(5,window_y-5)]
random_key = lambda:['w','s','a','d'][random.randrange(0,4)]

class block:
    def __init__(self,location,state):
        self.location = location
        self.state = state
        self.link = None

def move_block(block):
    L = block.location
    if block.state == 'up':
        block.location = [L[0],L[1]-1]
    elif block.state == 'down':
        block.location = [L[0],L[1]+1]
    elif block.state == 'left':
        block.location = [L[0]-1,L[1]]
    elif block.state == 'right':
        block.location = [L[0]+1,L[1]]


def success_block(block,state):
    block.state = state


class snake:
    def __init__(self):
        self.__directions = {'w':'up','s':'down','a':'left','d':'right'}
        self.head = block(random_location(),self.__directions[random_key()])
        self.tail = self.head

    def move(self):
        tmp = self.head
        c = 0
        while tmp!=None:
            move_block(tmp)
            if c>0:
                success_block(tmp,prvs_state)
            prvs_state = tmp.state
            tmp = tmp.link
            c = c + 1

    def get_food(self):
        L = self.tail.location
        S = self.tail.state
        if S == 'up':
            self.tail.link = block([L[0],L[1]+1],S)
        elif S == 'down':
            self.tail.link = block([L[0],L[1]-1],S)
        elif S == 'left':
            self.tail.link = block([L[0]+1,L[1]],S)
        elif S == 'right':
            self.tail.link = block([L[0]-1,L[1]],S)
        self.tail = self.tail.link
#Test Unit
"""
a = snake()
print(a.head.location)
print(a.head.state)
a.get_food()
print(a.head.link.location)
print(a.head.link.state)
a.move()
print('\n')
print(a.head.location)
print(a.head.state)
print(a.head.link.location)
print(a.head.link.state)
"""