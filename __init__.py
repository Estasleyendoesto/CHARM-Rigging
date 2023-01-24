from .libs import (
    props,
    setup,
    character,
    layers,
    switch,
    pose,
    animation,
)

bl_info = {
    "name" : "CHARM",
    "author" : "Megaera",
    "description" : "Easy Rigging with Character Customization for MHX",
    "blender" : (3, 4, 0),
    "version" : (0, 1, 0),
    "location" : "3D View > Sidebar > CHARM",
    "warning" : "",
    "category" : "Rigging"
}

def import_modules():
    import os
    import importlib
    global modules

    try:
        modules
    except NameError:
        modules = []

    if modules:
        print("\nReloading CHARM")
        for mod in modules:
            importlib.reload(mod)
    else:
        print("\nLoading CHARM")
        modnames = ["libs"]
        anchor = os.path.basename(__file__[0:-12])
        modules = []
        for modname in modnames:
            mod = importlib.import_module("." + modname, anchor)
            modules.append(mod)
import_modules()

def _call_globals(attr_name):
    for m in globals().values():
        if hasattr(m, attr_name):
            getattr(m, attr_name)()

def register():
    _call_globals("register")

def unregister():
    _call_globals("unregister")

if __name__ == '__main__':
    register()

print("CHARM loaded")