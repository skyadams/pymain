# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

setup(
	name='pymain',
	version='1.0.0',
	description='Simple package to make a "Main" similar to C',
	long_description=readme,
	author='Sky Adams',
	author_email='skrulladams@yahoo.com',
	url='https://github.com/skyadams/pymain',
	license=license,
	packages=find_packages()
)
