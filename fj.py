#!/usr/bin/python
#
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

import sys

import antlr3
import antlr3.tree

from parser.fjParser import fjParser
from parser.fjLexer import fjLexer

from klass import Class, cobject
from expression import exp_from_tree
from util import debug_node

f = sys.argv[1]

char_stream = antlr3.ANTLRFileStream(f)
lexer = fjLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = fjParser(tokens)

r = parser.program()
root = r.tree

children = r.tree.getChildren()
cds = children[:-1]
e = children[-1]

ct = {}

for cd in cds:
    klass = Class.fromTree(cd)
    ct[klass.name] = klass

# DEBUG
print "EXEC:"
debug_node(e)
exp = exp_from_tree(e)

# DEBUG
print "CT", ct
print "e", exp

ct["Object"] = cobject
var_dict = {}
print exp.execute(ct, var_dict)
