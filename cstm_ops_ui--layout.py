import bpy

class DummyUIDemo(bpy.type.Panel):
  bl_label = "My UI Demo"
  bl_idname =  "SCENE_PT_layout"
  bl_space_type = "PROPERTIES"
  bl_region_type = "WINDOW"
  bl_context = "material"
  
  def draw(self, context):
    obj = context.object
    layout = self.layout
    
    layout.label(text="JUST a label")
    
    row1 = layout.row()
    row1.prop(obj, "location")
    
    row2 = layout.row()
    row2.prop(obj, "scale")
    
    split = layout.split()
    
    col1 = split.column()
    col1.label(text="This is Col 1")
    
    col2 = split.column()
    col2.label(text="This is Col 2")
    col2.operator("mesh.wireframe")
    
    col3 = split.column()
    col3.label(text="This is Col 3")

    
def register():
  bpy.utils.register_class(DummyUIDemo)
  
def unregister():
  bpy.utils.unregister_class(DummyUIDemo)

if __name__ == "__main__":
  register()
