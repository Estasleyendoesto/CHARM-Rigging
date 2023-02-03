import bpy
import os
import uuid
from bpy_extras.io_utils import ImportHelper

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Props(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_label = 'CHARM'
    bl_options = {'DEFAULT_CLOSED'}
    bl_idname = 'CHARM_PT_Props'

    @classmethod
    def poll(cls, context):
        return context.active_object.get('charm_rig', False)

    def draw(self, context):
        rig = context.active_object
        layout = self.layout

        # Charm_props object
        charm_props_name = rig.get('charm_props_name', None)
        charm_props_object = None
        for c in rig.children:
            if c.name == charm_props_name:
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


class CHARM_PT_Scripts(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_label = 'Custom Scripts'
    bl_parent_id = 'CHARM_PT_Props'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        rig = context.active_object
        layout = self.layout

        # Añadir un script
        row = layout.row()
        op = row.operator('charm.script_add')

        for item in rig.charm_opts:
            row = layout.row()

            op = row.operator('charm.run_script', text=item.name)
            op.filename = item.name
            op.file_path = item.file_path
            op.text_name = item.script_name
            
            op = row.operator('charm.script_remove', text='', icon='X', emboss=False)
            op.identifier = item.identifier


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_OT_ScriptAdd(bpy.types.Operator, ImportHelper):
    bl_idname = 'charm.script_add'
    bl_label = 'ADD Custom Script'
    bl_description = 'Add a "*.py" file as persistent data'

    filter_glob: bpy.props.StringProperty(
        default='*.py', 
        options={'HIDDEN'}
    )
    user_input: bpy.props.StringProperty(
        name='File name', 
        description='If it is empty, the file name will be used instead.'
    )

    def is_script(self, ext):
        if ext == '.py':
            return True

        self.report({"WARNING"}, "You must select a python script")

    def print_info(self, filename):
        print('Selected file:', self.filepath)
        print('File name:', filename)

    def insert_items(self, context, filename, extension):
        rig = context.active_object
        opt = rig.charm_opts.add()
        opt.name = filename
        opt.file_path = self.filepath
        opt.identifier = str( uuid.uuid4() )
        opt.script_name = '%s_%s%s' % (filename, str(opt.identifier)[:8], extension)

    def save_on_data(self, context):
        text = bpy.data.texts.load(self.filepath)
        text.use_fake_user = True

        # Unique name for the script
        rig = context.active_object
        opt = rig.charm_opts[-1]
        text.name = opt.script_name

    def execute(self, context):
        filename, extension = os.path.splitext(bpy.path.basename(self.filepath))

        if not self.is_script(extension):
            return {'CANCELLED'}

        if self.user_input:
            filename = self.user_input

        self.insert_items(context, filename, extension)
        self.print_info(filename)
        self.save_on_data(context)

        return {'FINISHED'}

class CHARM_OT_ScriptRemove(bpy.types.Operator):
    bl_idname = 'charm.script_remove'
    bl_label = 'Delete Script'
    bl_description = 'Deletes a script permanently'

    identifier: bpy.props.StringProperty()

    def execute(self, context):
        rig = context.active_object

        charm_opts = rig.charm_opts

        deadly_name = None
        script_name = None
        for opt in charm_opts:
            if opt.identifier == self.identifier:
                opt.name = opt.name + '_' + opt.identifier
                deadly_name = opt.name
                script_name = opt.script_name

        # From charm_ops
        charm_opts.remove( charm_opts.keys().index(deadly_name) )

        # From data.texts
        script = bpy.data.texts.get(script_name)
        if script:
            bpy.data.texts.remove(script)

        return {'FINISHED'}

class CHARM_OT_RunScript(bpy.types.Operator):
    bl_idname = 'charm.run_script'
    bl_label = 'Run Script'
    bl_description = 'Execute a script'

    filename: bpy.props.StringProperty()
    file_path: bpy.props.StringProperty()
    text_name: bpy.props.StringProperty()

    def execute(self, context):
        text = bpy.data.texts.get(self.text_name)
        if text:
            exec( text.as_string() )
        else:
            self.report({"WARNING"}, "The script does not exist, you cannot rename or delete scripts imported directly")
            return {'CANCELLED'}

        # for area in bpy.context.screen.areas:
        #     if area.type == 'TEXT_EDITOR':
        #         area.spaces[0].text = text # make loaded text file visible

        #         ctx = bpy.context.copy()
        #         ctx['edit_text'] = text # specify the text datablock to execute
        #         ctx['area'] = area # not actually needed...
        #         ctx['region'] = area.regions[-1] # ... just be nice

        #         bpy.ops.text.run_script(ctx)
        #         break

        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Properties
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PG_Props(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    file_path: bpy.props.StringProperty()
    identifier: bpy.props.StringProperty()  
    script_name: bpy.props.StringProperty()


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Props,
    CHARM_PT_Scripts,
    CHARM_OT_RunScript,
    CHARM_PG_Props,
    CHARM_OT_ScriptAdd,
    CHARM_OT_ScriptRemove
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.charm_opts = bpy.props.CollectionProperty(type=CHARM_PG_Props)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)