australia_map = {"WA": ['NT','SA'],
                 'SA': ['WA','NT','Q','NSW','V'],
                 'NT': ['WA','SA','Q'],
                 'Q': ['NT','SA','NSW'],
                 'V': ['NSW','SA'],
                 'NSW':['Q','SA','V']
                }
domain = ['r', 'g', 'b']

map_available_colors = {
                        "WA": ['r','g','b'],
                        'SA': ['r','g','b'],
                        'NT': ['r','g','b'],
                        'Q': ['r','g','b'],
                        'V': ['r','g','b'],
                        'NSW':['r','g','b']

                        }
array_available_colors = {
                        1: ['r','g','b'],
                        2: ['r','g','b'],
                        3: ['r','g','b'],
                        4: ['r','g','b'],
                        5: ['r','g','b'],
                        6: ['r','g','b'],
                        7: ['r','g','b'],
                        8: ['r','g','b'],
                        9: ['r','g','b']
}
colors_array = {
                1 : [2,5,6],
                2 : [3,4,5,1],
                3: [4,2],
                4:[5,9,2,3],
                5: [6,9,8,1,2,4],
                6:[7,8,5,1],
                7:[8,6],
                8: [9,5,6,7],
                9: [8,5,4]
                }

domain = ['r', 'g', 'b']
if australia_map.get('RE') is None:
    print 'hello'

print australia_map
solution_array = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}
tried_colors_array = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}
solution = {
    "WA": [],
    'SA': [],
    'NT': [],
    'Q': [],
    'V': [],
    'NSW':[]
}
tried_colors = {
    "WA": [],
    'SA': [],
    'NT': [],
    'Q': [],
    'V': [],
    'NSW':[]
}

n = 11
i = 0
dfs = []


def back_track(node,graph,neighbours_tried_colors,neighbours_assigned_colors,dfs ):
    # print 'round: ',i
    # if i == n:
    #     return True
    # i += 1

    taken_colors = []
    #visited = False
    #done = True
    #print graph.get(node)
    #satisfiying the condition that the neighbours must have different colors
    #taken colors contains the NOT not allowed colors
    color = None
    for neighbour in graph.get(node):
        print 'neighbour: ',neighbour
        if len(neighbours_assigned_colors.get(neighbour)) != 0:
            color = neighbours_assigned_colors.get(neighbour)[0]
        print 'color ',color
        if color not in taken_colors and color is not None:
            taken_colors.append(color)
    #adding to the taken colors the already tried colors for this node from previos back tracked
    if neighbours_tried_colors.get(node) is not None:
        for color in neighbours_tried_colors.get(node):
            if color not in taken_colors:
                taken_colors.append(color)
    print 'taken_colors: ', taken_colors

    #assigning the first possible color from the domain to the current node and add this color tho tried colors and stack the node to the dfs
    # for color in domain:
    #     if color in taken_colors:

    if len(taken_colors) != 3:
        for color in domain:
            if color not in taken_colors:
                print 'type of assigned colors',type(neighbours_assigned_colors)
                neighbours_assigned_colors[node] = color
                neighbours_tried_colors[node].append(color)
                visited = True
                dfs.append(node)
                break
        print 'neighbours_assigned_colors:',neighbours_assigned_colors
        print  'neighbours_tried_colors:',neighbours_tried_colors
        print 'dfs: ',dfs
    #setting the next node to the fist not assigned yet neighbour
        all_neighbours_assigned = True
        for neighbour in graph.get(node):
            print 'here: ',neighbour

            if neighbours_assigned_colors.get(neighbour) == [] :
                node = neighbour
                all_neighbours_assigned = False
                #done = False
                break
        print 'node: ', node
        print 'all neighbous assigned: ',all_neighbours_assigned
        if all_neighbours_assigned:
            return True
    #
    #if the len(taken_colors) == 3 i.e no allowed colors from the domain we pop the previous node
    #to be the next node and changes it's color if possible
    else:
    #setting treid colors of this node = [] after leaving it to allow it to take all possible states
         print 'backtracking: '
         neighbours_tried_colors[node] = []
         node = dfs.pop()
         print 'node: ',node
         print 'neighbours assigned colors: ',neighbours_assigned_colors
    #re set the assigned colors to none
         neighbours_assigned_colors[node] = []
         print 'neighbours assigned colors: ', neighbours_assigned_colors
         print 'neghbours tried colors: ',neighbours_tried_colors
    # if done :
    #     return done

    print
    back_track(node,graph,neighbours_tried_colors,neighbours_assigned_colors,dfs)


#print back_track(1,colors_array,tried_colors_array,solution_array,dfs)


