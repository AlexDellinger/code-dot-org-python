"""Stage 15: Puzzle 9 of 10

Can you re-create the `draw house(length)` function without help? Try it,
and then draw a row of houses. Hint: replace 'pass' with your code.

"""

import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level90')

def draw_square(length):
    for count in range(4):
        z.move_forward(length)
        z.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        z.move_forward(length)
        z.turn_right(120)

def draw_house(length):
    draw_square(length)
    z.fd(length)
    z.rt(30)
    draw_triangle(length)
    z.rt(60)
    z.fd(length)
    z.rt()
    z.fd(length)
    z.lt(180)

for counter in range(50,151,50):
    draw_house(counter)                 
z.check()
