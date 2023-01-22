import bpy
import math

# Script created by Estasleyendoesto
# Only compatible with MHX armature from Diffeomorphic addon 

# Instructions:
# 1. Append CustomShapes collection to your project
# 2. Select the armature of your character
# 3. Run Script

# Custom Shapes
bones = [
    {
        'bone': 'master',
        'customShape': 'Root.Square',
        'scale': (5.8, 5.8, 5.8),
        'translation': (0.0, 0.0, 0.0),
        'rotation': (0.0, 0.0, 0.0)
    },
    {
        'bone': 'foot.ik.R',
        'customShape': 'Foot.R',
        'scale': (5.82, 5.82, 5.82),
        'translation': (0.008, 0.103, 0.0),
        'rotation': (0.0, 180.0, 180.0)
    },
    {
        'bone': 'foot.ik.L',
        'customShape': 'Foot.L',
        'scale': (5.82, 5.82, 5.82),
        'translation': (-0.008, 0.103, 0.0),
        'rotation': (0.0, 180.0, 180.0)
    },
    {
        'bone': 'shin.ik.twist.R',
        'customShape': 'Circle',
        'scale': (2.3, 2.3, 2.3),
        'translation': (0, 0.2, 0.048),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'shin.ik.twist.L',
        'customShape': 'Circle',
        'scale': (2.3, 2.3, 2.3),
        'translation': (-0.01, 0.2, 0.048),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'knee.pt.ik.R',
        'customShape': 'FootRoll',
        'scale': (11.35, 11.35, 11.35),
        'translation': (0, -0.04, 0),
        'rotation': (0, 9.4, 0)
    },
    {
        'bone': 'knee.pt.ik.L',
        'customShape': 'FootRoll',
        'scale': (11.35, 11.35, 11.35),
        'translation': (0, -0.04, 0),
        'rotation': (0, -9.4, 0)
    },
    {
        'bone': 'thigh.ik.twist.R',
        'customShape': 'Circle',
        'scale': (3.07, 3.913, 3.476),
        'translation': (-0.012, 0.19, 0.02),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'thigh.ik.twist.L',
        'customShape': 'Circle',
        'scale': (3.07, 3.913, 3.476),
        'translation': (-0.005, 0.19, 0.02),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'pelvis',
        'customShape': 'Sphere',
        'scale': (1.5, 1.5, 1.5),
        'translation': (0, 0.05, 0),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'hip',
        'customShape': 'Bowl.Horizontal',
        'scale': (23.6, 23.6, 23.6),
        'translation': (0, 0, 0.02),
        'rotation': (0, 90, 0)
    },
    {
        'bone': 'back',
        'customShape': 'spina',
        'scale': (1.22, 1, 1),
        'translation': (0, 0.114, 0.03),
        'rotation': (93.5, 0, 0)
    },
    {
        'bone': 'hand.ik.R',
        'customShape': 'GZM_HandIK',
        'scale': (1, 0.86, -0.1),
        'translation': (0.001, -0.007, 0),
        'rotation': (0, 0, -4.22)
    },
    {
        'bone': 'hand.ik.L',
        'customShape': 'GZM_HandIK',
        'scale': (1, 0.86, -0.1),
        'translation': (-0.001, -0.007, 0),
        'rotation': (0, 0, 4.22)
    },
    {
        'bone': 'forearm.ik.twist.R',
        'customShape': 'Circle',
        'scale': (2.6, 2.6, 2.6),
        'translation': (0, 0.101, 0.006),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'forearm.ik.twist.L',
        'customShape': 'Circle',
        'scale': (2.6, 2.6, 2.6),
        'translation': (0, 0.101, 0.006),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'upper_arm.ik.twist.R',
        'customShape': 'Circle',
        'scale': (2.92, 2.92, 2.92),
        'translation': (-0.011, 0.12, 0.01),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'upper_arm.ik.twist.L',
        'customShape': 'Circle',
        'scale': (2.92, 2.92, 2.92),
        'translation': (0.001, 0.12, 0.01),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'elbow.pt.ik.R',
        'customShape': 'FootRoll',
        'scale': (11.35, 11.35, 11.35),
        'translation': (0, -0.031, 0),
        'rotation': (0, 48.9, 0)
    },
    {
        'bone': 'elbow.pt.ik.L',
        'customShape': 'FootRoll',
        'scale': (11.35, 11.35, 11.35),
        'translation': (0, -0.031, 0),
        'rotation': (0, 41.7, 0)
    },
    {
        'bone': 'neckhead',
        'customShape': 'Root.2Way',
        'scale': (6.7, 6.7, 6.7),
        'translation': (0, 0.05, 0),
        'rotation': (90, 0, 0)
    },
    {
        'bone': 'gaze',
        'customShape': 'EyeMaster',
        'scale': (7.3, 7.3, 7.3),
        'translation': (0, 0, 0),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'gaze.R',
        'customShape': 'Circle.S',
        'scale': (30, 30, 30),
        'translation': (0, 0.006, 0),
        'rotation': (0, 0, 0)
    },
    {
        'bone': 'gaze.L',
        'customShape': 'Circle.S',
        'scale': (30, 30, 30),
        'translation': (0, 0.006, 0),
        'rotation': (0, 0, 0)
    },
]

