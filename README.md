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

      bpy
       data
       context
       drops
       ops
       path
       app
       utils
       types

![bpy](https://user-images.githubusercontent.com/47132583/159737291-a9761f44-2110-4cfe-9bdc-140e2d2363a2.png)

Blender application module is the entire blender application itself. The bpy corresponds to the entire blender application. Delteting object, switching between edit mode and sculpting mode... everything is here.

* Standalone Module

      bgl
      blf
      bmesh
      mathutils

* Game Engine Module (Game Engine Module is emoved from blender version 2.8)

      Blender Game Engine and other engine components like Blender Internal 

**Context Module**

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

 
