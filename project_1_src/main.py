from tree_and_node_class import *
from operations import *
from misplaced_tile_h import *
from manhattan_d_h import *
from uniform_cost_search_g import *
from search_algorithms import *
from interface_and_helper_functions import *
from anytree import LevelOrderIter
import time



#Python2

origin_table = None

#Initialize Goal State
goal_state = build_goal_state_table()

#   [['1', '2', '3'], ['4', '5', '6'], ['7', '8', 'b']]

#Load Table
if ask_for_default_or_custom() is 1:
    origin_table = build_doable_table()
else:
    origin_table = convert_grid(build_custom_table())

#Check if the table is valid
if(check_if_grid_valid(origin_table)):
    print("\nValid Table Loaded\n")
    print_state(origin_table)
else:
    print("Program Ending")
    exit()

#Check if input the goal state
if origin_table is goal_state:
    print("You entered the completed puzzle.")
    exit()

start_time = time.time()

#Initialize Root
root_node = build_tree(origin_table)

#Decide on which algorithm to use
algorithm_selection = ask_for_algorithm()

if algorithm_selection is '1':
    goal_node = uniform_cost_search_algorithm3(root_node,goal_state)
elif algorithm_selection is '2':
    goal_node = A_star_with_misplaced_tile_heuristic2(root_node,goal_state)
elif algorithm_selection is '3':
    goal_node = A_star_with_manhattan_distance_heuristic(root_node,goal_state)
else:
    print("Incorrect Value Entered for Algorithm Choice")
    print("Program Ending")
    exit()

time = time.time() - start_time

print('Time: ' + str(time) + ' seconds\n')

print('Trace node path?')
answer = raw_input("Enter [yes] or [no]\n")

if answer == 'yes':
    print_trace(goal_node)
