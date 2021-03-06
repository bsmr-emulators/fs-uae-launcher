'''OpenGL extension ARB.get_proc_address

This module customises the behaviour of the 
OpenGL.raw.GLX.ARB.get_proc_address to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds a function to return the address of GLX
	and GL extension functions, given the function name. This is
	necessary with (for example) heterogenous implementations where
	hardware drivers may implement extension functions not known to the
	link library; a similar situation on Windows implementations
	resulted in the wglGetProcAddress function.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/get_proc_address.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.ARB.get_proc_address import *
from OpenGL.raw.GLX.ARB.get_proc_address import _EXTENSION_NAME

def glInitGetProcAddressARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION