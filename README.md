# Slither on Terminal

This project is a realization of playing Slither on terminal.  The environment is Ubuntu 17.04 and 
Python 3.6.  The project is still developing but it can be executed and played now!  Just open the 
terminal and type:
```
git clone https://github.com/yitech/slither.git
cd slither
python main,py

```

# Introduction

There are some script to support the project:
main.py is the execute file.
skeleton.py construct the snake structure
kbhit.py is the instance input where fork by https://github.com/gbarbon/python-asip
printing.py define how the backend output on terminal
control.py conbine the script above to form a complete game



## Skeleton.py

Here is the snake structure, for example, suppose there is a snake is going to left with length 4:

```
A[Head, left] --> B[Body1, left]
B --> C[Body2, left]
C --> D[Body3, left]

```

Each of the block are define as:
```
class block:
	def __init__(self,location,state):
		self.location = location
		self.state = state
		self.link = None
```
Then we only need to push each block according to its state ( up, down, left, right ).

## kbhit.py & control.py
Use kbhit.py to change the head's state, and then push and update each block by previous block.
It can achieve the changing direction effect.
```
A[Head, left] --recieve up--> B[Body1, left]
B --> C[Body2, left]
C --> D[Body3, left]

A[Head, up] --> B[Body1, left]
B --> C[Body2, left]
C --> D[Body3, left]
```
Push each block and update the state of the block at back.
```
A[Head, up] --> B[Body1, up]
B --> C[Body2, left]
C --> D[Body3, left]
```

## printing.py

This script is responsible for output on terminal. Fork with the backend logic, it requires to read the
information of the current game and arrange the game state.
![Screenshot while playing](https://github.com/yitech/slither/blob/master/Screenshot.png)













