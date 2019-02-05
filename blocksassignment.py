import cozmo
import asyncio
from cozmo.util import degrees, distance_mm
from colors import Colors
from woc import WOC
import _thread
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id


def cozBlockProgram(robot: cozmo.robot.Robot):
    tappedCube = 0
    robot.world.connect_to_cubes()
    robot.camera.image_stream_enabled = True
    robot.say_text("Hi there")
    #cube = robot.world.wait_for_observed_light_cube(timeout=30)

    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)

    while tappedCube < 3:
        #look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        tapped_event = robot.wait_for(cozmo.objects.EvtObjectTapped, timeout=None)
        #robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

        if tapped_event.obj.object_id == 1:
            robot.set_all_backpack_lights(Colors.RED)
            cube2.set_lights(cozmo.lights.red_light)
            #look_around.stop()
            print("cube with object_id %s was tapped" % tapped_event.obj.object_id)
            robot.say_text("Block 1 was tapped")



        elif tapped_event.obj.object_id == 2:
            robot.set_all_backpack_lights(Colors.BLUE)
            cube3.set_lights(cozmo.lights.blue_light)
            #look_around.stop()
            robot.say_text("Cube 2 was tapped")
            print("cube with object_id %s was tapped" % tapped_event.obj.object_id)

        else:
            robot.set_all_backpack_lights(Colors.GREEN)
            cube1.set_lights(cozmo.lights.green_light)
            #look_around.stop()
            robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()
            print("cube with object_id %s was tapped" % tapped_event.obj.object_id)


        tappedCube = tappedCube +1
        print("tapped count is %s" %tappedCube)
cozmo.run_program(cozBlockProgram)
