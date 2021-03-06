# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# Author: Anne Mulhern <mulhern@cs.wisc.edu>

import os
import sys
import setuptools
if sys.version_info[0] < 3:
    from codecs import open

def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))

README = local_file("README.rst")

with open(local_file("src/justoptions_gui/_version.py")) as o:
        exec(o.read())

setuptools.setup(
    name='justoptions-gui',
    version=__version__,
    url='http://pythonhosted.org/justoptions-gui/',
    author='Anne Mulhern',
    author_email='mulhern@cs.wisc.edu',
    description='GUI library for exhibiting options',
    long_description=open(README, encoding='utf-8').read(),
    platforms=['Linux'],
    license='GPL 2+',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'Topic :: System :: Operating System Kernels :: Linux',
    ],
    install_requires = [
        'six'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    )
