from tree_and_node_class import *
import copy


def expand_node(given_node):
    #This function takes a node as a paramter
    #Take a node and generate its children
    #given_node is being passed by reference
    list_of_children_nodes = []

    grid_state_backup = copy.deepcopy(given_node.current_state)
    grid_state_temp = copy.deepcopy(given_node.current_state)

    if move_b_up(grid_state_temp) is not False:
        grid_state_temp=copy.deepcopy(grid_state_backup)
        list_of_children_nodes.append(AnyNode(parent=given_node,current_state=move_b_up(grid_state_temp),H=None,G=None,F=None,name=None))
        grid_state_temp=copy.deepcopy(grid_state_backup)

    grid_state_temp=copy.deepcopy(grid_state_backup)
    if move_b_down(grid_state_temp) is not False:
        grid_state_temp=copy.deepcopy(grid_state_backup)
        list_of_children_nodes.append(AnyNode(parent=given_node,current_state=move_b_down(grid_state_temp),H=None,G=None,F=None,name=None))
        grid_state_temp=copy.deepcopy(grid_state_backup)

    grid_state_temp=copy.deepcopy(grid_state_backup)
    if move_b_left(grid_state_temp) is not False:
        grid_state_temp=copy.deepcopy(grid_state_backup)
        list_of_children_nodes.append(AnyNode(parent=given_node,current_state=move_b_left(grid_state_temp),H=None,G=None,F=None,name=None))
        grid_state_temp=copy.deepcopy(grid_state_backup)

    grid_state_temp=copy.deepcopy(grid_state_backup)
    if move_b_right(grid_state_temp) is not False:
        grid_state_temp=copy.deepcopy(grid_state_backup)
        list_of_children_nodes.append(AnyNode(parent=given_node,current_state=move_b_right(grid_state_temp),H=None,G=None,F=None,name=None))
        grid_state_temp=copy.deepcopy(grid_state_backup)


    return list_of_children_nodes


def print_state(state):
    for row in state:
        print(row)

def move_b_up(grid_state):

    #Check if in row 1
    #Upper level will prevent this branch from occurring
    if 'b' in grid_state[0]:
        # print("Blank was found in row 1")
        # print("Illegal action")
        return False

    #Check if in row 2
    elif 'b' in grid_state[1]:
        #print("Blank was found in row 2")

        #Grab column of b
        count = 0
        for val in grid_state[1]:
            if val is 'b':
                break
            else:
                count+=1

        # print("b found in column index: " + str(count))
        #
        # print("Original State: ")
        # print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[0][int(count)]

        #replace target_spot
        grid_state[0][int(count)] = 'b'

        #replace old 'b'
        grid_state[1][int(count)] = target_spot_value

        # print("New State: ")
        # print_state(grid_state)
        return grid_state


    #Check if in row 3
    elif 'b' in grid_state[2]:
        # #print("Blank was found in row 3")

        #Grab column of b
        count = 0
        for val in grid_state[2]:
            if val is 'b':
                break
            else:
                count+=1

        # #print("b found in column index: " + str(count))
        #
        # #print("Original State: ")
        # #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[1][int(count)]

        #replace target_spot
        grid_state[1][int(count)] = 'b'

        #replace old 'b'
        grid_state[2][int(count)] = target_spot_value

        # #print("New State: ")
        # #print_state(grid_state)
        return grid_state

