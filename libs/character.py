import bpy

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Character(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHARM'
    bl_label = 'Character'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.active_object.get('charm_rig', False)

    def draw(self, context):
        rig = context.active_object
        layout = self.layout
        
        # Charm_props object
        charm_props_object = None
        for c in rig.children:
            if c.name == 'Charm_props':
                charm_props_object = c

        for prop in charm_props_object.keys():
            row = layout.row()
            # Name
            row.label(text=prop)
            # Value
            row.prop(charm_props_object, '["%s"]' % prop, text='')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Character,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)