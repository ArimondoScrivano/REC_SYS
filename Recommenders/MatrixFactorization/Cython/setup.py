from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize(
        [
            "MatrixFactorization_Cython_Epoch.pyx",
            "MatrixFactorizationImpressions_Cython_Epoch.pyx",
        ],
        compiler_directives={'language_level': "3"}  # Compatibilità con Python 3
    ),
    include_dirs=[numpy.get_include()]
)