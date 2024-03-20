from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28


# create the Robot instance.
robot = Robot()



leftMotor = robot.getDevice('Lmotor')
rightMotor = robot.getDevice('Rmotor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)


# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    # read sensors outputs
   

    # detect obstacles

    # initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed  = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED
    # modify speeds according to obstacles

    # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)