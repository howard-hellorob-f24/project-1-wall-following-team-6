import time
from mbot_bridge.api import MBot

robot = MBot()

def drive_square():
    for i in range(4):
        robot.drive(1.0,0,0)
        time.sleep(1)
        robot.drive(0,0,1.57)
        time.sleep(1)

def drive_square2():
    robot.drive(1.0,0,0)
    time.sleep(1)
    robot.drive(0,1,0)
    time.sleep(1)
    robot.drive(-1,0,0)
    time.sleep(1)
    robot.drive(0,-1,0)
    time.sleep(1)

def drive_square_three_times():
    for i in range(3):
        drive_square2()

try:
    drive_square_three_times()

except:
    robot.stop()
