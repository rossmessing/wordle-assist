from setuptools import setup, find_packages

from wordle_assist import __version__ as version


requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
    name="wordle_assist",
    author="Ross Messing",
    version=version,
    install_requires=requirements,
    packages=find_packages(exclude=("tests",))
)