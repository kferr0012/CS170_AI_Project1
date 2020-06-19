from tree_and_node_class import *
from operations import *
from misplaced_tile_h import *
from manhattan_d_h import *
from uniform_cost_search_g import *
from interface_and_helper_functions import *
import copy
import sys

# sys.setrecursionlimit(3500)

#Global Variables
explored_set = [] #contains nodes
frontier = []   #contains nodes
new_children = []

total_num_of_expanded_nodes = 0
max_num_nodes = 0

def increment_total_num_of_expanded_nodes():
    global total_num_of_expanded_nodes
    total_num_of_expanded_nodes+=1

def get_total_num_of_expanded_nodes():
    global total_num_of_expanded_nodes
    return total_num_of_expanded_nodes

def get_max_num_nodes():
    global max_num_nodess
    return max_num_nodes

def check_if_node_state_is_identical(node1,node2):
    if node1.current_state == node2.current_state:
        return True
    else:
        return False

def find_and_return_lowest_g_in_list(node_list):
    if len(node_list) == 0:
        print("Error 1")
        exit()
    else:
        min_node = node_list[0]

        for node_ in node_list:
            if node_.G < min_node.G:
                min_node =  node_
    return min_node

def find_min_g_node():
    global frontier

    minimum_node = frontier[0]

    for node in frontier:
        if node.G < minimum_node.G:
            minimum_node = node

    return minimum_node

def check_if_goal_in_frontier(goal_state,frontier):

    for node in frontier:
        if node.current_state == goal_state:
            return True
    return False

def check_if_node_state_in_explored_set(given_node,explored_set):
    for node in explored_set:
        if given_node.current_state == node:
            return True
    return False

def check_if_node_state_in_frontier(given_node,frontier):
    for node in frontier:
        if node.current_state == given_node.current_state:
            return True
    return False

def print_frontier_and_explored_set():
    global frontier
    global explored_set

    print("Printing Frontier:")
    for node in frontier:
        print(node)

    print("\nPrinting Explored Set:")
    for node in explored_set:
        print(node)


def uniform_cost_search_algorithm3(initial_node,goal_state):

    #Will contain nodes
    frontier_ = []

    frontier_size = 0

    #Initialize Frontier with Initial Node
    frontier_.append(initial_node)

    #Initialize Explored set to be empty, th=='ll hold states
    explored_set_ = []

    num_nodes_expanded = 0
    while True:
        if len(frontier_) == 0:
            print("Loop Ending")
            return

        #Choose a leaf node and remove from frontier
        #Find lowest G value in frontier
        min_node_ = frontier_[0]
        for node in frontier_:
            if node.G < min_node_.G:
                min_node_ = node
        next_node_ = min_node_


        #Remove from frontier
        frontier_.remove(next_node_)

        #Check if node contains a goal state then return the corresponding solution
        if next_node_.current_state == goal_state:
            assign_g_with_uniform_cost_search(next_node_)
            print('\nGoal state found! Depth = ' + str(next_node_.G) + '\n')
            print_state(next_node_.current_state)
            final_message(num_nodes_expanded,frontier_size)
            return next_node_

        # Add node to the explored set
        explored_set_.append(next_node_.current_state)

        #Expand the chosen node,
        #adding the resulting nodes to the frontier
        #only if not in the frontier or explored set
        if check_if_node_state_in_frontier(next_node_,frontier_) == False or check_if_node_state_in_explored_set(next_node_,explored_set_) == False:
            #Expand Chosen node
            expand_node(next_node_)
            num_nodes_expanded+=1

            #Print Message
            print_expand_node_and_g(next_node_)

            # #Print State
            # print_state(next_node_.current_state)


            #_Add expanded nodes into frontier
            for child in next_node_.children:
                assign_g_with_uniform_cost_search(child)
                if check_if_node_state_in_frontier(child,frontier_) == False and check_if_node_state_in_explored_set(child,explored_set_) == False:
                    frontier_.append(child)

                if len(frontier_) > frontier_size:
                    frontier_size = len(frontier_)

