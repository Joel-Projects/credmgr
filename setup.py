from setuptools import find_packages, setup


NAME = "CredentialManager"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["certifi>=2017.4.17", "python-dateutil>=2.1", "urllib3>=1.23"]

setup(name=NAME, version=VERSION, description="Credential Manager", author_email="", url="", keywords=["Swagger", "Credential Manager"],
    install_requires=REQUIRES, packages=find_packages(), include_package_data=True, long_description='''\
    API for interacting with Credential Manager 
    ''')