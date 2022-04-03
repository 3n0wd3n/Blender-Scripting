import bpy
# 31.3.2022

# UI
"""
creating class for making operator visible througth the button UI
"""

class MyOperatorUI(bpy.types.Panel):
  bl_idname = "MySimpleUI"
  bl_label = "Simple Blender Addon"
  bl_space_type = "PROPERTIES"
  bl_region_type = "WINDOW"
  bl_context = "scene"
  
  def draw(self, context):
    layout = self.layout
    
    row = layout.row()
    row.label(text = "My Blender Addon")
    
    row_space = layout.row()
    row_space.operator("mesh.mycubeoperator")

# TASKS
"""
1) create cube
2) apply wireframe modifier
3) rotate cube along z and y axis
"""

class MyOperator(bpy.types.Operator):
  bl_idname = "mesh.cubeoperator"
  bl_label = "My Operator"
  
  def execute(self, context):
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.object.modifier_add(type="WIREFRAME")
    bpy.context.selected_objects[0].rotation_euler.z += 10
    bpy.context.selected_objects[0].rotation_euler.y += 10
    return {"FINISHED"}

def register():
  bpy.utils.register_class(MyOperatorUI)
  bpy.utils.register_class(MyOperator)    
  
def unregister():
  bpy.utils.register_class(MyOperatorUI)
  bpy.utils.register_class(MyOperator)   
   
if __name__ == "__main__":
  register()
