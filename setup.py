# This file is part of hello-copr <https://pagure.io/copr-tito-quickdoc>.
# Copyright (C) 2020 Christopher Engelhard
#
# hello-copr is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hello-copr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hello-copr.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

# use README.md as readme
def readme():
    with open('README.md') as f:
        return f.read()

# setuptools configuration
setup(
    name='hellocopr',
    description='A trivial demo program used to explain packaging for Fedora Copr',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://pagure.io/copr-tito-quickdoc',
    author='Christopher Engelhard',
    license='GPLv3',
    version='1.0.0',

    # tell distutils packages are under src directory
    package_dir={
      '': 'src',
    },
    packages=find_packages('src'),
    install_requires=['colorama'],

    # automatically create console scripts
    entry_points={
      'console_scripts': ['hellocopr=hellocopr.hellocopr:main'],
    },
    )
