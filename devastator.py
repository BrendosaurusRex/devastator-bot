'''
Devastator Robot GPIO Code
'''
import curses
import RPi.GPIO as G
import os
import time

# Set numbering mode and define output pins
G.setmode(G.BOARD)
G.setup(7,  G.OUT) # Right Back
G.setup(11, G.OUT) # Right Forward
G.setup(13, G.OUT) # Left Forward
G.setup(15, G.OUT) # Left Back
G.setup(29, G.OUT)

for x in range(1, 4):
    G.output(29, False)
    time.sleep(0.25)
    G.output(29, True)
    time.sleep(0.5)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()

        # Define state variable
        #state = 0   # 1 = Forward; 2 = Backward
                    # 3 = Right; 4 = Left
        
        if char == ord('q'):
            break
        if char == ord('S'):
            os.system('sudo shutdown now')

        elif char == curses.KEY_DOWN:

            G.output(7,  True)
            G.output(11, False)
            G.output(13, False)
            G.output(15, True)
            
        elif char == curses.KEY_RIGHT:

            G.output(7,  True)
            G.output(11, False)
            G.output(13, True)
            G.output(15, False)
            
        elif char == curses.KEY_LEFT:

            G.output(7,  False)
            G.output(11, True)
            G.output(13, False)
            G.output(15, True)
            
        elif char == curses.KEY_UP:

            G.output(7,  False)
            G.output(11, True)
            G.output(13, True)
            G.output(15, False)
            
        elif char == 10:
            G.output(7,  False)
            G.output(11, False)
            G.output(13, False)
            G.output(15, False)

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    G.cleanup()


