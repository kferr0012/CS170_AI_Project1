from tree_and_node_class import *
from operations import *
import copy

def find_location_row(target_value,given_state):
    row_location = None
    count = 0

    for row in given_state:
        if target_value in row:
            return count
        else:
            count+=1

def find_location_col(target_value,given_state):
    col_location = None
    count = 0

    for row in given_state:
        if target_value in row:
            for val in row:
                if val is target_value:
                    return count
                else:
                    count+=1

def location_checker(target_value,given_state):
    row_location = find_location_row(target_value,given_state)
    col_location = find_location_col(target_value,given_state)
    print("Target: " + str(target_value) + " found in row index: " + str(row_location) + " and column index: " + str(col_location))



def assign_h_with_manhattan_distance(given_node,goal_state):

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

    #Iterate through every value and compare
    for row in range(num_rows):
        for col in range(num_col):
            target_value = node_state[row][col]

            original_state_row = find_location_row(target_value,node_state)
            original_state_col = find_location_col(target_value,node_state)

            goal_state_row = find_location_row(target_value,ideal_state)
            goal_state_col = find_location_col(target_value,ideal_state)

            h_value += abs(original_state_row-goal_state_row) + abs(original_state_col-goal_state_col)

    given_node.H=h_value
