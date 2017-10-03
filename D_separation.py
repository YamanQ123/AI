triple_causal_chain = ({'a': 'b', 'b': 'c'}, ['a', 'b', 'c'], {'a': False, 'b': True, 'c': False})
triple_common_cause = ({'a': ['b', 'c']}, ['a', 'b', 'c'], {'a': True, 'b': False, 'c': False})
triple_v_structure = ({'a': 'b', 'c': 'b'}, ['a', 'b', 'c'], {'a': False, 'b': True, 'c': False})
print len(triple_common_cause[0])
causal_chain = 'CAUSAL_CHAIN'
common_cause = 'COMMON_CAUSE'
v_structure = 'V_STRUCTURE'

graph_1 = {'R': ['T'],
            'B': ['T'],
            'T': ['T1']}
graph_2 = { 'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']}
graph_5 = {'L': ['R'],
           'R': ['D', 'T'],
           'B': ['T'],
           'T': ['T1']}
graph_5_givens = {'L': False,
                  'R': True,
                  'D': False,
                  'B': False,
                  'T': False,
                  'T1': False}

graph_v_structure = {'A':['B'],
                     'C':['B']}

graph_v_structure_givens={'A': False,
                          'B': True,
                          'C': False}
graph_common_cause = {'B':['A','C']}
graph_common_cause_givens = {'A': False,
                          'B': True,
                          'C': True}
graph_3 = {'U': ['W'],
           'W': ['Y'],
           'V': ['W','X','T'],
           'X': ['Y'],
           'T': ['Z']}
graph_3_givens ={   'U': False,
                    'W': False,
                    'Y': True,
                    'X': False,
                    'V': False,
                    'T': False,
                    'Z': False,
                 }
# def triple_type(triple):
#     triple_connections = triple[0]
#     triple_components = triple[1]
#     triple_givens = triple[2]
#     if len(triple_connections) == 1:
#         return common_cause
#     values = []
#     for value in triple_connections.values():
#         values.append(value)
#     if values[0] == values[1]:
#         return v_structure
#     else:
#         return causal_chain
#
#
# def is_active(triple):
#     triple_connections = triple[0]
#     triple_components = triple[1]
#     triple_givens = triple[2]
#     active = False
#     activation_element = 0
#     if triple_type(triple) == common_cause:
#         for k in triple_connections.keys():
#             activation_element = k
#         active = not triple_givens.get(activation_element)
#         return active
#     elif triple_type(triple) == v_structure:
#         key = list(triple_connections)[0]
#         activation_element = triple_connections.get(key)
#         active = triple_givens.get(activation_element)
#         return active
#     else:
#         activation_element = triple_components[1]
#         active = not triple_givens.get(activation_element)
#         return active


def directed_to_undirected(graph):
    import copy
    graph_copy = copy.deepcopy(graph)

    # for k,v in graph.items():
    #     graph_copy[k] = v
    for k in graph_copy.keys():
        for adjacent in graph_copy.get(k):
            if graph_copy.get(adjacent) is None:
                graph_copy[adjacent] = [k]
            if k not in graph_copy.get(adjacent):
                graph_copy[adjacent].append(k)
    return graph_copy


def find_all_paths(graph, start, end):
    undirected_graph = directed_to_undirected(graph)
    solution = list()
    visited = list()
    visited.append(start)
    path = list()
    path.append(start)
    recursive_find_all_paths(undirected_graph, start, end, path,visited, solution)
    return solution


def recursive_find_all_paths(graph,start,end,path,  visited, solution):
    for adj in graph.get(start):
        if adj not in visited:
            visited.append(adj)
            path.append(adj)
            start = adj
            if adj == end:
                sol = list()
                for x in path:
                    sol.append(x)
                solution.append(sol)
            else:
                recursive_find_all_paths(graph, start, end, path, visited,solution)
            path.pop()
            visited.pop()

# return true if path is active and false if path is not active
def is_path_active(path, graph, graph_givens):
    triples = list()
    triple = tuple()
    for i in range(0, len(path)-2):
        first = path[i]
        second = path[i+1]
        third = path[i+2]
        triple_components = [first,second,third]
        triple_givens = dict()
        for component in triple_components:
            triple_givens[component] = graph_givens.get(component)
        # common cause
        triple_connections = dict()
        triple_type = None
        active = None
        if graph.get(second) is not None and first in graph.get(second) and third in graph.get(second):
            triple_connections[second] = [first, third]
            triple_type = common_cause
            active = not triple_givens.get(second)
        # v_structure (common_effect)
        elif graph.get(third) is not None and graph.get(first) is not None and  second in graph.get(first) and second in graph.get(third):
            triple_connections[first] = second
            triple_connections[third] = second
            triple_type = v_structure
            active = triple_givens.get(second)
        # causal_chain
        elif graph.get(first) is not None and  second in graph.get(first):
            triple_connections[first] = second
            triple_connections[second] = third
            triple_type = causal_chain
            active = not triple_givens.get(second)
        else:
            triple_connections[third] = second
            triple_connections[second] = first
            triple_type = causal_chain
            active = not triple_givens.get(second)
        triple = (triple_connections, triple_components, triple_givens,triple_type,  active)
    #     triples.append(triple)
    # return triples
        if not active:
            return False
    return True


# return true if start and end is guaranteed to be  independent and false if dependent
def D_separation(graph,graph_givens, start, end):
    paths = find_all_paths(graph, start,end)
    for path in paths:
        if is_path_active(path,graph,graph_givens):
            return False
    return True




# graph_5_directed = graph_5
# graph_5_undirected = directed_to_undirected(graph_5)
# paths = find_all_paths(graph_5, 'L', 'T1')
# print paths
# path = paths[0]
# print path
# break_to_triples(path, graph_5, graph_5_givens)
# print graph_5
# paths = find_all_paths(graph_v_structure,'A','C')
# print paths
# break_to_triples(paths[0], graph_v_structure,graph_v_structure_givens)
# paths = find_all_paths(graph_3,'Y','Z')
# print paths
# for path in paths:
#     print is_path_active(path, graph_3, graph_3_givens)
print D_separation(graph_3, graph_3_givens,'U', 'Z')