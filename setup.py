from setuptools import find_packages, setup


NAME = "CredentialManager"
VERSION = "1.0.0"

REQUIRES = ["certifi>=2017.4.17", "python-dateutil>=2.1"]

setup(
      name=NAME,
      version=VERSION,
      description="Credential Manager Client",
      author_email="spaz@jesassn.org",
      url="https://credmgr.jesassn.org",
      install_requires=REQUIRES,
      packages=find_packages(),
      include_package_data=True,
      long_description='API client for interacting with Credential Manager'
)