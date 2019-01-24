import sys
from setuptools import setup

if sys.version_info < (3, 7):
    sys.exit('Используйте Python 3.7+')

setup(
    name='bracket_sequence_checker',
    version='0.1.0',
    packages=[
        'bracket_sequence',
    ],
    url='',
    license='',
    author='aarifkhamdi',
    author_email='aarifkhamdi@gmail.com',
    description='',
    entry_points={
        'console_scripts': ['bracket_checker=bracket_sequence.bracket_sequence:_console_run']
    },
)
