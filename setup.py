
from setuptools import setup
import platform, warnings

#Pypy dependency support
python_implementation = platform.python_implementation()

setup(name='curseXcel',
    version='0.0.1',
    description='ncurses library to generate and manipulate tables',
    url='http://github.com/coffeeandscripts/curseXcel',
    author='coffeeandscripts',
    packages=['curseXcel'],
    author_email='coffeeandscripts@gmail.com',
    license='GNU',
    include_package_data=True
)
