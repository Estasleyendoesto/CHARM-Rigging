import bpy
from . import constructor

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_PT_Main(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHARM'
    bl_label = 'CHARM (0.1)'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('charm.rig_loader', icon='SHADERFX')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARM_OT_Loader(bpy.types.Operator):
    bl_idname = 'charm.rig_loader'
    bl_label = 'To CHARM Rig'
    bl_description = (
        "First have a selected MHX armature"
    )

    def parent_collection(self, rig):
        all_collections = bpy.data.collections[:]
        for collection in all_collections:
            if rig.name in collection.all_objects:
                return collection

    def is_rigged(self, rig):
        # MHX selected
        if not rig.MhxRig:
            self.report({"WARNING"}, "You need to selected an MHX Armature First")
            return True

        # If transform already applied
        key = 'charm_rig'
        if rig.get(key, False):
            self.report({"WARNING"}, "CHARM has already been applied")
            return True
        else:
            bpy.types.Object.charm_rig = bpy.props.BoolProperty()
            rig.charm_rig = True

        return False

    def collection_visibility(self, context, c):
        # Hide Collection
            c.hide_viewport = True
            c.hide_render = True

            # Exclude Collection
            viewLayer = context.scene.view_layers['ViewLayer']
            for layerCollection in viewLayer.layer_collection.children:
                for lc in layerCollection.children:
                    if lc.collection == c:
                        lc.exclude = True

    def add_props_armature(self, rig, collection):
        # New Armature
        object_name = "Charm_props"
        armature_object = bpy.data.objects.new(object_name, bpy.data.armatures.new(object_name))
        collection.objects.link(armature_object)
        # Selection
        bpy.context.view_layer.objects.active = rig
        rig.select_set(True)
        armature_object.select_set(True)
        # Emparenting
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')
        # Hide
        armature_object.hide_viewport = True
        armature_object.hide_render = True
        armature_object.hide_select = True
        armature_object.hide_set(True)

    def execute(self, context):
        # Rig selected
        rig = context.active_object
        
        # If is rigged
        if self.is_rigged(rig):
            return {"CANCELLED"}
        
        # CS Loader
        import os
        from pathlib import Path
        path = os.path.dirname(os.path.abspath(__file__))
        path = Path(path).parent
        path = Path(path, 'customShapes.blend')
        path = str(path)

        D = bpy.data
        with D.libraries.load(path) as (data_from, data_to):
            data_to.collections = [c for c in data_from.collections]

        # MHX Transform
        parent = self.parent_collection(rig)
        for c in data_to.collections:
            parent.children.link(c)
            constructor.run(context)
            self.collection_visibility(context, c)
            self.add_props_armature(rig, parent)

        # Clear
        D.libraries.remove(D.libraries.get('customShapes.blend'))      

        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARM_PT_Main,
    CHARM_OT_Loader,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)