def A_star_with_misplaced_tile_heuristic2(initial_node,goal_state):

    #Will contain nodes
    frontier_ = []

    frontier_size = 0

    #Initialize Frontier with Initial Node
    frontier_.append(initial_node)

    #Initialize Explored set to be empty, th=='ll hold states
    explored_set_ = []

    num_nodes_expanded = 0
    while True:
        if len(frontier_) == 0:
            print("Loop Ending")
            return

        #Choose a leaf node and remove from frontier
        #Find lowest G value in frontier
        min_node_ = frontier_[0]
        for node in frontier_:
            if (node.G + node.H) < (min_node_.G + min_node_.H):
                min_node_ = node
        next_node_ = min_node_


        #Remove from frontier
        frontier_.remove(next_node_)

        #Check if node contains a goal state then return the corresponding solution
        if next_node_.current_state == goal_state:
            assign_g_with_uniform_cost_search(next_node_)
            print('\nGoal state found! Depth = ' + str(next_node_.G) + '\n')
            print_state(next_node_.current_state)
            final_message(num_nodes_expanded,frontier_size)
            return next_node_

        # Add node to the explored set
        explored_set_.append(next_node_.current_state)

        #Expand the chosen node,
        #adding the resulting nodes to the frontier
        #only if not in the frontier or explored set
        if check_if_node_state_in_frontier(next_node_,frontier_) == False or check_if_node_state_in_explored_set(next_node_,explored_set_) == False:
            #Expand Chosen node
            expand_node(next_node_)
            num_nodes_expanded+=1

            #Print Message
            print_expand_node_and_g_and_h(next_node_)

            # #Print State
            # print_state(next_node_.current_state)

            #_Add expanded nodes into frontier
            for child in next_node_.children:
                assign_g_with_uniform_cost_search(child)
                assign_h_with_misplaced_tile(child,goal_state)
                if check_if_node_state_in_frontier(child,frontier_) == False and check_if_node_state_in_explored_set(child,explored_set_) == False:
                    frontier_.append(child)

                if len(frontier_) > frontier_size:
                    frontier_size = len(frontier_)



def A_star_with_manhattan_distance_heuristic(initial_node,goal_state):

    #Will contain nodes
    frontier_ = []

    frontier_size = 0

    #Initialize Frontier with Initial Node
    frontier_.append(initial_node)

    #Initialize Explored set to be empty, th=='ll hold states
    explored_set_ = []

    num_nodes_expanded = 0
    while True:
        if len(frontier_) == 0:
            print("Loop Ending")
            return

        #Choose a leaf node and remove from frontier
        #Find lowest G value in frontier
        min_node_ = frontier_[0]
        for node in frontier_:
            if (node.G + node.H) < (min_node_.G + min_node_.H):
                min_node_ = node
        next_node_ = min_node_


        #Remove from frontier
        frontier_.remove(next_node_)

        #Check if node contains a goal state then return the corresponding solution
        if next_node_.current_state == goal_state:
            assign_g_with_uniform_cost_search(next_node_)
            print('\nGoal state found! Depth = ' + str(next_node_.G) + '\n')
            print_state(next_node_.current_state)
            final_message(num_nodes_expanded,frontier_size)
            return next_node_

        # Add node to the explored set
        explored_set_.append(next_node_.current_state)

        #Expand the chosen node,
        #adding the resulting nodes to the frontier
        #only if not in the frontier or explored set
        if check_if_node_state_in_frontier(next_node_,frontier_) == False or check_if_node_state_in_explored_set(next_node_,explored_set_) == False:
            #Expand Chosen node
            expand_node(next_node_)
            num_nodes_expanded+=1

            #Print Message
            print_expand_node_and_g_and_h(next_node_)

            # #Print State
            # print_state(next_node_.current_state)

            #_Add expanded nodes into frontier
            for child in next_node_.children:
                assign_g_with_uniform_cost_search(child)
                assign_h_with_manhattan_distance(child,goal_state)
                #Check if already in frontier and explored set
                if check_if_node_state_in_frontier(child,frontier_) == False and check_if_node_state_in_explored_set(child,explored_set_) == False:
                    frontier_.append(child)

                if len(frontier_) > frontier_size:
                    frontier_size = len(frontier_)
