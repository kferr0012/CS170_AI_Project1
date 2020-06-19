from tree_and_node_class import *
from operations import *
import copy


def assign_g_with_uniform_cost_search(given_node):
    #All operations are the same so the cost is just the depth
    given_node.G=given_node.depth
    return None
