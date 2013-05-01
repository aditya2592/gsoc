from morse.builder import *

# Add a robot with a position sensor and a motion controller
r2d2 = ATRV()

pose = Pose()
pose.add_interface('socket')
r2d2.append(pose)

motion = Waypoint()
motion.add_interface('socket')
r2d2.append(motion)


# Environment
env = Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
