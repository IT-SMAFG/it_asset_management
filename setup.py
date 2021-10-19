from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in it_asset_management/__init__.py
from it_asset_management import __version__ as version

setup(
	name="it_asset_management",
	version=version,
	description="Manage IT Asset",
	author="Lutfidmz",
	author_email="lutfidmz@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
