from setuptools import find_packages, setup

setup(
    name='CTools',
    packages=find_packages(include=['Exceptions', 'LogicGates']),
    version='0.0.1',
    description='CTools, a python circuit library.',
    author='LovetheFrogs',
    license='GPL-3.0'
)