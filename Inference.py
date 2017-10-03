class CPT:
    def __init__(self, directed_acyclic_graph, file_name):
        self.DAG = directed_acyclic_graph
        self.file_name = file_name
        self.evidence = {}
        self.CPT_node_values = self.get_CPT_node_values()
        self.parents_graph = self.generate_node_parents()
        self.all_cpt_entries = self.generate_all_cpt_entries()

    def get_cpt_node(self, node):
        return self.get_cpt().get(node)

    def get_CPT_node_values(self):
        cpt_node_values = dict()
        file_handler = open(self.file_name)
        for line in file_handler:
            l = list()
            l = line.split()
            x = l.pop(0)
            for i in range(0, len(l)):
                l[i] = float(l[i])
            if x[0] == '+' or x[0] == '-':
                self.evidence[x[1].upper()] = x[0]
            cpt_node_values[x] = l
        return  cpt_node_values

    def generate_node_parents(self):
        parents_graph= dict()
        for k in self.DAG.keys():
            parents_graph[k] = list()
        for parent, children in self.DAG.items():
            for child in children:
                if parent not in parents_graph.get(child):
                    parents_graph[child].append(parent)
        return parents_graph

    def generate_cpt_entries(self, node):
        nodes = list()
        for el in self.parents_graph[node]:
            nodes.append(el.lower())
        nodes.sort()
        nodes.append(node.lower())
        nodes_with_evidence = list()
        for el in nodes:
            nodes_with_evidence.append(el)
        evidences_positions = dict()
        for i in range(0, len(nodes)):
            if self.evidence.get(nodes[i].upper()):
                evidences_positions[nodes[i]] = i
        import operator
        sorted_evidences_positions = sorted(evidences_positions.items(), key=operator.itemgetter(1))
        for k in self.evidence.keys():
            if k.lower() in nodes:
                nodes.remove(k.lower())
        n = len(nodes)
        rows_no = 2 ** n
        x = n
        cpt_entries = [[] for _ in range(rows_no)]
        for m in range(0, n):
            alternates = 2 ** x
            element = nodes[m]
            for i in range(0, rows_no / alternates):
                offset = i * alternates
                for j in range(0, alternates / 2):
                    cpt_entries[j + offset].append('+' + element)
                for k in range(alternates / 2, alternates):
                    cpt_entries[k + offset].append('-' + element)
            x -= 1
        for entry in cpt_entries:
            for el in sorted_evidences_positions:
                entry.insert(el[1], self.evidence.get(el[0].upper()) + el[0])

        return cpt_entries

    def generate_cpt_entries_string(self, node):
        l = self.generate_cpt_entries(node)
        l_string = list()
        for el in l:
            s = ''.join(str(e) for e in el)
            l_string.append(s)
        return l_string

    def generate_all_cpt_entries(self):
        all_cpt_entries =dict()
        for node in self.DAG.keys():
            all_cpt_entries[node] = self.generate_cpt_entries_string(node)
        return all_cpt_entries

    def get_cpt(self):
        cpt = dict()
        for node,entries in self.all_cpt_entries.items():
            if self.evidence.get(node):
                node = self.evidence.get(node) + node.lower()
            entry_value_pair = dict()
            values = list()
            values = self.CPT_node_values.get(node)
            for i in range(0, len(entries)):
                entry_value_pair[entries[i]] = values[i]
            cpt[node] = entry_value_pair
        return cpt


