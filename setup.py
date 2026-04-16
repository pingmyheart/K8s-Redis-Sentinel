import warnings

from setuptools import setup, find_packages

# Suppress all warnings
warnings.filterwarnings("ignore")

setup(
    name='redis',
    version='8.2.6.dev0',
    packages=find_packages()
)
