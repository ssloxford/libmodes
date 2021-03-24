import runpy
#from distutils.core import setup, Extension
from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py

# Third-party modules - we depend on numpy for everything
import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
	numpy_include = numpy.get_include()
except AttributeError:
	numpy_include = numpy.get_numpy_include()

module1 = Extension('_pylibmodes',
#                    define_macros = [('MAJOR_VERSION', '1'),
#                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['include'],
#                    libraries = ['tcl83'],
#                    library_dirs = ['/usr/local/lib'],
#                    sources = ['src/mode-s.c', 'swig/modes_wrap.c'])
                    sources = ['src/mode-s.c', 'src/modes.i'])

# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


setup (
	name = 'pylibmodes',
	version = '1.0',
	description = 'Python wrapper to libmodes',
	author = 'Richard Baker',
	author_email = 'richard.baker@cs.ox.ac.uk',
	url = 'https://docs.python.org/extending/building',

	#long_description = '''Python wrapper to libmodes''',

	packages=find_packages('src'),
	package_dir={'': 'src'},
	ext_modules = [module1],
	py_modules = ["pylibmodes"],
	cmdclass = { 'build_py': BuildPy }
)