# Set Custom Shape
def set_custom_shape():
    for b in bones:
        object = bpy.data.objects[ b['customShape'] ]
        bone = armature.bones[ b['bone'] ]
        
        bone.custom_shape = object
        bone.custom_shape_scale_xyz = b['scale']
        bone.custom_shape_translation = b['translation']
        
        rotation = b['rotation']
        x, y, z = math.radians(rotation[0]), math.radians(rotation[1]), math.radians(rotation[2])
        bone.custom_shape_rotation_euler = (x, y, z)
        
# Hide unused bones:
def hide_bones():
    armature.bones['kneePoleA.L'].bone.hide = True
    armature.bones['kneePoleA.R'].bone.hide = True
    armature.bones['elbowPoleA.L'].bone.hide = True
    armature.bones['elbowPoleA.R'].bone.hide = True
    
    armature.bones['upper_arm.ik.twist.R'].bone.hide = True
    armature.bones['upper_arm.ik.twist.L'].bone.hide = True
    armature.bones['forearm.ik.twist.R'].bone.hide = True
    armature.bones['forearm.ik.twist.L'].bone.hide = True
    armature.bones['thigh.ik.twist.R'].bone.hide = True
    armature.bones['thigh.ik.twist.L'].bone.hide = True
    armature.bones['shin.ik.twist.R'].bone.hide = True
    armature.bones['shin.ik.twist.L'].bone.hide = True
    
# Move unused bones
def change_bones_layer():
    armature.bones['pelvis'].bone.layers[24] = True
    armature.bones['gaze.R'].bone.layers[24] = True
    armature.bones['gaze.L'].bone.layers[24] = True
    armature.bones['gaze'].bone.layers[24] = True
    
# Creation of bone groups
def create_bone_groups():
    bg = [ 
        'IK', 'IK_Pole', 'ArmLeg Rotation', 'Clavicle', 'FootRev', 'Genital', 'Hair'
    ]
    
    for name in bg:
        armature.bone_groups.new(name=name)
    
    
    armature.bone_groups['IK'].color_set = 'CUSTOM'
    armature.bone_groups['IK_Pole'].color_set = 'CUSTOM'
    armature.bone_groups['ArmLeg Rotation'].color_set = 'THEME06'
    armature.bone_groups['Clavicle'].color_set = 'CUSTOM'
    armature.bone_groups['FootRev'].color_set = 'CUSTOM'
    armature.bone_groups['Genital'].color_set = 'THEME05'
    armature.bone_groups['Hair'].color_set = 'THEME03'
     
# Change existent bone groups themes
def change_bonegroup_theme():
    armature.bone_groups['Left Arm IK'].color_set = 'THEME10'
    armature.bone_groups['Right Arm IK'].color_set = 'THEME10'
    armature.bone_groups['Left Leg IK'].color_set = 'THEME10'
    armature.bone_groups['Right Leg IK'].color_set = 'THEME10'
    armature.bone_groups['Face'].color_set = 'THEME13'
    
