import control
import sys

G = control.playing_inform()
if len(sys.argv)<2:
    fps = 0.5

if sys.argv[1].startswith('--fps='):
    fps = float(sys.argv[1][6:])

if __name__=='__main__':
    G.game(fps)