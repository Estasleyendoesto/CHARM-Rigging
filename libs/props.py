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
        # Esta función solo se registra junto con este panel y si no existe
        handlers = [h.__name__ for h in bpy.app.handlers.depsgraph_update_post[::-1]]
        if "on_charm_property_change" not in handlers:
            bpy.app.handlers.depsgraph_update_post.append(on_charm_property_change)

        return context.active_object.get('charm_rig', False)

    def draw(self, context):
        rig = context.active_object
        layout = self.layout

        row = layout.row()
        # Add Property
        row.operator('charm.properties_add')

        for prop in rig.charm_props:
            row = layout.row()
            # Name
            row.label(text=prop.name)
            # Value
            row.prop(rig, '["%s"]' % prop.name, text='')
            # Edit
            p = row.operator("wm.properties_edit", text="", icon='PREFERENCES', emboss=False)
            p.data_path = 'object'
            p.property_name = prop.name

            # Delete
            p = row.operator("charm.properties_remove", text="", icon='X', emboss=False)
            p.property_name = prop.name


    """
    def notocar(self):
        row = layout.row()
        row.operator("wm.properties_add") # Crea la propiedad
        row.operator("wm.properties_remove", text="", icon='X', emboss=False) # Elimina la propiedad
        row.operator("wm.properties_edit") # Edita la propiedad
        layout.prop(context.object, '["prop"]') # Edita el valor de la propiedad (importante el nombre estar entre corchetes)
        # Run python file path
        # Esto lo usaremos para que un operator ejecute un script pequeño, para usarlo con varios botones (operators)
        # https://docs.blender.org/api/current/bpy.ops.script.html#bpy.ops.script.python_file_run
    """

# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_OT_add_property(bpy.types.Operator):
    bl_idname = 'charm.properties_add'
    bl_label = 'ADD Property'

    def execute(self, context):
        rig = context.active_object

        # Create property
        bpy.ops.wm.properties_add(data_path='object')
        
        # Get property name
        props = [ p for p in rig.keys() ]
        prop_name = props[-1]
        
        # Adding to Property Group
        prop = rig.charm_props.add()
        prop.name = prop_name
        prop.index = len(props) - 1
        
        return {'FINISHED'}

class CHARM_OT_del_property(bpy.types.Operator):
    bl_idname = 'charm.properties_remove'
    bl_label = 'Remove Property'

    property_name: bpy.props.StringProperty()

    def execute(self, context):
        rig = context.active_object

        # Delete property
        bpy.ops.wm.properties_remove(data_path='object', property_name=self.property_name)
        
        # Delete property from charm_props
        charm_props = rig.charm_props
        charm_props.remove( charm_props.keys().index(self.property_name) )

        # Update charm_props index
        rig_props = [p for p in rig.keys()]
        for prop in charm_props:
            if prop.name in rig_props:
                prop.index = rig_props.index(prop.name)

        return {'FINISHED'}

# - - - - - - - - - - - - - - - - - - - - - - - -
# Properties
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PG_Props(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    index: bpy.props.IntProperty()  

def on_charm_property_change(scene):
    ''' Registro de eventos, necesario para interceptar un posible cambio de nombre de charm_props.items
    '''    
    rig = bpy.context.active_object.get('charm_rig', False)
    if not rig:
        return

    print( 'vamonooooooooooooooooooooos!' )

    # Update charm_props index
    charm_props = rig.charm_props
    rig_props = [p for p in rig.keys()]

    for prop in charm_props:
        if prop.name in rig_props:
            prop.index = rig_props.index(prop.name)
        else:
            pass
            # if rig_props[-1] != prop


'''
import bpy

p =  bpy.context.active_object.charm_props

print("---------------- new")

n = 0
for i in p:
    print( 'charm_props pos: ', n, '  value: ' , i.name, '   index: ', i.index, )
    n += 1
    
print("----")
a = [i for i in bpy.context.active_object.keys()]
for k in p:
    print('all_props_index: ', k.index, '  value: ',    a[k.index]) 
'''

# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PG_Props,
    CHARM_PT_Props,
    CHARM_OT_add_property,
    CHARM_OT_del_property,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.charm_props = bpy.props.CollectionProperty(type=CHARM_PG_Props)
    bpy.app.handlers.depsgraph_update_post.append(on_charm_property_change)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    for handler in bpy.app.handlers.depsgraph_update_post[::-1]:
        if handler.__name__ == "on_charm_property_change":
            bpy.app.handlers.depsgraph_update_post.remove(handler)