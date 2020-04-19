from os import path
import re

from setuptools import find_packages, setup


projectName = 'credmgr'

root = path.abspath(path.dirname(__file__))

with open(path.join(root, projectName, "const.py")) as f:
    __version__ = re.search('__version__ = "([^"]+)"', f.read()).group(1)

with open(path.join(root, "README.rst")) as f:
    longDescription = f.read()

requires = [
    'setuptools',
    'python-dateutil',
    'requests',
    'praw',
    'prawcore'
]
testsRequires = [
    'coverage',
    'pytest',
    'betamax',
    'sphinx'
]

setup(
    name=projectName,
    author='Lil_SpazJoekp',
    author_email='spaz@jesassn.org',
    python_requires='>=3.6',
    description='Credential Manager API Client',
    include_package_data=True,
    install_requires=requires,
    docs_requires=requires,
    license='Private',
    long_description=longDescription,
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='tests',
    tests_require=testsRequires,
    url='https://credmgr.jesassn.org',
    version=__version__
)