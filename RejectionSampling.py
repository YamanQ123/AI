from Inference import  CPT
import random
graph = {'C': ['R', 'S'],
         'R': ['W'],
         'S': ['W'],
         'W': []}

f_name = "Rain.txt"
topological = ['C', 'S', 'R', 'W']
no = 100


class RejectionSampling:
    def __init__(self, directed_acyclic_graph, file_name, topological_order, no_of_samples):
        self.assignments = list()
        self.cpt = CPT(directed_acyclic_graph, file_name)
        print self.cpt.get_cpt()
        self.order = topological_order
        self.no_of_samples = no_of_samples
        self.actual_no_of_samples = 0

    def sample_once(self, evidence):
        signs = dict()
        for node in self.order:
            string = ""
            # print self.cpt.generate_node_parents().get(node)
            for parent in self.cpt.generate_node_parents().get(node):
                string += signs.get(parent.lower()) + parent.lower()
                # print string

            assigned_value = self.assign_randomly_given_parents(node.lower(), string)
            # print 'node:  ', node.lower()
            # print 'assigned value:  ', assigned_value

            if evidence is not None:
                if evidence.get(node.lower()):
                    # print 'evidence on node: ', evidence.get(node.lower())
                    if evidence.get(node.lower()) != assigned_value:
                        return
            signs[node.lower()] = assigned_value
            # print 'signs', signs
        self.actual_no_of_samples += 1
        # print 'actual no ', self.actual_no_of_samples
        self.assignments.append(signs)
        # print 'assignments ',self.assignments

    def assign_randomly_given_parents(self, node, parents):
        ne_ve = parents + '-' + node
        x = random.uniform(0, 1)
        # print 'x', x
        # print ne_ve, self.cpt.get_cpt_node(node.upper()).get(ne_ve)
        if x > self.cpt.get_cpt_node(node.upper()).get(ne_ve):
            return '+'
        else:
            return '-'

    def sample_all(self, evidence):
        for i in range(0, self.no_of_samples):
            self.sample_once(evidence)
        for sample in self.assignments:
            print sample
        print self.actual_no_of_samples

    def probability_of(self, events, evidence=None):
        n = 0.0
        self.sample_all(evidence)
        for ass in self.assignments:
            # print ass
            flag = True
            for event, happen in events.items():
                if happen != ass.get(event):
                    flag = False
                    break
            if flag:
                n += 1
        return n / self.actual_no_of_samples




rejection = RejectionSampling(graph, f_name, topological, no)
# print rejection.sample_all({'c': '+','r': '+'})
print rejection.probability_of({'c': '+'}, {'r': '+', 'w': '+'})
