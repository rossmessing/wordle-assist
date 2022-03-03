from setuptools import setup, find_packages

from wordle import __version__ as version

setup(
    name="wordle-assist",
    author="Ross Messing",
    version=version,
    packages=find_packages(exclude=("tests",))
)