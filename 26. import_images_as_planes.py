# extend Python's functionality to work with file paths
import pathlib

# give Python access to Blender's functionality
import bpy

# give Python access to Blender's add-on functionality
import addon_utils


def partially_clean_the_scene():
    """select all the object and delete them (just like pressing A + X + D in the viewport)"""
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def enable_addon(addon_name):
    # check if the addon is enabled
    loaded_default, loaded_state = addon_utils.check(addon_name)
    if not loaded_state:
        # enable the addon
        addon_utils.enable(addon_name)


def import_image_as_plane(image_path):
    # check if the image exists on disk
    if image_path.exists():
        # import the image as a plane
        bpy.ops.import_image.to_plane(files=[{"name": str(image_path)}])


def main():
    
    partially_clean_the_scene()

    # create a variable to represent the name of the add-on we want to enable
    addon_name = "io_import_images_as_planes"

    enable_addon(addon_name)

    # create a variable that will hold the path to the target image
    image_path = pathlib.Path.home() / "Desktop" / "3d Print" / "blender models" / "scripting" / "assets" / "image_plane.png"
    print("image path", image_path)

    import_image_as_plane(image_path)


main()