"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Michael Kelly.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

blueturtle = rg.SimpleTurtle('turtle')
blueturtle.pen = rg.Pen('midnight blue', 3)
blueturtle.speed = 200

size = 100

for k in range(50):
    blueturtle.draw_circle(size)
    blueturtle.pen_up()
    blueturtle.left(90)
    blueturtle.forward(1)
    blueturtle.pen_down()
    size = size - 1

greenTurtle = rg.SimpleTurtle('turtle')
greenTurtle.pen = rg.Pen('green', 5)
greenTurtle.speed = 200

length = 700
greenTurtle.pen_up()
greenTurtle.backward(350)
greenTurtle.right(90)
greenTurtle.forward(225)
greenTurtle.left(90)

for n in range(300):
    greenTurtle.pen_down()
    greenTurtle.forward(length)
    greenTurtle.left(120)

    length = length + 5

window.close_on_mouse_click()
