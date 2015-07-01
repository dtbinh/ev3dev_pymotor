# PID
PID_MULTI_THRES = 0.25 # Determines the weight of each PID value


KP = 0.0127
KI = 0.005
KD = 0.0095
DERIVATOR = 0

P_VAL = 0
I_VAL = 0
D_VAL = 0

I_MAX = 0.01359
I_MIN = 0

PID_TOTAL = 0

ERROR = 0
MOTOR_RPS = 0.3 # rotations per scond
MOTOR_RPS_MIN = -2.0

# If line is on the right = negative value

# ROI Settings
ROI_Y = 80
ROI2_Y = 120
ROI3_Y = 160 # DON'T EXCEED 200

ROI_START = ROI_Y
ROI_DIF = abs(ROI2_Y-ROI_Y)

# THRESHOLD
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
MIDDLE = CAMERA_WIDTH/2

THRESH = 55 # Change threshold to high if can't detect line; Change to lower if detects too many
AREA_THRESH = 200

# COLORS ARE IN BGR
RED_COLOR = (43, 57, 192)
GREEN_COLOR = (113, 204, 46)
BLUE_COLOR = (219, 152, 52)
YELLOW_COLOR = (131, 130, 224)

