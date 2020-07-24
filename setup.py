# This file is part of hellocopr <https://pagure.io/copr-tito-quickdoc>.
# Copyright (C) 2020 Christopher Engelhard
#
# hellocopr is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hellocopr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hellocopr.  If not, see <http://www.gnu.org/licenses/>.

import codecs, os.path
from setuptools import setup, find_packages

# use README.md as readme
def readme():
    with open('README.md') as f:
        return f.read()

# get __version__ from a file
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

# setuptools configuration
setup(
    name='hellocopr',
    description='A trivial demo program used to explain packaging for Fedora Copr',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://pagure.io/copr-tito-quickdoc',
    author='Christopher Engelhard',
    author_email='ce@lcts.de',
    license='GPLv3',

    # extract version from source
    version=get_version("src/hellocopr/__init__.py"),

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
