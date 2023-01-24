import bpy

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Props(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_label = 'CHARM Properties'
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
        rna_path = 'object.children[%s]' % rig.children.index(charm_props_object)

        # Add Property
        row = layout.row()
        p = row.operator('wm.properties_add')
        p.data_path = rna_path

        for prop in charm_props_object.keys():
            row = layout.row()
            # Name
            row.label(text=prop)
            # Value
            row.prop(charm_props_object, '["%s"]' % prop, text='')
            # Edit
            p = row.operator("wm.properties_edit", text="", icon='PREFERENCES', emboss=False)
            p.data_path = rna_path
            p.property_name = prop

            # Delete
            p = row.operator("wm.properties_remove", text="", icon='X', emboss=False)
            p.data_path = rna_path
            p.property_name = prop

# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Props,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)