# Change of bone exists groups colors
def change_bonegroup_color():
    bonegroups = [
        { 
            'name': 'Spine', 'normal': (0.733, 1.0, 0.953), 'select': (0.733, 1, 0.953), 'active': (1, 0.992, 0.745)
        },
        {
            'name': 'IK', 'normal': (1.0, 0.784, 0.275), 'select': (0, 0, 0), 'active': (0.878, 0.867, 0.616)
        },
        {
            'name': 'IK_Pole', 'normal': (0.945, 0.945, 0.945), 'select': (0, 0, 0), 'active': (0, 1, 1)
        },
        {
            'name': 'Clavicle', 'normal': (1, 0.745, 0), 'select': (0.282, 0.298, 0.337), 'active': (1, 0.961, 0.659)
        },
        {
            'name': 'FootRev', 'normal': (0.220, 0.627, 1), 'select': (0.965, 0.412, 0.075), 'active': (0.812, 0.949, 1)
        }
    ]
    
    for bg in bonegroups:
        armature.bone_groups[ bg['name'] ].colors.normal = bg['normal']
        armature.bone_groups[ bg['name'] ].colors.select = bg['select']
        armature.bone_groups[ bg['name'] ].colors.active = bg['active']
    
# Assing bone groups
def assing_bonegroup():
    bdata = [
        {
            'bonegroup': 'Spine',
            'bones': ['pelvis']
        },
        { 
            'bonegroup': 'IK', 
            'bones': [ 'hand.ik.R', 'hand.ik.L', 'foot.ik.R', 'foot.ik.L' ] 
        },
        { 
            'bonegroup': 'IK_Pole', 
            'bones': [ 'elbow.pt.ik.R', 'elbow.pt.ik.L', 'knee.pt.ik.R', 'knee.pt.ik.L' ] },
        { 
            'bonegroup': 'ArmLeg Rotation', 
            'bones': [ 
                'upper_arm.ik.twist.R', 'upper_arm.ik.twist.L', 'forearm.ik.twist.R', 'forearm.ik.twist.L',
                'thigh.ik.twist.R', 'thigh.ik.twist.L', 'shin.ik.twist.R', 'shin.ik.twist.L'
            ] 
        },
        {
            'bonegroup': 'Clavicle',
            'bones': [ 'clavicle.R', 'clavicle.L' ]
        },
        {
            'bonegroup': 'FootRev',
            'bones': [ 'foot.rev.R', 'foot.rev.L', 'toe.rev.R', 'toe.rev.L' ]
        },
    ]
    
    for b in bdata:
        for bone in b['bones']:
            armature.bones[ bone ].bone_group = armature.bone_groups[ b['bonegroup'] ]

# Lock bones
def lock_bones():
    bones = [
        {
            'bone': 'gaze',
            'scale': (True, True, True),
        },
        {
            'bone': 'gaze.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'gaze.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'neckhead',
            'location': (True, True, True),
            'scale': (True, True, True),
        },
        {
            'bone': 'clavicle.R',
            'location': (True, True, True),
            'rotation': (False, True, False),
            'scale': (True, True, True),
        },
        {
            'bone': 'clavicle.L',
            'location': (True, True, True),
            'rotation': (False, True, False),
            'scale': (True, True, True),
        },
        {
            'bone': 'pectoral.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'pectoral.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'upper_arm.ik.twist.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'upper_arm.ik.twist.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'forearm.ik.twist.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'forearm.ik.twist.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'elbow.pt.ik.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'elbow.pt.ik.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'hand.ik.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'hand.ik.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'back',
            'location': (True, True, True),
            'scale': (True, True, True),
        },
        {
            'bone': 'pelvis',
            'scale': (True, True, True),
        },
        {
            'bone': 'hip',
            'scale': (True, True, True),
        },
        {
            'bone': 'thigh.ik.twist.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'thigh.ik.twist.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'shin.ik.twist.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'shin.ik.twist.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'knee.pt.ik.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'knee.pt.ik.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'foot.ik.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'foot.ik.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'foot.rev.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'foot.rev.L',
            'scale': (True, True, True),
        },
        {
            'bone': 'toe.rev.R',
            'scale': (True, True, True),
        },
        {
            'bone': 'toe.rev.L',
            'scale': (True, True, True),
        },
    ]
    
    for b in bones:
        if 'location' in b:
            armature.bones[ b['bone'] ].lock_location = b['location']
        if 'rotation' in b:
            armature.bones[ b['bone'] ].lock_rotation = b['rotation']
        if 'scale' in b:
            armature.bones[ b['bone'] ].lock_scale = b['scale']
            
def bone_layers_visibility(context):
    context.object.data.layers[1]  = False
    context.object.data.layers[10] = False
    context.object.data.layers[24] = True

def run(context):
    global armature
    armature = context.object.pose

    set_custom_shape()
    hide_bones()
    change_bones_layer()
    create_bone_groups()
    change_bonegroup_theme()
    change_bonegroup_color()
    assing_bonegroup()
    lock_bones()
    bone_layers_visibility(context)