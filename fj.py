# Copyright 2011 Jorge Lucangeli Obes
#
# This file is part of fj-llvm.
#
# fj-llvm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fj-llvm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fj-llvm. If not, see <http://www.gnu.org/licenses/>.

import sys

import antlr3
import antlr3.tree

from parser.fjParser import fjParser
from parser.fjLexer import fjLexer

f = sys.argv[1]

char_stream = antlr3.ANTLRFileStream(f)
lexer = fjLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = fjParser(tokens)

r = parser.program()
