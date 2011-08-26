from expression import expFromTree
from util import typedNameListFromTrees

class Method:
    def __init__(self, t, name, args, exp):
        self.t = t
        self.name = name
        self.args = args
        self.exp = exp
        
    def execute(self, params, ct):
        var_dict = {}
        for i, arg in enumerate(self.args):
            var_dict[arg.name] = params[i]

        return self.exp.execute(ct, var_dict)

def methodsFromTree(root):
    # ^(METHOD $type $name $vs $exp)
    children = root.getChildren()

    # DEBUG
    print "Method.children", [child.text for child in children]
    
    type = children[0]
    name = children[1]
    args = typedNameListFromTrees(children[2].getChildren())
    exp = expFromTree(children[3])
    return Method(type, name, args, exp)