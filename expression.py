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

# Expression objects represent FJ expressions.
# Expressions appear both in methods and as the "main" part
# of FJ programs.
# Expressions can be executed, yielding an object which is the
# result of the computation of the expression.

from obj import FJObject

EXP = "EXPRESSION"
EXPS = "EXPRESSIONS"
BASE = "BASE_EXPRESSION"
DOT = "DOT_EXPRESSION"
NEW = "new"
THIS = "this"

class Expression(object):
    def execute(self):
        raise NotImplementedError("subclass responsibility")

class BaseExpression(Expression):
    pass

class DotExpression(Expression):
    def find_this(self, ct, var_dict):
        if self.this == THIS:
            o = var_dict[THIS]
        else:
            o = self.this.execute(ct, var_dict)
        
        return o

class VarExpression(BaseExpression):
    def __init__(self, vname):
        self.vname = vname
    
    def execute(self, ct, var_dict):
        return var_dict[self.vname]

class NewExpression(BaseExpression):
    def __init__(self, cname, param_exps):
        self.cname = cname
        self.param_exps = param_exps
    
    def execute(self, ct, var_dict):
        params = [param_exp.execute(ct, var_dict) for param_exp in self.param_exps]
        res = ct[self.cname].construct(ct, params)
        return res

class CastExpression(BaseExpression):
    def __init__(self, cname, exp):
        self.cname = cname
        self.exp = exp

    def execute(self, ct, var_dict):
        obj = self.exp.execute()
        res = FJObject(self.cname, obj.fields)
        return res

class FieldExpression(DotExpression):
    def __init__(self, this, fname):
        self.this = this
        self.fname = fname
    
    def execute(self, ct, var_dict):
        o = super(FieldExpression, self).find_this(ct, var_dict)
        return o.fields[self.fname]

class MethodCallExpression(DotExpression):
    def __init__(self, this, mname, params):
        self.this = this
        self.mname = mname
        self.params = params

    def execute(self, ct, var_dict):
        # DEBUG
        print "MethodCallExp.execute self.this", self.this
        
        if self.this == THIS:
            o = var_dict[THIS]
        else:
            o = self.this.execute(ct, var_dict)
        
        # DEBUG
        print "MethodCallExp.execute self.o", o
        
        klass = ct[o.klass]
        
        # DEBUG
        print "MethodCallExp.execute", klass.name, klass.methods, self.mname
        
        m = klass.methods[self.mname]
        return m.execute(o, self.params, ct)

def exp_from_tree(root):
    children = root.getChildren()
    child0 = children[0].text
    
    if child0 == BASE:
        this = base_exp_from_tree(children[0])
    elif child0 == THIS:
        this = THIS
    
    exp = this
    for dot_exp_tree in children[1:]:
        exp = dot_exp_from_tree(dot_exp_tree, exp)
    
    return exp

def base_exp_from_tree(root):
    children = root.getChildren()
    
    if children[0].text == NEW:
        # new
        expressions = [exp_from_tree(child) for child in children[2].getChildren()]
        return NewExpression(children[1].text, expressions)
    elif len(children) == 1:
        # var
        return VarExpression(children[0].text)
    elif len(children) == 2:
        # cast
        return CastExpression(children[0].text, exp_from_tree(children[1]))

def dot_exp_from_tree(root, this):
    children = root.getChildren()
    
    if len(children) == 1:
        # field
        field_name = children[0].text
        return FieldExpression(this, field_name)
    elif len(children) == 2:
        # method call
        method_name = children[0].text
        expressions = [exp_from_tree(child) for child in children[1].getChildren()]
        return MethodCallExpression(this, method_name, expressions)
