'''OpenGL extension EXT.subtexture

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.subtexture to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows a contiguous portion of an already-existing
	texture image to be redefined, without affecting the remaining portion
	of the image, or any of the other state that describe the texture.  No
	provision is made to query a subregion of a texture.
	
	Semantics for null image pointers are defined for TexImage1D,
	TexImage2D, and TexImage3DEXT.  Null image pointers can be used by
	applications to effectively support texture arrays whose dimensions
	are not a power of 2.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/subtexture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.subtexture import *
from OpenGL.raw.GL.EXT.subtexture import _EXTENSION_NAME

def glInitSubtextureEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION