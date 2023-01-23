import bpy

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Pose(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHARM'
    bl_label = 'Pose'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.active_object.get('charm_rig', False)

    def draw(self, context):
        rig = context.active_object
        layout = self.layout

        row = layout.row()
        layout.operator("daz.import_pose")
        layout.operator("daz.import_expression")
        layout.operator("daz.clear_pose")

        op = layout.operator("daz.clear_morphs")
        op.morphset = "All"
        if rig.DazDriversDisabled:
            layout.operator("daz.enable_drivers")
        else:
            layout.operator("daz.disable_drivers")

        layout.operator("daz.impose_locks_limits")
        layout.operator("daz.bake_pose_to_fk_rig")
        layout.operator("daz.save_pose_preset")


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Pose,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)