#
# Copyright (c) 2018 - 2020 Alexander "CheeryLee" Pluzhnikov
# 
# This file is part of blender_apply_modifiers.
# 
# blender_apply_modifiers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# blender_apply_modifiers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with blender_apply_modifiers.  If not, see <http://www.gnu.org/licenses/>.
#

import bpy
from . import apply_modifiers

bl_info = {
    "name": "Apply Modifiers",
    "author": "Alexander Pluzhnikov",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Apply",
    "description": "Apply all modifiers on selected objects",
    "wiki_url": "https://github.com/CheeryLee/blender_apply_modifiers",
    "category": "Object",
}

def register():
    bpy.utils.register_class(apply_modifiers.ApplyModifiers)
    bpy.types.VIEW3D_MT_object_apply.prepend(apply_modifiers.menu_func)
    print("Addon \"Apply Modifiers\" enabled")

def unregister():
    bpy.utils.unregister_class(apply_modifiers.ApplyModifiers)
    bpy.types.VIEW3D_MT_object_apply.remove(apply_modifiers.menu_func)
    print("Addon \"Apply Modifiers\" disabled")

if __name__ == "__main__":
    register()