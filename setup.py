from setuptools import find_packages, setup
from pathlib import Path


this_directory = Path(__file__).parent
desc = (this_directory / "README.md").read_text()
setup(
    name='PyCircTools',
    packages=find_packages(include=['Exceptions', 'LogicGates', 'Multiplexers', 'Latches', 'Operators']),
    version='1.0.0',
    description='PyCircTools, a python library to build digital circuits.',
    author='LovetheFrogs',
    license='GPL-3.0',
    url='https://github.com/LovetheFrogs/PyCircTools',
    long_description=desc,
    long_description_content_type='text/markdown'
)
