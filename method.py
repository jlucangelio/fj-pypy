from expression import exp_from_tree
from util import typedNameListFromTrees

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
    args = typedNameListFromTrees(children[2].getChildren())
    exp = exp_from_tree(children[3])
    return Method(type, name, args, exp)