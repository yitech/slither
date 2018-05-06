import skeleton as sk
import sys
import os



class envir:
    os.system('clear')
    def __init__(self, windows_x, windows_y):
        self.unit = {'ceiling': '#', 'wall': '#', 'empty': ' ', 'snake': 'O', 'food': '@'}
        self.windows_x = windows_x
        self.windows_y = windows_y

    def window(self,snake_body,food):
        for j in range(0,self.windows_y):
            row = ''
            for i in range(0,self.windows_x):
                if i==0 or i==self.windows_x-1:
                    row = row + self.unit['wall']
                elif j==0 or j==self.windows_y-1:
                    row = row + self.unit['ceiling']
                else:
                    if (i,j) in snake_body:
                        row = row + self.unit['snake']
                    elif (i,j)==tuple(food):
                        row = row + self.unit['food']
                    else:
                        row = row + self.unit['empty']
            print(row)

