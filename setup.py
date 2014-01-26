#!/usr/bin/env python
# encoding: utf-8

import os
import re
from setuptools import setup, find_packages


def docs_read(fname):
    return open(os.path.join(os.path.dirname(__file__), 'docs', fname)).read()

def version_read():
    settings_file = open(os.path.join(os.path.dirname(__file__), 'lib', 'status', 'settings.py')).read()
    major_regex = """major_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    minor_regex = """minor_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    patch_regex = """patch_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    major_match = re.search(major_regex, settings_file)
    minor_match = re.search(minor_regex, settings_file)
    patch_match = re.search(patch_regex, settings_file)
    major_version = major_match.group(1)
    minor_version = minor_match.group(1)
    patch_version = patch_match.group(1)
    if len(major_version) == 0:
        major_version = 0
    if len(minor_version) == 0:
        minor_version = 0
    if len(patch_version) == 0:
        patch_version = 0
    return major_version + "." + minor_version + "." + patch_version


setup(
    name='status',
    version=version_read(),
    description='Report the HTTP status codes for GET and POST requests',
    long_description=(docs_read('README.rst')),
    url='https://github.com/chrissimpkins/status',
    license='MIT license',
    author='Christopher Simpkins',
    author_email='chris@zerolabs.net',
    platforms=['any'],
    entry_points = {
        'console_scripts': [
            'status = status.app:main'
        ],
    },
    packages=find_packages("lib"),
    package_dir={'': 'lib'},
    install_requires=['Naked'],
    keywords='HTTP, request, POST, GET, status code, status, website, URL',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        'Topic :: System',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Monitoring'
    ],
)
