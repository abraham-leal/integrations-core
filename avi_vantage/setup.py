# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from codecs import open  # To use a consistent encoding
from os import path

from setuptools import setup

HERE = path.dirname(path.abspath(__file__))

# Get version info
ABOUT = {}
with open(path.join(HERE, 'datadog_checks', 'avi_vantage', '__about__.py')) as f:
    exec(f.read(), ABOUT)

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def get_dependencies():
    dep_file = path.join(HERE, 'requirements.in')
    if not path.isfile(dep_file):
        return []

    with open(dep_file, encoding='utf-8') as f:
        return f.readlines()


CHECKS_BASE_REQ = 'datadog-checks-base>=23.1.2'


setup(
    name='datadog-avi_vantage',
    version=ABOUT['__version__'],
    description='The Avi Vantage check',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='datadog agent avi_vantage check',
    # The project's main homepage.
    url='https://github.com/DataDog/integrations-core',
    # Author details
    author='Datadog',
    author_email='packages@datadoghq.com',
    # License
    license='BSD-3-Clause',
    python_requires='>=3.8',
    # See https://pypi.org/classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
    ],
    # The package we're going to ship
    packages=['datadog_checks.avi_vantage'],
    # Run-time dependencies
    install_requires=[CHECKS_BASE_REQ],
    extras_require={'deps': get_dependencies()},
    # Extra files to ship with the wheel package
    include_package_data=True,
)
