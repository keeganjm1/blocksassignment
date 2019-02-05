import cozmo
import asyncio
from cozmo.util import degrees, distance_mm
from colors import Colors
from woc import WOC
import _thread
import time



def cozBlockProgram(robot: cozmo.robot.Robot):
    tappedCube = 0
    robot.world.connect_to_cubes()
    robot.say_text("Hi there")
    while tappedCube < 3:

        tapped_event = robot.wait_for(cozmo.objects.EvtObjectTapped, timeout=None)


        if tapped_event.obj.object_id == 1:

            print("cube with object_id %s was tapped" % tapped_event.obj.object_id)
            robot.say_text("Block 1 was tapped")
        elif tapped_event.obj.object_id == 2:
            robot.say_text("Cube 2 was tapped")
            print("cube with object_id %s was tapped" % tapped_event.obj.object_id)
        else:
            robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()
            print("cube with object_id %s was tapped" % tapped_event.obj.object_id)

        tappedCube = tappedCube +1
        print("tapped count is %s" %tappedCube)
cozmo.run_program(cozBlockProgram)
