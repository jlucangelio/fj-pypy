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

# Method objects represent methods.
# Each method holds its parameters and an expression
# that represents its body.
# Methods can be executed, which means executing their expressions
# with the appropiate substitutions.

from expression import exp_from_tree
from util import typed_name_list_from_trees

THIS = "this"

class Method:
    def __init__(self, t, name, args, exp):
        self.t = t
        self.name = name
        self.args = args
        self.exp = exp
        
    def execute(self, this, params, ct):
        var_dict = {}
        for i, arg in enumerate(self.args):
            var_dict[arg.name] = params[i]
        
        var_dict[THIS] = this

        return self.exp.execute(ct, var_dict)

def methods_from_tree(root):
    # ^(METHODS method*)
    
    children = root.getChildren()
    methods = [method_from_tree(child) for child in children]
    return dict([(m.name, m) for m in methods])

def method_from_tree(root):
    # ^(METHOD $type $name $vs $exp)
    
    children = root.getChildren()

    # DEBUG
    print "Method.children", [child.text for child in children]
    
    type = children[0].text
    name = children[1].text
    args = typed_name_list_from_trees(children[2].getChildren())
    exp = exp_from_tree(children[3])
    return Method(type, name, args, exp)