class InferenceByVariableElimination:
    def __init__(self, directed_acyclic_graph, file_name):
        conditional_probability_table = CPT(directed_acyclic_graph, file_name)
        bayes_net = conditional_probability_table.get_cpt()
        self.cpt = bayes_net

    # def multiply(self, table_l, table_m, el):
    #     ls = sorted(table_l.keys())
    #     ms = sorted(table_m.keys())
    #     el_po = '+' + el.lower()
    #     el_ne = '-' + el.lower()
    #     l_po = list()
    #     l_ne = list()
    #     m_po = list()
    #     m_ne = list()
    #     # creating the positive lists
    #     for x in ls:
    #         if el_po in x:
    #             l_po.append(x)
    #     for x in ms:
    #         if el_po in x:
    #             m_po.append(x)
    #     # creating the negative lists
    #     for y in ls:
    #         if el_ne in y:
    #             l_ne.append(y)
    #     for y in ms:
    #         if el_ne in y:
    #             m_ne.append(y)
    #     # calculating the multiplication by extracting the value of each element from the two table multiply them
    #     # form a new entry with the summing element at the beginning of this entry then associate this entry
    #     # with the calculated value
    #     result_table = dict()
    #     for positive_entry_l in l_po:
    #         for positive_entry_m in m_po:
    #             value = table_l.get(positive_entry_l) * table_m.get(positive_entry_m)
    #             new_positive_entry_l = positive_entry_l.replace(el_po, '')
    #             new_positive_entry_m = positive_entry_m.replace(el_po, '')
    #             entry = el_po + new_positive_entry_l + new_positive_entry_m
    #             result_table[entry] = value
    #     for negative_entry_l in l_ne:
    #         for negative_entry_m in m_ne:
    #             value = table_l.get(negative_entry_l) * table_m.get(negative_entry_m)
    #             new_negative_entry_l = negative_entry_l.replace(el_ne, '')
    #             new_negative_entry_m = negative_entry_m.replace(el_ne, '')
    #             entry = el_ne + new_negative_entry_l + new_negative_entry_m
    #             result_table[entry] = value
    #     return result_table


    def extract_co_elements(self, table_1, table_2):
        # extracting common elements in both lists and put them in a list
        # returns common elements list
        # getting each table elements
        common = list()
        table_1_els_w_s = table_1.keys()[0]
        table_2_els_w_s = table_2.keys()[0]
        table_1_els = list()
        table_2_els = list()
        for ch in table_1_els_w_s:
            if ch == '+' or ch == '-':
                continue
            else:
                table_1_els.append(ch)
        for ch in table_2_els_w_s:
            if ch == '+' or ch == '-':
                continue
            else:
                table_2_els.append(ch)
        # figuring out common elements:
        for el in table_1_els:
            if el in table_2_els:
                common.append(el)
        return common

    # generate signed common elements and return them as a list of lists
    def generate_signed_co_elements(self, common):
        nodes = common
        n = len(nodes)
        rows_no = 2 ** n
        x = n
        cpt_entries = [[] for _ in range(rows_no)]
        # for el in self.evidences.key():
        #     if el.lower() in common:
        #         common.remove(el)
        for m in range(0, n):
            alternates = 2 ** x
            element = nodes[m]
            for i in range(0, rows_no / alternates):
                offset = i * alternates
                for j in range(0, alternates / 2):
                    cpt_entries[j + offset].append('+' + element)
                for k in range(alternates / 2, alternates):
                    cpt_entries[k + offset].append('-' + element)
            x -= 1
        common_entries = cpt_entries
        return common_entries

    def extract_co_keys(self, table_1, table_2, entry):
        # return w lists co_keys_1 ,co_keys_2 witch contains the corresponding elements from each table
        # to this entry.
        # extracting entries from table_1 and table_2 corresponding to this common entry
        # and putting them in lists (co_key_1 , co_key_2).
        co_keys_1 = list()
        for k in table_1.keys():
            is_co_key_1 = True
            for el in entry:
                if el not in k:
                    is_co_key_1 = False
                    break
            if is_co_key_1:
                co_key_1 = k
                co_keys_1.append(co_key_1)
        co_keys_2 = list()
        for k in table_2.keys():
            is_co_key_2 = True
            for el in entry:
                if el not in k:
                    is_co_key_2 = False
                    break
            if is_co_key_2:
                co_key_2 = k
                co_keys_2.append(co_key_2)
        return co_keys_1, co_keys_2

    def sub_string(self, string, start, end):
        sub = ""
        for i in range(start, end):
            sub += string[i]
        return sub

    def generate_new_name(self, key_1, key_2):
        name = key_1
        i = 0
        while i < len(key_2):
            el = self.sub_string(key_2, i, i + 2)
            if el not in name:
                name += el
            i += 2
        return name

    def multiply(self, table_1, table_2, el):
        common = self.extract_co_elements(table_1, table_2)
        common_entries = self.generate_signed_co_elements(common)
        result_table = dict()
        for entry in common_entries:
            co_keys_1, co_keys_2 = self.extract_co_keys(table_1, table_2, entry)
            for key_1 in co_keys_1:
                for key_2 in co_keys_2:
                    new_entry = self.generate_new_name(key_1, key_2)
                    value = table_1.get(key_1) * table_2.get(key_2)
                    result_table[new_entry] = value

        return result_table


    def sum_out(self, table, el):
        # creating positive and negative lists
        summed_out_table = dict()
        el_po = '+'+el.lower()
        el_ne = '-'+el.lower()
        ts = sorted(table.keys())
        t_po = list()
        t_ne = list()
        # creating the positive lists
        for x in ts:
            if el_po in x:
                t_po.append(x)
        # creating the positive lists
        for y in ts:
            if el_ne in y:
                t_ne.append(y)
        for i in range(0, len(t_po)):
            value = table.get(t_po[i]) + table.get(t_ne[i])
            entry = t_po[i]
            summed_entry = entry.replace(el_po, '')
            summed_out_table[summed_entry] = value
        return summed_out_table

    def factorize(self, factors, el):
        table = factors[0]
        for i in range(0, len(factors) - 1):
            table = self.multiply(table, factors[i+1], el)
        # print 'table: ', table
        new_factor = self.sum_out(table, el)
        # print 'new_factor: ',  new_factor
        return new_factor

    def eliminate(self, list_of_elimination):
        new_factors = list()
        cpt_list = list()
        for v in self.cpt.values():
            cpt_list.append(v)
        el = 'A'
        for el in list_of_elimination:
            factors = list()
            print 'el: ', el
            print 'cpt_list: ', cpt_list
            print 'length of cpt list: ', len(cpt_list)
            for i in range(0, len(cpt_list)):
                print 'cpt_list[i]: ', cpt_list[i]
            current_tables = list()
            for table in cpt_list:
                print 'length of cpt list: ', len(cpt_list)
                # keys of table as a list
                print 'table: ', table
                table_list = list(table)
                print 'table_list[0]: ', table_list[0]
                print 'el.lower(): ', el.lower()
                if el.lower() in table_list[0]:
                    current_tables.append(table)
            for table in current_tables:
                factors.append(table)
                cpt_list.remove(table)
            current_factors = list()
            for new_factor in new_factors:
                new_factor_list = list(new_factor)
                if el.lower() in new_factor_list[0]:
                    current_factors.append(new_factor)
            for factor in current_factors:
                factors.append(factor)
                new_factors.remove(factor)
            print 'factors: ', factors
            new_factors.append(self.factorize(factors, el))
            print 'cpt_list: ', cpt_list
            print 'new_factors: ', new_factors


Dag = {'B': ['A'],
       'E': ['A'],
       'A': ['J', 'M'],
       'J': [],
       'M': []}
graph_1 = {'A': ['B'],
           'B': ['C', 'D'],
           'C': ['E'],
           'D': ['E'],
           'E': []}
# file_name_1 = 'table-1.txt'
#
# cpt = CPT(Dag, "Burglary.txt")
# print cpt.get_cpt()
#
# print cpt.generate_cpt_entries('A')
# print cpt.generate_cpt_entries_string('A')
# print cpt.DAG
# print cpt.generate_node_parents()
#
#


# print cpt.get_CPT_node_values()
# print cpt.generate_node_parents()
# print cpt.generate_cpt_entries('A')
# print cpt.generate_cpt_entries_string('A')
# print cpt.generate_all_cpt_entries()
# Cpt = cpt.get_cpt()
# print Cpt
# for k,v in Cpt.items():
#     print k
#     for x, y in v.items():
#         print x,y
# cpt_1 = CPT(graph_1,file_name_1)
# print cpt_1.get_CPT_node_values()
# print cpt_1 .generate_node_parents()
# print cpt_1.generate_cpt_entries_string('E')
# print cpt_1.generate_cpt_entries('D')
# print cpt_1.generate_all_cpt_entries()
# print cpt_1.get_cpt()
# table_l = {'+a-e-f': 4, '-a+e+f': 5, '+a-e+f': 3, '-a-e+f': 7, '-a-e-f': 8, '+a+e-f': 2, '-a+e-f': 6, '+a+e+f': 1}
# table_m = {'+d+a': 1, '+d-a': 2, '-d-a': 4, '-d+a': 3}
# i = InferenceByVariableElimination(graph_1, file_name_1)
# r1 = i.multiply(table_l, table_m, 'A')
# table_k = {'+a': 1, '-a': 2}
# print i.multiply(table_k, r1, 'A')
# print r1
# print i.sum_out(r1, 'A')
# factors_list = [table_l,table_k,table_m]
# i.factorize(factors_list, 'A')

# infrence = InferenceByVariableElimination(graph_1,file_name_1)
# infrence.eliminate(['A','B', 'D'])