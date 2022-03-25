# 24.3.2022

#SIMPLE properties
name = bpy.props.StringProperty(name="Enter your name")
age = bpy.props.IntStringProperty(name="Enter your age", min = 1, max = 100)
alive = bpy.props.BoolProperty(name="Alive or not ?")
height = bpy.props.FloatProperty(name="Enter your height")

#VECTOR properties
scale = bpy.props.IntVectorProperty(name="Scale")
rotation = bpy.props.FloatVectorProperty(name="Rotation")
bool_vectors = bpy.props.BoolVectorProperty(name="Bool vectors?")
