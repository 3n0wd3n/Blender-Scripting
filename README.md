# BlenderScripting

*Handsome and useful links:*

https://www.youtube.com/playlist?list=PLmGhGFnN_vMITtIKBKjPJ1h5C5i-iabqO

https://docs.blender.org/api/current/index.html

*Content division:*

> Context Module
>
> Data Module
>
> Types Module
>
> Build in Operators
>
> Custom Operators
>
> Intro to User Interface

*Before starting:*

![python_tooltip](https://user-images.githubusercontent.com/47132583/159736743-bed45d69-44df-4b36-bff5-96a55b52b299.png)

## Intro to Blender API

Blender application is made of three main modules 

* Application Module

      >>> bpy.
              app
              context
              data
              msgbus
              ops
              path
              props
              types
              utils

Blender application module is the entire blender application itself. The bpy corresponds to the entire blender application. Delteting object, switching between edit mode and sculpting mode... everything is here.

* Standalone Module

      bgl
      blf
      bmesh
      mathutils

* Game Engine Module (Game Engine Module is emoved from blender version 2.8)

      Blender Game Engine and other engine components like Blender Internal 

**Context Module**
--

https://docs.blender.org/api/current/bpy.context.html

      >>> bpy.context.
                      active_annotation_layer
                      active_bone
                      active_editable_fcurve
                      active_gpencil_frame
                      active_gpencil_layer
                      active_nla_strip
                      active_nla_track
                      active_object
                      active_operator
                      active_pose_bone
                      active_sequence_strip
                      annotation_data
                      annotation_data_owner
                      area
                      as_pointer(
                      asset_file_handle
                      asset_library_ref
                      bl_rna
                      bl_rna_get_subclass(
                      bl_rna_get_subclass_py(
                      blend_data
                      collection
                      copy(
                      driver_add(
                      driver_remove(
                      edit_object
                      editable_bones
                      editable_fcurves
                      editable_gpencil_layers
                      editable_gpencil_strokes
                      editable_objects
                      engine
                      evaluated_depsgraph_get(
                      get(
                      gizmo_group
                      gpencil_data
                      gpencil_data_owner
                      id_data
                      id_properties_clear(
                      id_properties_ensure(
                      id_properties_ui(
                      image_paint_object
                      is_property_hidden(
                      is_property_overridable_library(
                      is_property_readonly(
                      is_property_set(
                      items(
                      keyframe_delete(
                      keyframe_insert(
                      keys(
                      layer_collection
                      mode
                      object
                      objects_in_mode
                      objects_in_mode_unique_data
                      particle_edit_object
                      path_from_id(
                      path_resolve(
                      pop(
                      pose_object
                      preferences
                      property_overridable_library_set(
                      property_unset(
                      region
                      region_data
                      rna_type
                      scene
                      screen
                      sculpt_object
                      selectable_objects
                      selected_bones
                      selected_editable_bones
                      selected_editable_fcurves
                      selected_editable_keyframes
                      selected_editable_objects
                      selected_editable_sequences
                      selected_movieclip_tracks
                      selected_nla_strips
                      selected_objects
                      selected_pose_bones
                      selected_pose_bones_from_active_object
                      selected_sequences
                      selected_visible_fcurves
                      sequences
                      space_data
                      tool_settings
                      type_recast(
                      ui_list
                      values(
                      vertex_paint_object
                      view_layer
                      visible_bones
                      visible_fcurves
                      visible_gpencil_layers
                      visible_objects
                      visible_pose_bones
                      weight_paint_object
                      window
                      window_manager
                      workspace

Everything that is shown here is actually what we have in the current context (outliner, properties, scripting tab, viewport, etc.)

![context](https://user-images.githubusercontent.com/47132583/159739566-be501e46-3f7c-4772-9374-e61f1ccdbd8e.png)

![scene](https://user-images.githubusercontent.com/47132583/159740931-ac045d8b-7526-49d0-8dce-f9d18fb75732.png)

**Basic Commands Of Context Model**

Returning selected objects

      >>> bpy.context.selected_objects
      [bpy.data.objects['Cube']]

      >>> bpy.context.selected_objects
      [bpy.data.objects['Cube'], bpy.data.objects['Light']]

      >>> bpy.context.selected_objects
      [bpy.data.objects['Cube'], bpy.data.objects['Light'], bpy.data.objects['Camera']]

Returning of the current scene

      >>> bpy.context.scene.name
      'Scene'

Creating new scene

      >>> bpy.ops.scene.new(type='NEW')
      {'FINISHED'}

Returning all scenes (using bpy.data module)

      >>> bpy.data.scenes
      <bpy_collection[2], BlendDataScenes>

Listing in scenes (using bpy.data module)

      >>> for scene in bpy.data.scenes:
      ...         print(scene)
      ...         
      <bpy_struct, Scene("Scene") at 0x0000021897364088>
      <bpy_struct, Scene("Scene.001") at 0x00000218AF51C088>

Listing in scenes and returning their names (using bpy.data module)

      >>> for scene in bpy.data.scenes:
      ...         print(scene.name)
      ...         
      Scene
      Scene.001

**Data Module**
--

https://docs.blender.org/api/current/bpy.data.html

      >>> bpy.data.
                   actions
                   armatures
                   as_pointer(
                   batch_remove(
                   bl_rna
                   bl_rna_get_subclass(
                   bl_rna_get_subclass_py(
                   brushes
                   cache_files
                   cameras
                   collections
                   curves
                   driver_add(
                   driver_remove(
                   filepath
                   fonts
                   get(
                   grease_pencils
                   id_data
                   id_properties_clear(
                   id_properties_ensure(
                   id_properties_ui(
                   images
                   is_dirty
                   is_property_hidden(
                   is_property_overridable_library(
                   is_property_readonly(
                   is_property_set(
                   is_saved
                   items(
                   keyframe_delete(
                   keyframe_insert(
                   keys(
                   lattices
                   libraries
                   lightprobes
                   lights
                   linestyles
                   masks
                   materials
                   meshes
                   metaballs
                   movieclips
                   node_groups
                   objects
                   orphans_purge(
                   paint_curves
                   palettes
                   particles
                   path_from_id(
                   path_resolve(
                   pop(
                   property_overridable_library_set(
                   property_unset(
                   rna_type
                   scenes
                   screens
                   shape_keys
                   sounds
                   speakers
                   temp_data(
                   texts
                   textures
                   type_recast(
                   use_autopack
                   user_map(
                   values(
                   version
                   volumes
                   window_managers
                   workspaces
                   worlds

What is the difference between bpy.context and bpy.data --> They both behave slightly differently.

**Basic Commands Of Context Model**

Returns how many objects (collection) are in the !scenes!

      >>> bpy.data.objects
      <bpy_collection[3], BlendDataObjects>

Using list (python function) to return specific obejcts in the !scenes!

      >>> list(bpy.data.objects)
      [bpy.data.objects['Camera'], bpy.data.objects['Cube'], bpy.data.objects['Light']]

The difference is that that bpy.data is not focused only on one scene instead of this it is checking all scenes properties. Bpy.context provide information about what am I having currently on the scene not in the memory. Bpy.data is a real place where everything is getting created.
      
      SCENE here is in plural form
      The context using singular form
      
      >>> bpy.context.scene
      bpy.data.scenes['Scene']
      
      Here we can see that scenes is not in plural form when we speaking about bpy.data
      
      >>> bpy.data.scenes
      <bpy_collection[2], BlendDataScenes>

Using python cuts to print all scenes instead of looping them 

      >>> bpy.data.scenes[:]
      [bpy.data.scenes['Scene'], bpy.data.scenes['Scene.001']]

 **Type Module**
 --

https://docs.blender.org/api/current/bpy.types.html

Use of bpy.type is that, that each and every object that we have in blender (light, scenes, real object in viewport, keyframes in animation section, just everything that we use inside Blender) is actualy defined under the bpy.type)

**Basic Commands Of Type Module**

This is the real place where behavior of the object is defined (all the functionalities all the properties)

      >>> bpy.types.Object
                          (
                          Base(
                          Constraints(
                          Display(
                          GpencilModifiers(
                          LineArt(
                          Modifiers(
                          ShaderFx(
                          SolverConstraint(
                          
      >>> bpy.types.Material
                      (
                      GPencilStyle(
                      LineArt(
                      Slot(
      
      >>> bpy.types.Scene
                   (
                   Display(
                   EEVEE(
                   Gpencil(
                   Objects(
                   RenderView(
                   Sequence(
      .
      .
      . 
      
      etc.
      
Here we can see, that everything is instance of some class (even our objects in viewport)

      >>> type(bpy.context.selected_objects[0])
      <class 'bpy_types.Object'>
                        
                        
Type is blueprint for everything that is defined. Under bpy.type is everything about classes. And we just make instances of them. And we can even make our own types.

Making our own type with property

      >>> bpy.types.Object.MyOwnProp = "Hello Property"
      
See OUR own property

      >>> bpy.types.Object."
                           MyOwnProp
                           as_pointer(
                           bl_rna
                           bl_rna_get_subclass(
                           bl_rna_get_subclass_py(
                           children
                           cycles(
                           driver_add(
                           driver_remove(
                           get(
                           id_data
                           id_properties_clear(
                           id_properties_ensure(
                           id_properties_ui(
                           is_property_hidden(
                           is_property_overridable_library(
                           is_property_readonly(
                           is_property_set(
                           items(
                           keyframe_delete(
                           keyframe_insert(
                           keys(
                           mro(
                           path_from_id(
                           path_resolve(
                           pop(
                           property_overridable_library_set(
                           property_unset(
                           type_recast(
                           users_collection
                           users_scene
                           values(

Asking for the property 

      >>> bpy.types.Object.MyOwnProp
      'Hello Property'
                    
                        
