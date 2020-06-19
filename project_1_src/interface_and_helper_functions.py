from tree_and_node_class import *
from operations import *
from misplaced_tile_h import *
from manhattan_d_h import *
from uniform_cost_search_g import *
from search_algorithms import *
import copy

def print_welcome_message():
    print("\nWelcome to Kevin Ferrer's (861272244) 8-puzzle solver.\
          \nType '1' to use a default puzzle, or '2' to enter your own puzzle.\n")


def print_trace(goal_node):
    backwards_list = []
    node_iterator = goal_node

    print('\n Trace Beginning \n')

    while node_iterator.name != 'root':
        backwards_list.append(node_iterator)
        node_iterator = node_iterator.parent

    backwards_list.append(node_iterator)

    for node in reversed(backwards_list):
        print('\n')
        print_state(node.current_state)
        print('\n')

    print('\n Trace Ending \n')



def print_expand_node_and_h(node):
    #Copy
    copy_node = copy.deepcopy(node)

    #Check if node is root
    if copy_node.name is "root":
        print("\nExpanding State")
        print_state(copy_node.current_state)
        print("\n")
        return

    print("The best state to expand with a h(n) = " + str(copy_node.H) + " is...")
    print_state(copy_node.current_state)
    print("Expanding this node...\n")

def print_expand_node_and_g(node):
    #Copy
    copy_node = copy.deepcopy(node)

    #Check if node is root
    if copy_node.name is "root":
        print("\nExpanding State")
        print_state(copy_node.current_state)
        print("\n")
        return

    print("The best state to expand with a g(n) = " + str(copy_node.G) + " is...")
    print_state(copy_node.current_state)
    print("Expanding this node...\n")

def print_expand_node_and_g_and_h(node):
    #Copy
    copy_node = copy.deepcopy(node)

    #Check if node is root
    if copy_node.name is "root":
        print("\nExpanding State")
        print_state(copy_node.current_state)
        print("\n")
        return

    print("The best state to expand with a g(n) = " + str(copy_node.G) + " and h(n) = " + str(copy_node.H) +" is...")
    print_state(copy_node.current_state)
    print("Expanding this node...\n")



def grab_first_row():
    print("\nEnter your puzzle, use a zero to represent the blank.")
    print ("Enter the first row, use enter between numbers ")
    row1 = []
    row1.append(raw_input())
    row1.append(raw_input())
    row1.append(raw_input())
    return row1

def grab_second_row():
    print("Enter the second row, use enter between numbers ")
    row2 = []
    row2.append(raw_input())
    row2.append(raw_input())
    row2.append(raw_input())
    return row2

def grab_third_row():
    print("Enter the third row, use enter between numbers ")
    row3 = []
    row3.append(raw_input())
    row3.append(raw_input())
    row3.append(raw_input())
    return row3

def build_custom_table():
    r1 = grab_first_row()
    r2 = grab_second_row()
    r3 = grab_third_row()
    custom_table = [r1,r2,r3]
    return custom_table

def build_default_table():
    s1_r1 = ['1','5','7']
    s1_r2 = ['4','b','6']
    s1_r3 = ['3','2','8']
    default_table = [s1_r1,s1_r2,s1_r3]
    return default_table

def build_trivial_table():
    r1 = ['1','2','3']
    r2 = ['4','5','6']
    r3 = ['7','b','8']
    trivial_table = [r1,r2,r3]
    return trivial_table


def build_easy_table():
    r1 = ['1','2','b']
    r2 = ['4','5','3']
    r3 = ['7','8','6']
    easy_table = [r1,r2,r3]
    return easy_table

def build_doable_table():
    r1 = ['b','1','2']
    r2 = ['4','5','3']
    r3 = ['7','8','6']
    doable_table = [r1,r2,r3]
    return doable_table

def build_oh_boy_table():
    r1 = ['8','7','1']
    r2 = ['6','b','2']
    r3 = ['5','4','3']
    table = [r1,r2,r3]
    return table

def build_goal_state_table():
    g1_r1 = ['1','2','3']
    g1_r2 = ['4','5','6']
    g1_r3 = ['7','8','b']
    goal_state = [g1_r1,g1_r2,g1_r3]
    return goal_state



def convert_grid(grid_state):
    row_count = 0
    col_count = 0
    for row in grid_state:
        if '0' in row:
            for val in row:
                if val == '0':
                    break
                else:col_count+=1
            break
        else:
            row_count+=1

    grid_state[row_count][col_count] = 'b'
    return grid_state


def check_if_grid_valid(grid_state):

    given_list = []
    expected_values = ['1','2','3','4','5','6','7','8','b']
    print("\n")
    for row in grid_state:
        for val in row:
            given_list.append(val)

    if sorted(given_list) == sorted(expected_values):
        return True
    else:
        print("Invalid Input for custom table")
        return False

def ask_for_default_or_custom():
    print_welcome_message()
    answer = int(input())
    return answer

def ask_for_algorithm():
    print("\nEnter your choice of algorithm")
    print("Uniform Cost Search")
    print("A* with the Misplaced Tile Heuristic.")
    print("A* with the Manhattan distance heuristic.")

    answer = input("\n")
    return str(answer)


#FIXME
def final_message(num1,num2):
    print('\nTo solve this problem the search algorithm expanded a total of ' + str(num1) + ' nodes.')
    print('The maximum number of nodes in the queue at any one time was ' + str(num2) + '.\n')
