from constructor import constructorFromTree, ObjectConstructor
from method import methodsFromTree
from util import fieldsFromTree

class InvalidTreeException(BaseException):
    pass

class Class(object):
    CLASS = "class"

    def __init__(self, parent, name, fields, constructor, methods):
        self.parent = parent
        self.name = name
        self.fields = fields
        self.constructor = constructor
        self.methods = methods

    def construct(self, ct, params):
        res = self.constructor.call(ct, params)
        return res

    @staticmethod
    def fromTree(root):
        # ^(CLASS $cname $pname fields constructor methods)
        if root.text != Class.CLASS:
            print root.text
            raise InvalidTreeException

        children = root.getChildren()

        # DEBUG
        print "Class.children", [child.text for child in children]
        
        name = children[0].text
        parent = children[1].text
        fields = fieldsFromTree(children[2])

        # DEBUG
        print "fields", fields
        
        constructor = constructorFromTree(name, children[3])
        methods = methodsFromTree(children[4])
        return Class(parent, name, fields, constructor, methods)

cobject = Class("Object", "Object", [], ObjectConstructor(), [])