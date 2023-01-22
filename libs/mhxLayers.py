L_MAIN =    0
L_SPINE =   1

L_LARMIK =  2
L_LARMFK =  3
L_LLEGIK =  4
L_LLEGFK =  5
L_LHAND =   6
L_LFINGER = 7
L_LEXTRA =  12
L_LTOE =    13

L_RARMIK =  18
L_RARMFK =  19
L_RLEGIK =  20
L_RLEGFK =  21
L_RHAND =   22
L_RFINGER = 23
L_REXTRA =  28
L_RTOE =    29

L_FACE =    8
L_TWEAK =   9
L_HEAD =    10
L_CUSTOM =  16

L_HELP =    14
L_HELP2 =   15
L_FIN =     30
L_DEF =     31

MhxLayers = [
    ((L_MAIN,       'Root', 'MhxRoot'),
     (L_SPINE ,     'Spine', 'MhxFKSpine')),

    ((L_HEAD,       'Head', 'MhxHead'),
     (L_TWEAK,      'Tweak', 'MhxTweak')),

    ((L_LARMIK,     'IK Arm', 'MhxIKArm'),
     (L_RARMIK,     'IK Arm', 'MhxIKArm')),

    ((L_LARMFK,     'FK Arm', 'MhxFKArm'),
     (L_RARMFK,     'FK Arm', 'MhxFKArm')),

    ((L_LLEGIK,     'IK Leg', 'MhxIKLeg'),
     (L_RLEGIK,     'IK Leg', 'MhxIKLeg')),

    ((L_LLEGFK,     'FK Leg', 'MhxFKLeg'),
     (L_RLEGFK,     'FK Leg', 'MhxFKLeg')),

    ((L_LHAND,      'Hand', 'MhxHand'),
     (L_RHAND,      'Hand', 'MhxHand')),

    ((L_LFINGER,    'Fingers', 'MhxFingers'),
     (L_RFINGER,    'Fingers', 'MhxFingers')),

    ((L_LTOE,       'Toes', 'MhxToe'),
     (L_RTOE,       'Toes', 'MhxToe')),
]