def backtracking_forward_checking(node,graph,available_colors,neighbours_assigned_colors,dfs):
        # print 'round: ', i
        # if i == n:
        #     return True
        # i += 1
        print 'node: ', node
        for color in available_colors[node]:
            violates = False
            print 'current node neighbours: ',graph.get(node)
            for neighbour in graph.get(node):
                if len(neighbours_assigned_colors[neighbour]) == 0 and color in available_colors[neighbour]:
                    print 'color: ',color
                    print 'available_colors_',neighbour,": ",available_colors[neighbour]
                    available_colors[neighbour].remove(color)
                    if len(available_colors[neighbour]) == 0:
                        violates = True

            if violates:
                for neighbour in graph.get(node):
                    if len(neighbours_assigned_colors[neighbour]) == 0:
                        available_colors[neighbour].append(color)

            if not violates:
                break
            print 'violates: ', violates
            print 'available colors: ', available_colors
            print 'assigned colors: ', neighbours_assigned_colors
            print 'dfs: ', dfs

        if not violates:
            dfs.append(node)
            neighbours_assigned_colors[node].append(color)
            available_colors[node].remove(color)
            all_neighbours_assigned = True
            for neighbour in graph.get(node):
                if neighbours_assigned_colors.get(neighbour) == []:
                    node = neighbour
                    all_neighbours_assigned = False
                    break
            print 'finished: ',all_neighbours_assigned
            print'node: ', node
            print 'violates: ', violates
            print 'available colors: ', available_colors
            print 'assigned colors: ', neighbours_assigned_colors
            print 'dfs: ', dfs
            if all_neighbours_assigned:
                return True


        elif violates:
            node = dfs.pop()
            color = neighbours_assigned_colors[node].pop()
            for neighbour in graph.get(node):
                if len(neighbours_assigned_colors[node]) == 0:
                    available_colors[neighbour].append(color)
            print 'available colors: ',available_colors
            print 'assigned colors: ', neighbours_assigned_colors
            print 'dfs: ', dfs

        backtracking_forward_checking(node, graph, available_colors, neighbours_assigned_colors, dfs)


#print backtracking_forward_checking(1,colors_array,array_available_colors,solution_array,dfs)

map_available_colors1 = {
    "WA": ['r'],
    'SA': ['r', 'g', 'b'],
    'NT': ['r', 'g', 'b'],
    'Q': ['r', 'g', 'b'],
    'V': ['r', 'g', 'b'],
    'NSW': ['r', 'g', 'b']
                        }
from Queue import Queue


def ac_3(node,graph,available_colors,neighbours_assigned_colors):
    test_available_colors = {}
    need_to_backtrack = False
    for color in available_colors[node]:
        test_available_colors = {}
        for k, v in available_colors.items():
            test_available_colors[k] = v
        test_available_colors[node] = color
        arc_already_queued = {}
        queue = Queue()
        for neighbour in graph.get(node):
            arc = (neighbour, node)
            queue.enque(arc)
            arc_already_queued[arc] = True
        print arc_already_queued
        while not queue.is_empty():
            arc = queue.deque()
            arc_already_queued[arc] = False
            state = remove_inconsistent_values(arc, test_available_colors)
            removed = state[0]
            need_to_backtrack = state[1]
            if removed:
                for neighbour in graph.get(arc[0]):
                    adj_arc = (neighbour, arc[0])
                    if not arc_already_queued.get(adj_arc):
                        queue.enque(adj_arc)
                        arc_already_queued[adj_arc] = True

            if need_to_backtrack:
                break
        print 'need to backtrack: ', need_to_backtrack
        print 'test available colors: ', test_available_colors
        if not need_to_backtrack:
            break

    available_colors = {}
    for k,v in test_available_colors.items():
        available_colors[k] = v
    neighbours_assigned_colors[node] = True
    for neighbour in graph.get(node):
        if not neighbours_assigned_colors.get(neighbour):
            node = neighbour
            break
    counter = 0
    for k,v in test_available_colors.items():
        if len(test_available_colors.get(k)) == 1:
            counter += 1
    print 'next node ',node
    print 'available colors: ',available_colors
    if counter == len(available_colors):
        return True
    print 'counter: ',counter
    ac_3(node,graph,available_colors,neighbours_assigned_colors)


def remove_inconsistent_values(arc, available_colors):
    head = arc[1]
    tail = arc[0]
    removed = False
    need_to_backtrack = False
    if len(available_colors[head]) == 1:
        for color in available_colors[tail]:
            if color == available_colors[head][0]:
                available_colors[tail].remove(color)
                removed = True
    if len(available_colors[tail]) == 0:
        need_to_backtrack = True
    return removed,need_to_backtrack


#b = remove_inconsistent_values(('SA' , 'WA'), map_available_colors1)

ac_3(1,colors_array, array_available_colors,neighbours_assigned_colors={})
#print map_available_colors