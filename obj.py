# Copyright 2011 Jorge Lucangeli Obes
#
# This file is part of fj-pypy.
#
# fj-pypy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fj-pypy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fj-pypy. If not, see <http://www.gnu.org/licenses/>.

# FJObject objects represent FJ objects.
# They only hold their class and their instance variables.

class FJObject:
    def __init__(self, klass, fields):
        self.klass = klass
        self.fields = fields

    def __str__(self):
        return self.klass + "(" + str(self.fields) + ")"
