
from distutils.core import setup
from Cython.Build import cythonize
from setuptools import setup
from setuptools.command.build_ext import build_ext as _build_ext
from distutils.extension import Extension

class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

extensions = [Extension("c1", ["c1.pyx"])]



setup(
        name = "c1",
        ext_modules = cythonize(extensions),  # accepts a glob pattern
        cmdclass={'build_ext':build_ext},
    	setup_requires=['numpy'],
    )
