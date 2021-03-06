'''OpenGL extension EXT.shader_integer_mix

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.shader_integer_mix to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/shader_integer_mix.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.EXT.shader_integer_mix import *
from OpenGL.raw.GLES2.EXT.shader_integer_mix import _EXTENSION_NAME

def glInitShaderIntegerMixEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION