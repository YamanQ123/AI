# DAG = {'B': ['A'],
#        'E': ['A'],
#        'A': ['J','M'],
#        'J': [],
#        'M': []}
# graph_1 = {'A': ['B'],
#            'B': ['C','D'],
#            'C': ['E'],
#            'D': ['E'],
#            'E': []}
# file_name = "Burglary.txt"
# file_name_1 = 'table-1.txt'
# file_handler = open(file_name_1)
# CPT_node_values = dict()
# evidence_1 = {}
# for line in file_handler:
#     l = list()
#     l = line.split()
#     x = l.pop(0)
#     if x[0] == '+' or x[0] == '-':
#         evidence_1[x[1].upper()] = x[0]
#     CPT_node_values[x] = l
# print CPT_node_values
# print evidence_1
#
# def generate_node_parents(graph):
#     parents_graph = dict()
#     for k in graph.keys():
#         parents_graph[k] = list()
#     for parent, children in graph.items():
#         for child in children:
#             if parent not in parents_graph.get(child):
#                 parents_graph[child].append(parent)
#     return parents_graph
#
# # parents = generate_node_parents(DAG)
# # print parents
# # remove all evidences from the node:
# # then add them after finishing all the values
# parents_1 = generate_node_parents(graph_1)
# print parents_1
# nodes = list()
# for el in parents_1['E']:
#     nodes.append(el.lower())
# nodes.sort()
# nodes.append('e')
# nodes_with_evidence = list()
# for el in nodes:
#     nodes_with_evidence.append(el)
# evidences_positions = dict()
#
# for i in range(0,len(nodes)):
#     print evidence_1.get(nodes[i].upper())
#     if evidence_1.get(nodes[i].upper()):
#         evidences_positions[nodes[i]] = i
# print nodes
# import operator
# sorted_evidences_positions = sorted(evidences_positions.items(), key=operator.itemgetter(1))
# for k in evidence_1.keys():
#     if k.lower() in nodes:
#         nodes.remove(k.lower())
# print 'nodes',nodes
# print 'evidences_positions:',evidences_positions
# n = len(nodes)
# rows_no = 2 ** n
# x = n
# print'nodes', nodes
# print n
# #
# #
# print 'evidence_!',evidence_1
# def generate_cpt_entries(node,parents,evidence_1):
#     nodes = list()
#     for el in parents[node]:
#         nodes.append(el.lower())
#     nodes.sort()
#     nodes.append(node.lower())
#     nodes_with_evidence = list()
#     for el in nodes:
#         nodes_with_evidence.append(el)
#     evidences_positions = dict()
#     for i in range(0, len(nodes)):
#         print evidence_1.get(nodes[i].upper())
#         if evidence_1.get(nodes[i].upper()):
#             evidences_positions[nodes[i]] = i
#     import operator
#     sorted_evidences_positions = sorted(evidences_positions.items(), key=operator.itemgetter(1))
#     for k in evidence_1.keys():
#         print 'k.lower(_)',k.lower()
#         if k.lower() in nodes:
#             nodes.remove(k.lower())
#     print 'nodes',nodes
#     n = len(nodes)
#     print 'n',n
#     rows_no = 2 ** n
#     x = n
#     cpt_entries = [[] for _ in range(rows_no)]
#     for m in range(0, n):
#         alternates = 2 ** x
#         element = nodes[m].lower()
#         for i in range(0, rows_no / alternates):
#             offset = i * alternates
#             for j in range(0, alternates / 2):
#                 cpt_entries[j + offset].append('+' + element)
#             for k in range(alternates / 2, alternates):
#                 cpt_entries[k + offset].append('-' + element)
#         x -= 1
#     for entry in cpt_entries:
#         for el in sorted_evidences_positions:
#             entry.insert(el[1],evidence_1.get(el[0].upper())+ el[0])
#
#     return cpt_entries
# print generate_cpt_entries('E',parents_1,evidence_1)

# print parents
# list1 = ['a', 'b', 'c']
# str1 = ''.join(str(e) for e in list1)
# print str1
import random
print random.uniform(0, 1)