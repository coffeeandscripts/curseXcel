
from setuptools import setup
import platform, warnings

#Pypy dependency support
python_implementation = platform.python_implementation()

install_requires = ['ncurses',]
if python_implementation == "PyPy":
    install_requires = ['ncurses',]
elif python_implementation != "CPython":
    warnings.warn("We don't know how to deal with the {} runtime. Treating it like CPython".format(python_implementation), RuntimeWarning)

setup(name='curseXcel',
    version='0.0.1',
    description='ncurses library to generate and manipulate tables',
    url='http://github.com/coffeeandscripts/curseXcel',
    author='coffeeandscripts',
    author_email='coffeeandscripts@gmail.com',
    license='GNU',
    packages=['curseExcel',],
    install_requires=install_requires,
    include_package_data=True
)
