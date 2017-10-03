tree = {
    1: ['max',False,[2,3]],
    2: ['min',False,[4,5]],
    3: ['min',False,[6,7]],
    4: ['max',False,[8,9]],
    5: ['max',False,[10,11]],
    6: ['max',False,[12,13]],
    7: ['max',False,[14,15]],
    8: ['min',True,4],
    9: ['min', True, 2],
    10: ['min', True, 5],
    11: ['min', True, 7],
    12: ['min', True, 6],
    13: ['min', True, 1],
    14: ['min', True, 3],
    15: ['min', True, 8],

}
tree_values = {}
tree_2 = {
    1: ['max',False,[2,3,4]],
    2: ['min',False,[5,6,7]],
    3: ['min',False,[8,9,10]],
    4: ['min',False,[11,12,13]],
    5: ['max',True,3],
    6: ['max', True, 12],
    7: ['max', True, 8],
    8: ['max', True, 2],
    9: ['max', True, 4],
    10: ['max', True, 6],
    11: ['max', True, 14],
    12: ['max', True, 5],
    13: ['max', True, 2],

}
tree_3 = {
    1: ['max',False,[2,3]],
    2: ['min',False,[4,5]],
    3: ['min',False,[6,7]],
    4: ['max',False,[8,9]],
    5: ['max',False,[10,11]],
    6: ['max',False,[12,13]],
    7: ['max',False,[14,15]],
    8: ['min',True,10],
    9: ['min', True, 6],
    10: ['min', True, 100],
    11: ['min', True, 8],
    12: ['min', True, 1],
    13: ['min', True, 2],
    14: ['min', True, 20],
    15: ['min', True, 4],

}


def minimax(graph,node,values):
    maxi = False
    if graph.get(node)[0] == 'max':
        maxi = True
    else:
        maxi = False
    if maxi:
        v = -1000
        successors = graph.get(node)[2]
        for successor in successors:
            terminal = graph.get(successor)[1]
            if terminal:
                value = graph.get(successor)[2]
            else:
                value = minimax(graph,successor,values)
            if value > v:
                v = value
        values[node] = v
        return v
    elif not maxi:
        v = 1000
        successors = graph.get(node)[2]
        for successor in successors:
            terminal = graph.get(successor)[1]
            if terminal:
                value = graph.get(successor)[2]
            else:
                value = minimax(graph, successor,values)
            if value < v:
                v = value
        values[node] = v
        return  v


def alpha_beta(graph,node,values,a,b,explored):
    maxi = False
    if graph.get(node)[0] == 'max':
        maxi = True
    else:
        maxi = False
    if maxi:
        v = -1000
        successors = graph.get(node)[2]
        for successor in successors:
            explored[successor] = True
            terminal = graph.get(successor)[1]
            if terminal:
                value = graph.get(successor)[2]
            else:
                value = alpha_beta(graph,successor,values,a,b,explored)
            if value > v:
                v = value
            if v >= b:
                values[node] = v
                return v
            if v > a:
                a = v
        values[node] = v
        return v
    elif not maxi:
        v = 1000
        successors = graph.get(node)[2]
        for successor in successors:
            explored[successor] = True
            terminal = graph.get(successor)[1]
            if terminal:
                value = graph.get(successor)[2]
            else:
                value = alpha_beta(graph, successor, values, a, b, explored)
            if value < v:
                v = value
            if v <= a:
                values[node] = v
                return v
            if v < b:
                b = v
        values[node] = v
        return v

    def minimax(graph, node, values):
        maxi = False
        if graph.get(node)[0] == 'max':
            maxi = True
        else:
            maxi = False
        if maxi:
            v = -1000
            successors = graph.get(node)[2]
            for successor in successors:
                terminal = graph.get(successor)[1]
                if terminal:
                    value = graph.get(successor)[2]
                else:
                    value = minimax(graph, successor, values)
                if value > v:
                    v = value
            values[node] = v
            return v
        elif not maxi:
            v = 1000
            successors = graph.get(node)[2]
            for successor in successors:
                terminal = graph.get(successor)[1]
                if terminal:
                    value = graph.get(successor)[2]
                else:
                    value = minimax(graph, successor, values)
                if value < v:
                    v = value
            values[node] = v
            return v


def expectimax(graph,node,values):
    maxi = False
    if graph.get(node)[0] == 'max':
        maxi = True
    else:
        maxi = False
    if maxi:
        v = -1000
        successors = graph.get(node)[2]
        for successor in successors:
            terminal = graph.get(successor)[1]
            if terminal:
                value = graph.get(successor)[2]
            else:
                value = expectimax(graph,successor,values)
            if value > v:
                v = value
        values[node] = v
        return v
    elif not maxi:
        v = 0
        successors = graph.get(node)[2]
        probability = 1.0 / len(successors)
        for successor in successors:
            terminal = graph.get(successor)[1]
            if terminal:
                value = graph.get(successor)[2]
            else:
                value = expectimax(graph, successor,values)
            v += (value*probability)
        values[node] = v
        return  v
explored_nodes={}
expectimax(tree,1,tree_values)
print tree_values
print
