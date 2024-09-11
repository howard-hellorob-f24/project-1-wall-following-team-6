import time
from mbot_bridge.api import MBot

robot = MBot()

def drive_square():
    for i in range(4):
        robot.drive(1.0,0,0)
        time.sleep(1)
        robot.drive(0,0,1.57)
        time.sleep(1)

def drive_square_three_times():
    for i in range(3):
        drive_square()

drive_square_three_times()

"""

TODO: (P1.1) Write code to make the robot drive in a square. Then,
modify your code so that the robot drives in a square 3 times.

HINT: A function to send velocity commands to the robot is provided. To
use it, use the following code:

    robot.drive(vx, vy, wz);

Replace vx, vy, and wz with the velocity in the x direction (vx), y
direction (vy), and the angular velocity (wz). You can also use this code:

    time.sleep(secs);

to sleep for "secs" seconds (replace with desired number of seconds).
"""

robot.stop()
