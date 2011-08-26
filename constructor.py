from obj import Object
from util import typedNameListFromTrees, nameListFromTrees, initListFromTrees

def constructorFromTree(class_name, root):
    # ^(CONSTRUCTOR $cname $vs $ns $ins)

    children = root.getChildren()

    # DEBUG
    print "Constructor.children", [child.text for child in children]
    
    name = children[0]
    variables = typedNameListFromTrees(children[1].getChildren())
    sargs = nameListFromTrees(children[2].getChildren())
    inits = initListFromTrees(children[3:])
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
        super(ObjectConstructor, self).__init__("Object", "Object", [], [], [])
    
    def call(self, ct, params):
        return Object("Object", {})