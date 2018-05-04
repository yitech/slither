import skeleton as sk
import kbhit as kbh
import time
import threading


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

def game(fps=1):
    snake = sk.snake()
    leading = snake.head
    wait_key = threading.Thread(target=control,args=(leading,))
    wait_key.start()

    while True:
        print(snake.head.location,snake.head.state)
        time.sleep(fps)
        snake.move()






if __name__=='__main__':
    game()
