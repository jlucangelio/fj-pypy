from obj import Object
from util import debug_node

BASE = "BASE_EXPRESSION"
DOT = "DOT_EXPRESSION"
NEW = "new"
THIS = "this"

class Expression:
    def execute(self):
        raise NotImplementedError("subclass responsibility")

class BaseExpression(Expression):
    pass

class DotExpression(Expression):
    pass

class VarExpression(BaseExpression):
    def __init__(self, vname):
        self.vname = vname
    
    def execute(self, ct, var_dict):
        return var_dict[self.vname]

class NewExpression(BaseExpression):
    def __init__(self, cname, params):
        self.cname = cname
        self.params = params
    
    def execute(self, ct, var_dict):
        res = ct[self.cname].construct(ct, self.params)
        return res

class CastExpression(BaseExpression):
    def __init__(self, cname, exp):
        self.cname = cname
        self.exp = exp

    def execute(self, ct, var_dict):
        obj = self.exp.execute()
        res = Object(self.cname, obj.fields)
        return res

class FieldExpression(DotExpression):
    def __init__(self, this, fname):
        self.this = this
        self.fname = fname
    
    def execute(self, ct, var_dict):
        return self.this.fields[self.fname]

class MethodCallExpression(DotExpression):
    def __init__(self, this, mname, params):
        self.this = this
        self.mname = mname
        self.params = params

    def execute(self, ct, var_dict):
        klass = ct[self.this]
        m = klass.methods[self.mname]
        return m.execute(self.params, ct)

def expFromTree(root):
    text = root.text
    children = root.getChildren()
    
    if text == BASE:
        if children[0].text == NEW:
            # new
            expressions = [expFromTree(child) for child in children[2].getChildren()]
            # DEBUG
            return NewExpression(children[1].text, expressions)
        elif len(children) == 1:
            # var
            return VarExpression(children[1].text)
        else:
            # cast
            return CastExpression(children[1].text, expFromTree(children[2]))
    elif text == DOT:
        if children[0].text == THIS:
            this = THIS
        elif children[0].text == BASE:
            this = expFromTree(children[0])
        
        if len(children) == 2:
            # field
            field_name = children[1]
            return FieldExpression(this, field_name)
        elif len(children) > 2:
            # method call
            method_name = children[1]
            expressions = [expFromTree(child) for child in children[2].getChildren()]
            return MethodCallExpression(this, method_name, expressions)
