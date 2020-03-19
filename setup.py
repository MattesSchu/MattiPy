
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='matti',
    version='0.0.0',
    description='Learning python by writing my personal Matrix library',
    long_description=readme,
    author='Mattes Schumann',
    author_email='me@kennethreitz.com',
    url='https://github.com/MattesSchu/PyMatti',
    license=license,
    packages=find_packages(exclude=('tests'))#, 'docs'))
)