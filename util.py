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

# Miscellaneous utilities.

from collections import namedtuple

TypedName = namedtuple("TypedName", "t name")
InitStatement = namedtuple("InitStatement", "l r")

def name_list_from_trees(trees):
    names = []
    for tree in trees:
        names.append(tree.text)

    return names

def typed_name_list_from_trees(trees):
    tnames = []
    for tree in trees:
        children = tree.getChildren()
        tname = TypedName(t=children[0].text, name=children[1].text)
        tnames.append(tname)

    return tnames

def typed_name_dict_from_trees(trees):
    tnames = {}
    for tree in trees:
        children = tree.getChildren()
        tname = TypedName(t=children[0].text, name=children[1].text)
        tnames[tname.name] = tname

    return tnames

def init_list_from_trees(trees):
    inits = []
    for tree in trees:
        children = tree.getChildren()
        init = InitStatement(l=children[0].text, r=children[1].text)
        inits.append(init)
    return inits

def fields_from_tree(root):
    fieldTrees = root.getChildren()
    fields = typed_name_dict_from_trees(fieldTrees)
    return fields

def debug_node(node):
    print node.text, [child.text for child in node.getChildren()]
