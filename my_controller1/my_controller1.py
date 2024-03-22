
from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# initialize devices
ps = []
psNames = [
    'sensord1' ,
     'sensord2'
]

for i in range(2):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

FleftMotor = robot.getDevice('FLmotor')
FrightMotor = robot.getDevice('FRmotor')
BleftMotor = robot.getDevice('BLmotor')
BrightMotor = robot.getDevice('BRmotor')

FleftMotor.setPosition(float('inf'))
FrightMotor.setPosition(float('inf'))
BleftMotor.setPosition(float('inf'))
BrightMotor.setPosition(float('inf'))

FleftMotor.setVelocity(0.0)
FrightMotor.setVelocity(0.0)
BleftMotor.setVelocity(0.0)
BrightMotor.setVelocity(0.0)

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    psValues = []
    for i in range(2):
        psValues.append(ps[i].getValue())

    # detect obstacles
    right_obstacle = psValues[1] > 80.0
    left_obstacle = psValues[0] > 80.0

    # initialize motor speeds at 50% of MAX_SPEED.
    FleftSpeed  = 0.5 * MAX_SPEED
    FrightSpeed = 0.5 * MAX_SPEED
    BleftSpeed  = 0.5 * MAX_SPEED
    BrightSpeed = 0.5 * MAX_SPEED
    # modify speeds according to obstacles

    # write actuators inputs
    FleftMotor.setVelocity(FleftSpeed)
    FrightMotor.setVelocity(FrightSpeed)
    BleftMotor.setVelocity(BleftSpeed)
    BrightMotor.setVelocity(BrightSpeed)