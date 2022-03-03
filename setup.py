from setuptools import setup, find_packages

from wordle_assist import __version__ as version

setup(
    name="wordle_assist",
    author="Ross Messing",
    version=version,
    packages=find_packages(exclude=("tests",))
)