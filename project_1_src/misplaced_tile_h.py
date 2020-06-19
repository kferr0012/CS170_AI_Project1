from tree_and_node_class import *
from operations import *
import copy


def assign_h_with_misplaced_tile(given_node,goal_state):

    #return value
    h_value=0
    do_bs_match=False

    #Grab current State
    node_state = copy.deepcopy(given_node.current_state)
    ideal_state = copy.deepcopy(goal_state)

    #Find out number of rows
    num_rows = len(node_state)

    #Find out number of columns
    num_col = len(node_state[0])

    #Iterate through both states and count the number of mismatches
    #1) Iterate by row
    for row in range(0,num_rows):
        #2) Iterate by column
        for col in range(0,num_col):
            if node_state[row][col] is ideal_state[row][col] and node_state[row][col] is 'b':
                do_bs_match=True
            if node_state[row][col] is not ideal_state[row][col]:
                h_value+=1

    if h_value is 0:
        # print("Perfect Match!")
        #set the node's h value
        given_node.H=h_value
        return None

    elif do_bs_match:
        # print("b in same location")
        # print("h value: " + str(h_value))
        #set the node's h value
        given_node.H=h_value
        return None

    else:
        # print("b in different location")
        #We don't count the blank tile so we minus 1
        h_value-=1
        # print("h value: " + str(h_value))
        given_node.H=h_value
        #set the node's h value

        return None
