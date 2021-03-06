'''OpenGL extension VERSION.GL_4_1

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_4_1 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_4_1.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.VERSION.GL_4_1 import *
from OpenGL.raw.GL.VERSION.GL_4_1 import _EXTENSION_NAME

def glInitGl41VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.GL.ARB.ES2_compatibility import *
from OpenGL.GL.ARB.get_program_binary import *
from OpenGL.GL.ARB.separate_shader_objects import *
from OpenGL.GL.ARB.shader_precision import *
from OpenGL.GL.ARB.vertex_attrib_64bit import *
from OpenGL.GL.ARB.viewport_array import *
