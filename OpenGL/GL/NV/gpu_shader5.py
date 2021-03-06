'''OpenGL extension NV.gpu_shader5

This module customises the behaviour of the 
OpenGL.raw.GL.NV.gpu_shader5 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a set of new features to the OpenGL Shading
	Language and related APIs to support capabilities of new GPUs.  Shaders
	using the new functionality provided by this extension should enable this
	functionality via the construct
	
	  #extension GL_NV_gpu_shader5 : require     (or enable)
	
	This extension was developed concurrently with the ARB_gpu_shader5
	extension, and provides a superset of the features provided there.  The
	features common to both extensions are documented in the ARB_gpu_shader5
	specification; this document describes only the addition language features
	not available via ARB_gpu_shader5.  A shader that enables this extension
	via an #extension directive also implicitly enables the common
	capabilities provided by ARB_gpu_shader5.
	
	In addition to the capabilities of ARB_gpu_shader5, this extension
	provides a variety of new features for all shader types, including:
	
	  * support for a full set of 8-, 16-, 32-, and 64-bit scalar and vector
	    data types, including uniform API, uniform buffer object, and shader
	    input and output support;
	
	  * the ability to aggregate samplers into arrays, index these arrays with
	    arbitrary expressions, and not require that non-constant indices be
	    uniform across all shader invocations;
	
	  * new built-in functions to pack and unpack 64-bit integer types into a
	    two-component 32-bit integer vector;
	
	  * new built-in functions to pack and unpack 32-bit unsigned integer
	    types into a two-component 16-bit floating-point vector;
	
	  * new built-in functions to convert double-precision floating-point
	    values to or from their 64-bit integer bit encodings;
	
	  * new built-in functions to compute the composite of a set of boolean
	    conditions a group of shader threads;
	
	  * vector relational functions supporting comparisons of vectors of 8-,
	    16-, and 64-bit integer types or 16-bit floating-point types; and
	
	  * extending texel offset support to allow loading texel offsets from
	    regular integer operands computed at run-time, except for lookups with
	    gradients (textureGrad*).
	
	This extension also provides additional support for processing patch
	primitives (introduced by ARB_tessellation_shader).
	ARB_tessellation_shader requires the use of a tessellation evaluation
	shader when processing patches, which means that patches will never
	survive past the tessellation pipeline stage.  This extension lifts that
	restriction, and allows patches to proceed further in the pipeline and be
	used
	
	  * as input to a geometry shader, using a new "patches" layout qualifier;
	
	  * as input to transform feedback;
	
	  * by fixed-function rasterization stages, in which case the patches are
	    drawn as independent points.
	
	Additionally, it allows geometry shaders to read per-patch attributes
	written by a tessellation control shader using input variables declared
	with "patch in".
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/gpu_shader5.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.gpu_shader5 import *
from OpenGL.raw.GL.NV.gpu_shader5 import _EXTENSION_NAME

def glInitGpuShader5NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION