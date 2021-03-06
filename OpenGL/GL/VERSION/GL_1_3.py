'''OpenGL extension VERSION.GL_1_3

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_3 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_1_3.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.VERSION.GL_1_3 import *
from OpenGL.raw.GL.VERSION.GL_1_3 import _EXTENSION_NAME

def glInitGl13VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
GL_SRC0_ALPHA = GL_SOURCE0_ALPHA # alias
GL_SRC0_RGB = GL_SOURCE0_RGB # alias
GL_SRC1_ALPHA = GL_SOURCE1_ALPHA # alias
GL_SRC1_RGB = GL_SOURCE1_RGB # alias
GL_SRC2_ALPHA = GL_SOURCE2_ALPHA # alias
GL_SRC2_RGB = GL_SOURCE2_RGB # alias


for typ,arrayType in (
    ('d',arrays.GLdoubleArray),
    ('f',arrays.GLfloatArray),
    ('i',arrays.GLintArray),
    ('s',arrays.GLshortArray),
):
    for size in (1,2,3,4):
        name = 'glMultiTexCoord%(size)s%(typ)sv'%globals()
        globals()[name] = arrays.setInputArraySizeType(
            globals()[name],
            size,
            arrayType,
            'v',
        )
        try:
            del size,name
        except NameError as err:
            pass
    try:
        del typ,arrayType
    except NameError as err:
        pass

for typ,arrayType in (
    ('d',arrays.GLdoubleArray),
    ('f',arrays.GLfloatArray),
):
    for function in ('glLoadTransposeMatrix','glMultTransposeMatrix'):
        name = '%s%s'%(function,typ)
        globals()[name] = arrays.setInputArraySizeType(
            globals()[name],
            16,
            arrayType,
            'm',
        )
        try:
            del function,name
        except NameError as err:
            pass
    try:
        del typ,arrayType
    except NameError as err:
        pass

from OpenGL import wrapper
from OpenGL.raw.GL.VERSION import GL_1_3 as _simple
from OpenGL.GL import images, glget

for dimensions in (1,2,3):
    for function in ('glCompressedTexImage%sD','glCompressedTexSubImage%sD'):
        name = function%(dimensions,)
        globals()[ name ] = images.compressedImageFunction(
            getattr( _simple, name )
        )
        try:
            del name, function
        except NameError as err:
            pass
    try:
        del dimensions
    except NameError as err:
        pass

if _simple.glGetCompressedTexImage:
    def glGetCompressedTexImage( target, level, img=None ):
        """Retrieve a compressed texture image"""
        if img is None:
            length = glget.glGetTexLevelParameteriv(
                target, 0,
                _simple.GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB,
            )
            img = arrays.ArrayDataType.zeros( (length,), constants.GL_UNSIGNED_BYTE )
        return _simple.glGetCompressedTexImage(target, 0, img);
