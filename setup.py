from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ksa_vat/__init__.py
from ksa_vat import __version__ as version

setup(
	name='ksa_vat_zakat',
	version=version,
	description='KSA VAT',
	author='Wajihah',
	author_email='ribrahim@wajihah.sa',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
