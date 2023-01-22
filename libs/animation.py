import bpy

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Animation(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHARM'
    bl_label = 'Animation'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.object.get('CharmRig', False)

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        layout.operator('mhx.remove_frame_zero')
        layout.operator('mhx.remove_unused_fcurves')
        layout.operator('mhx.enforce_all_limits')
        layout.operator('mhx.transfer_to_fk')
        layout.operator('mhx.transfer_to_ik')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Animation,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)