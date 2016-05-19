# Copyright (C) 2016 Anne Mulhern
#
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
# Anne Mulhern <mulhern@cs.wisc.edu>

"""
Errors for justbytes_gui.
"""
import abc

from six import add_metaclass


@add_metaclass(abc.ABCMeta)
class GUIError(Exception):
    """
    Superclass of all errors for this package.
    """
    pass


class GUIValueError(GUIError):
    """
    Raised if argument value is bad.
    """
    pass
