from setuptools import setup, find_packages
import os

version = open (os.path.join("plonetheme", "p2", "version.txt")).read().strip()

setup(
	name='plonetheme.p2',
	version=version,
	description="An installable theme for Plone 3.0",
	long_description=open("README.txt").read() + "\n" +
		open(os.path.join("docs", "HISTORY.txt")).read(),
	# Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
	"Framework :: Plone",
	"Programming Language :: Python",
	"Topic :: Software Development :: Libraries :: Python Modules",
	],
	keywords='web zope plone theme',
	author='Paul-Michael Agapow',
	author_email='agapow@bbsrc.ac.uk',
	url='http://www.agapow.net/software/plonetheme.p2',
	license='BSD',
	packages=find_packages(exclude=['ez_setup']),
	namespace_packages=['plonetheme'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
	'setuptools',
		# -*- Extra requirements: -*-
	],
	entry_points="""
		# -*- Entry points: -*-

		[distutils.setup_keywords]
		paster_plugins = setuptools.dist:assert_string_list

		[egg_info.writers]
		paster_plugins.txt = setuptools.command.egg_info:write_arg
	""",
	paster_plugins = ["ZopeSkel"],
)
