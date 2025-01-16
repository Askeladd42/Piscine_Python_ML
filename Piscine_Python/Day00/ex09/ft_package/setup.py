from setuptools import setup, find_packages

setup(
	name="ft_package",
	version="0.0.1",
	summary="A simple example package",
	author="plam",
	author_email="plam@student.42.fr",
	description="A simple example package",
	long_description=open('README.md').read(),
	url="https://github.com/Askeladd42/ft_package",
	license="MIT",
	packages=find_packages(),
	classifiers=[],
	entrypoints={},
)