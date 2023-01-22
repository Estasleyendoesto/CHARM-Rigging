import bpy
from . import constructor

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARA_PT_Main(bpy.types.Panel):
    # bl_idname = 'chararig.setup_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CHARM'
    bl_label = 'Setup'

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        row.operator('chararig.rig_loader', icon='SHADERFX')
        
        rig = context.object


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class CHARARIG_OT_Loader(bpy.types.Operator):
    bl_idname = 'chararig.rig_loader'
    bl_label = 'Configure MHX Rig'
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
        key = 'CharmRig'
        if rig.get(key, False):
            self.report({"WARNING"}, "CHARM has already been applied")
            return True
        else:
            rig[key] = True
            ui = rig.id_properties_ui(key)
            ui.update(
                default = False, 
            )

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

    def execute(self, context):
        # Rig selected
        rig = context.object
        
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

        # Clear
        D.libraries.remove(D.libraries.get('customShapes.blend'))      

        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
classes = (
    CHARA_PT_Main,
    CHARARIG_OT_Loader,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)