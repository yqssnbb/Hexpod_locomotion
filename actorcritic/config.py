# -^- coding: utf8 -^- 

ENVIRONMENT = "TOY"
# ENVIRONMENT = "BLUE"
# ENVIRONMENT = "VREP"

COMMENT="TEST"
FILEOUT = False
FILEOUT = FILEOUT and ENVIRONMENT=="TOY"

REFRESHTOPO = True

#Configues for topomain
RESUME = 0
LOGGING = False
OBSERVETOPO = True
TESTBEHAVE = True


#Configurations in toyrep
STRICT_BALANCE = True 
TIPS_order = False
TIPS_distance = True
DISPLAY = False

BLUEROBOT = ENVIRONMENT=="BLUE"

#Reward Options:
RWD_PAIN = True
RWD_DANEROUS = True


#Reward factors:
RWDFAC_PAIN = 1
RWDFAC_DANEROUS = 1