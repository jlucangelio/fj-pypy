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

# Constructor objects represent class constructors.
# As constructors in FJ have a fixed structure,
# they are not represented as ordinary methods.
# Constructor objects call the constructor of the superclass,
# and then assign the object fields.
# The constructor for the Object class, ObjectConstructor,
# is the only place where objects are created.

from obj import FJObject
from util import typed_name_list_from_trees, name_list_from_trees, init_list_from_trees

def constructorFromTree(class_name, root):
    # ^(CONSTRUCTOR $cname $vs $ns $ins)

    children = root.getChildren()

    # DEBUG
    print "Constructor.children", [child.text for child in children]
    
    name = children[0]
    variables = typed_name_list_from_trees(children[1].getChildren())
    sargs = name_list_from_trees(children[2].getChildren())
    inits = init_list_from_trees(children[3:])
    return Constructor(class_name, name, variables, sargs, inits)

class Constructor(object):
    def __init__(self, class_name, name, variables, sargs, inits):
        self.class_name = class_name
        self.name = name
        self.variables = variables
        self.sargs = sargs
        self.inits = inits

    def call(self, ct, params):
        var_dict = {}
        for i, var in enumerate(self.variables):
            var_dict[var.name] = params[i]
        
        klass = ct[self.class_name]
        parent = ct[klass.parent]
        res = parent.construct(ct, self.sargs)
        for init in self.inits:
            res.fields[init.l] = var_dict[init.r]
        
        return res

class ObjectConstructor(Constructor):
    def __init__(self):
        super(ObjectConstructor, self).__init__("FJObject", "FJObject", [], [], [])
    
    def call(self, ct, params):
        return FJObject("FJObject", {})
