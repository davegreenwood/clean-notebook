"""
setup.py
Entry point which give the command line call: 'clnb'
To use, from the directory containing this file:
pip install -e .
NB: the -e flag (editable) allows user changes to the package on disk.
"""
from setuptools import setup

setup(name='clean-notebook',
      version='0.1',
      description='Strip the outputs from a jupyter notebook.',
      author='Dave Greenwood',
      py_modules=['cleannb'],
      zip_safe=False,
      entry_points={'console_scripts': [
          'cnb=cleannb:main'
      ]}
      )
