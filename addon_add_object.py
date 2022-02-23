import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "MyCube"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MikesTab"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Add my own cube", icon = "CUBE")
        #spacing from upper label
        for i in range(2):
            row = layout.row()
        row.operator("mesh.primitive_cube_add")
        
    
def register():
    bpy.utils.register_class(TestPanel)
def unregister():
    bpy.utils.register_class(TestPanel)
    
if __name__ == "__main__":
    register()
