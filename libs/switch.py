import bpy

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Switch(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHARM'
    bl_label = 'FK / IK Switch'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.active_object.get('charm_rig', False)

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text='Left arm')
        row.operator('mhx.snap_fk_left_arm', text='FK')
        row.operator('mhx.snap_ik_left_arm', text='IK')

        row = layout.row()
        row.label(text='Right arm')
        row.operator('mhx.snap_fk_right_arm', text='FK')
        row.operator('mhx.snap_ik_right_arm', text='IK')

        row = layout.row()
        row.label(text='Left leg')
        row.operator('mhx.snap_fk_left_leg', text='FK')
        row.operator('mhx.snap_ik_left_leg', text='IK')

        row = layout.row()
        row.label(text='Right leg')
        row.operator('mhx.snap_fk_right_leg', text='FK')
        row.operator('mhx.snap_ik_right_leg', text='IK')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Switch,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)