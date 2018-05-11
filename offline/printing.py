import skeleton as sk
import sys
import os,time
import control as c




class envir(c.Backend):
    os.system('clear')
    def __init__(self):
        super(envir,self).__init__()
        self.unit = {'ceiling': '#', 'wall': '#', 'empty': ' ', 'snake': 'O', 'food': '@'}

    def GraphicAPI(self,fps):
        self.initializing()
        self.initializeGame()
        while self._Backend__isAlive:
            self.GameSlide()
            self.window()
            time.sleep(fps)
        self.endGame()

    def window(self):
        for j in range(0,self.windows_y):
            row = ''
            for i in range(0,self.windows_x):
                if i==0 or i==self.windows_x-1:
                    row = row + self.unit['wall']
                elif j==0 or j==self.windows_y-1:
                    row = row + self.unit['ceiling']
                else:
                    if (i,j) in self.body:
                        row = row + self.unit['snake']
                    elif (i,j)==tuple(self.food):
                        row = row + self.unit['food']
                    else:
                        row = row + self.unit['empty']
            print(row)

    def initializing(self):
        s = 'initializing'
        for i in range(0,3):
            s = s + '.'
            print(s)
            time.sleep(0.5)
            os.system('clear')
        print('Press wasd to control the slither.')
        time.sleep(1)

