from setuptools import find_packages, setup
from pathlib import Path


this_directory = Path(__file__).parent
desc = (this_directory / "README.md").read_text()
setup(
    name='PyCircTools',
    packages=find_packages(include=['Exceptions', 'LogicGates', 'Multiplexers']),
    version='0.1.0',
    description='PyCircTools, a python circuit library.',
    author='LovetheFrogs',
    license='GPL-3.0',
    url='https://github.com/LovetheFrogs/CTools',
    long_description=desc,
    long_description_content_type='text/markdown'
)
