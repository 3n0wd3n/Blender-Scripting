import bpy

"""
23.3.2022
Blender allows us to write custom operators and will help us to automate the task and complex problems
The process is very simple -> we need to define the operation that we expect to be executed whenever the operator is called we also need to qualify these set of tasks and these set of actions as an operator and we need to register under the blenders bpy.ops module
We only can call the operator when is registered in bpy.ops
"""

# Defining task we need to perform
# TASKS
# 1) create cube
# 2) apply wireframe modifier
# 3) rotate cube along z axis

# We need to akke function because if we wnat to call this operator we need to difine his atributes and we will call this function and class

class MyOperator(bpy.types.Operator):
  # the value which is defining here is going to be the path in bpy.ops
  bl_idname = "mesh.mycubeoperator"
  # For definition purpose yet
  bl_label = "My Operator"
  
  def execute(self, context):
    # 1) create cube
    bpy.ops.mesh.primitive_cube_add()

    # 2) apply wireframe modifier
    bpy.ops.object.modifier_add(type='WIREFRAME')

    # 3) rotate cube along z axis
    bpy.context.selected_objects[0].rotation_euler.z += 10
    
    return {"FINISHED"}
    
    
# We need to register our operator --> we will use utility class

bpy.utils.register_class(MyOperator)

bpy.ops.mesh.mycubeoperator()
