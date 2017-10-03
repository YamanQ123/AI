grid_1_diagonal = [[' ','o','x'],[' ','x','o'],['x',' ',' ']]
grid_1_row = [[' ','o',' '],['x','o','x'],[' ','o','x']]
grid_1_column = [[' ',' ','x'],['o',' ','x'],[' ',' ','x']]
grid_0_full = [['x','o','x'],['x','o','o'],['o','x','x']]


def output(grid):
    for row in grid:
        print row


def generate_successors(grid, maxi):
    space_co = []
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j]== ' ':
                space_co.append((i,j))
    successors = []
    if maxi:
        for co in space_co:
            successor = [[],[],[]]
            for i in range(0,3):
                for j in range(0,3):
                    successor[i].append(grid[i][j])
            successor[co[0]][co[1]] = 'x'
            successors.append(successor)
        return successors,space_co
    else:
        for co in space_co:
            successor = [[], [], []]
            for i in range(0, 3):
                for j in range(0, 3):
                    successor[i].append(grid[i][j])
            successor[co[0]][co[1]] = 'o'
            successors.append(successor)
        return successors,space_co



def evaluation_function(grid):
    terminal_state = False
    utility = None
    if grid[0][2] == grid[1][1] == grid[2][0] =='x'  or grid[0][0] == grid[1][1] == grid[2][2] =='x' or grid[0][0] == grid[0][1] == grid[0][2] =='x' or grid[1][0] == grid[1][1] == grid[1][2] =='x' or grid[2][0] == grid[2][1] == grid[2][2] =='x'\
        or grid[0][0] == grid[1][0] == grid[2][0] =='x' or grid[0][1] == grid[1][1] == grid[2][1] =='x' or grid[0][2] == grid[1][2] == grid[2][2] =='x' :
        utility = 1
        terminal_state = True
        return terminal_state, utility
    elif grid[0][2] == grid[1][1] == grid[2][0] == 'o' or grid[0][0] == grid[1][1] == grid[2][2] == 'o' or grid[0][0] ==  grid[0][1] == grid[0][2] == 'o' or grid[1][0] == grid[1][1] == grid[1][2] == 'o' or grid[2][0] == grid[2][
        1] == grid[2][2] == 'o'  or grid[0][0] == grid[1][0] == grid[2][0] == 'o' or grid[0][1] == grid[1][1] == grid[2][1] == 'o' or  grid[0][2] == grid[1][2] == grid[2][2] == 'o':
        utility = -1
        terminal_state = True
        return terminal_state, utility

    else:
        counter = 0
        for row in grid:
            for element in row:
                if element == 'x' or element == 'o':
                    counter += 1
        if counter == 9:
            utility = 0
            terminal_state = True
        return terminal_state, utility

    return terminal_state,utility


def minimax(grid,maxi):
    #returns an action (position)
    if maxi:
        print'maximizing'
        v = -10
        value = v
        action = ()
        best_action = ()
        successors_state = generate_successors(grid,maxi)
        successors = successors_state[0]
        space_co = successors_state[1]
        for i in range(0,len(successors)):
            evaluate = evaluation_function(successors[i])
            terminal_state = evaluate[0]
            utility = evaluate[1]
            if terminal_state:
                value = utility
                action = space_co[i]
            else:
                value_state = minimax(successors[i],not maxi)
                value = value_state[0]
                action = space_co[i]
            print 'successor[i]: '
            output(successors[i])
            print'action: ', action, ' value: ', value
            if value > v:
                v = value
                best_action = action
        return v,best_action
    else:
        print 'minimizing'
        v = 10
        value = v
        action = ()
        best_action = ()
        successors_state = generate_successors(grid,maxi)
        successors = successors_state[0]
        space_co = successors_state[1]
        for i in range(0, len(successors)):
            evaluate = evaluation_function(successors[i])
            terminal_state = evaluate[0]
            utility = evaluate[1]
            if terminal_state:
                value = utility
                action = space_co[i]
            else:
                value_state = minimax(successors[i],not maxi)
                value = value_state[0]
                action = space_co[i]
            print 'successor[i]: '
            output(successors[i])
            print'action: ',action,' value: ',value
            if value < v:
                v = value
                best_action = action
        return v, best_action


# print evaluation_function(grid_0_full)
# output(grid_1_diagonal)
# successors =  generate_successors(grid_1_diagonal , maxi=False)
# print
# for successor in successors:
#     output(successor)
#     print
test_grid_1=[
    ['x','o','x'],
    ['o','x','o'],
    ['o','x',' ']
]
test_grid_2=[
    ['x','o','x'],
    ['x','o','x'],
    ['o',' ',' ']

]
test_grid_3=[
    ['x','o','x'],
    ['x','o',' '],
    [' ',' ','o']

]
test_grid_4=[
    ['x','x','o'],
    ['o','o',' '],
    ['x',' ',' ']

]

print
print minimax(test_grid_4,maxi=True)

#print generate_successors(test_grid_1,maxi=True)