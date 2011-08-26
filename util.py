from collections import namedtuple

TypedName = namedtuple("TypedName", "t name")
InitStatement = namedtuple("InitStatement", "l r")

def nameListFromTrees(trees):
    names = []
    for tree in trees:
        names.append(tree.text)

    return names

def typedNameListFromTrees(trees):
    tnames = []
    for tree in trees:
        children = tree.getChildren()
        tname = TypedName(t=children[0].text, name=children[1].text)
        tnames.append(tname)

    return tnames

def typedNameDictFromTrees(trees):
    tnames = {}
    for tree in trees:
        children = tree.getChildren()
        tname = TypedName(t=children[0].text, name=children[1].text)
        tnames[tname.name] = tname

    return tnames

def initListFromTrees(trees):
    inits = []
    for tree in trees:
        children = tree.getChildren()
        init = InitStatement(l=children[0].text, r=children[1].text)
        inits.append(init)
    return inits

def fieldsFromTree(root):
    fieldTrees = root.getChildren()
    fields = typedNameDictFromTrees(fieldTrees)
    return fields

def debug_node(node):
    print node.text, [child.text for child in node.getChildren()]