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

# Class objects represent FJ classes.
# They hold the name of the class and its parent,
# the dictionary of fields and methods,
# and the constructor for the class.

from constructor import constructorFromTree, ObjectConstructor
from method import methods_from_tree
from util import fields_from_tree

class InvalidTreeException(BaseException):
    pass

class Class(object):
    CLASS = "class"

    def __init__(self, parent, name, fields, constructor, methods):
        self.parent = parent
        self.name = name
        self.fields = fields
        self.constructor = constructor
        self.methods = methods

    def construct(self, ct, params):
        # DEBUG
        print "Class.construct", self.name
        
        res = self.constructor.call(ct, params)
        res.klass = self.name
        return res

    @staticmethod
    def fromTree(root):
        # ^(CLASS $cname $pname fields constructor methods)

        if root.text != Class.CLASS:
            print root.text
            raise InvalidTreeException

        children = root.getChildren()

        # DEBUG
        print "Class.children", [child.text for child in children]
        
        name = children[0].text
        parent = children[1].text
        fields = fields_from_tree(children[2])

        # DEBUG
        print "fields", fields
        
        constructor = constructorFromTree(name, children[3])
        methods = methods_from_tree(children[4])
        
        # DEBUG
        print "methods", methods
        
        return Class(parent, name, fields, constructor, methods)

# Object class is hardcoded
CObject = Class("Object", "Object", [], ObjectConstructor(), {})
