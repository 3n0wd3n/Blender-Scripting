# 24.3.2022

#SIMPLE properties
name = bpy.props.StringProperty(name="Enter your name")
age = bpy.props.IntStringProperty(name="Enter your age", min = 1, max = 100)
alive = bpy.props.BoolProperty(name="Alive or not ?")

#VECTOR properties