def move_b_left(grid_state):

    #Check if b in left column
    #Upper level will prevent this from happening
    if grid_state[0][0] is 'b' or grid_state[1][0] is 'b' or grid_state[2][0] is 'b':
        # print("b found in left column")
        # print("Illegal action")
        return False

    #Check if b in middle column:
    elif grid_state[0][1] is 'b' or grid_state[1][1] is 'b' or grid_state[2][1] is 'b':
        # #print("b is in the middle column")

        row_index = None
        #grab row value
        if grid_state[0][1] is 'b':
            row_index = 0
            # #print("row_index: " + str(row_index))
        elif grid_state[1][1] is 'b':
            row_index = 1
            # #print("row_index: " + str(row_index))
        elif grid_state[2][1] is 'b':
            row_index = 2
            # #print("row_index: " + str(row_index))

        # #print("Original State: ")
        # #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[int(row_index)][0]

        #replace target spot
        grid_state[int(row_index)][0] = 'b'

        #replace old 'b'
        grid_state[int(row_index)][1] = target_spot_value

        #print("New State: ")
        #print_state(grid_state)

        return grid_state


    #Check if b in the right column:
    elif grid_state[0][2] is 'b' or grid_state[1][2] is 'b' or grid_state[2][2] is 'b':
        #print("b is in the right column")

        row_index = 0
        #grab row value
        if grid_state[0][2] is 'b':
            row_index = 0
            # #print("row_index: " + str(row_index))
        elif grid_state[1][2] is 'b':
            row_index = 1
            # #print("row_index: " + str(row_index))
        elif grid_state[2][2] is 'b':
            row_index = 2
            # #print("row_index: " + str(row_index))

        # #print("Orginal State: ")
        # #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[int(row_index)][1]

        #replace target spot
        grid_state[int(row_index)][1] = 'b'

        #replace old 'b'
        grid_state[int(row_index)][2] = target_spot_value

        # #print("New State: ")
        # #print_state(grid_state)
        return grid_state

def move_b_down(grid_state):

    #Level above will prevent this from happening
    #Check if B in bottom row
    if 'b' in grid_state[2]:
        # print("b in bottom row")
        # print("Illegal action")
        return False
    #Check if B in middle row
    elif 'b' in grid_state[1]:

        #Grab column of b
        count = 0
        for val in grid_state[1]:
            if val is 'b':
                break
            else:
                count+=1

        # #print("b found in column index: " + str(count))

        #print("Original State: ")
        #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[2][int(count)]

        #replace target_spot
        grid_state[2][int(count)] = 'b'

        #replace old 'b'
        grid_state[1][int(count)] = target_spot_value

        #print("New State: ")
        #print_state(grid_state)

        return grid_state

    #Check if B in top row
    elif 'b' in grid_state[0]:

        #Grab column of b
        count = 0
        for val in grid_state[0]:
            if val is 'b':
                break
            else:
                count+=1

        # #print("b found in column index: " + str(count))

        #print("Original State: ")
        #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[1][int(count)]

        #replace target_spot
        grid_state[1][int(count)] = 'b'

        #replace old 'b'
        grid_state[0][int(count)] = target_spot_value

        #print("New State: ")
        #print_state(grid_state)

        return grid_state



def move_b_right(grid_state):

    #Check if b in right column
    #Upper level will prevent this from happening
    if grid_state[0][2] is 'b' or grid_state[1][2] is 'b' or grid_state[2][2] is 'b':
        # print("b found in right column")
        # print("Illegal action")
        return False

    #Check if b in middle column:
    elif grid_state[0][1] is 'b' or grid_state[1][1] is 'b' or grid_state[2][1] is 'b':
        # #print("b is in the middle column")

        row_index = None
        #grab row value
        if grid_state[0][1] is 'b':
            row_index = 0
            # #print("row_index: " + str(row_index))
        elif grid_state[1][1] is 'b':
            row_index = 1
            # #print("row_index: " + str(row_index))
        elif grid_state[2][1] is 'b':
            row_index = 2
            # #print("row_index: " + str(row_index))

        #print("Original State: ")
        #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[int(row_index)][2]

        #replace target spot
        grid_state[int(row_index)][2] = 'b'

        #replace old 'b'
        grid_state[int(row_index)][1] = target_spot_value

        #print("New State: ")
        #print_state(grid_state)

        return grid_state

    #Check if b in left column:
    elif grid_state[0][0] is 'b' or grid_state[1][0] is 'b' or grid_state[2][0] is 'b':
        # #print("b is in the middle column")

        row_index = None
        #grab row value
        if grid_state[0][0] is 'b':
            row_index = 0
            # #print("row_index: " + str(row_index))
        elif grid_state[1][0] is 'b':
            row_index = 1
            # #print("row_index: " + str(row_index))
        elif grid_state[2][0] is 'b':
            row_index = 2
            # #print("row_index: " + str(row_index))

        #print("Original State: ")
        #print_state(grid_state)

        #switch the values
        #grab target value
        target_spot_value = grid_state[int(row_index)][1]

        #replace target spot
        grid_state[int(row_index)][1] = 'b'

        #replace old 'b'
        grid_state[int(row_index)][0] = target_spot_value

        #print("New State: ")
        #print_state(grid_state)

        return grid_state
