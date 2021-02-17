from os import path
import re
from textwrap import dedent

from setuptools import find_packages, setup


project_name = "credmgr"

root = path.abspath(path.dirname(__file__))

with open(path.join(root, project_name, "const.py")) as f:
    __version__ = re.search(r"__version__ = '(.+)'", f.read()).group(1)

with open(path.join(root, "README.rst")) as f:
    long_description = f.read()

requires = [
    "setuptools",
    "python-dateutil",
    "requests",
    "praw",
    "prawcore",
    "requests_toolbelt",
]
tests_requires = [
    "coverage",
    "pytest",
    "betamax",
    "betamax_serializers",
    "pytest-mock",
    "pytest-xdist",
    "pytest-cov",
    "mock",
]
docs_requires = ["sphinx", "sphinx_rtd_theme"]
extras = {"test": tests_requires, "docs": docs_requires}


if not path.isfile(path.join(root, project_name, ".credmgr.ini")):
    default_config = dedent(
        """
    [DEFAULT]
    server = https://credmgr.jesassn.org
    endpoint = /api/v1
    dateformat = %%m/%%d/%%Y %%I:%%M:%%S %%p %%Z"""
    )
    with open(path.join(root, project_name, ".credmgr.ini"), "w") as f:
        f.write(default_config)

setup(
    name=project_name,
    author="Lil_SpazJoekp",
    author_email="spaz@jesassn.org",
    license="Proprietary",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: Other/Proprietary License",
    ],
    python_requires=">=3.6",
    description="Credential Manager API Client",
    include_package_data=True,
    install_requires=requires,
    long_description=long_description,
    packages=find_packages(exclude=["tests", "tests.*"]),
    test_suite="tests",
    tests_require=tests_requires,
    extras_require=extras,
    url="https://credmgr.jesassn.org",
    version=__version__,
)
