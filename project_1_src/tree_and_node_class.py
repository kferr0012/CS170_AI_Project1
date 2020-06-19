from anytree import AnyNode, RenderTree

#This function takes an initial state as a paramter
#Labels the node as "root"
#returns the node
def build_tree(initial_state):
    root_node = AnyNode(name="root",current_state=initial_state,G=0,H=0)
    return root_node

def build_node(grid_state,parent=None):
    new_node = AnyNode(current_state=grid_state , g=None , h=None , f=None , isValid=None, parent=None)
    return new_node
