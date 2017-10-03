from Inference import  CPT
import random
graph = {'C': ['R', 'S'],
         'R': ['W'],
         'S': ['W'],
         'W': []}

f_name = "Rain.txt"
topological = ['C', 'S', 'R', 'W']
no = 10


class WeightedSampling:
    def __init__(self, directed_acyclic_graph, file_name, topological_order, no_of_samples):
        self.assignments = list()
        self.cpt = CPT(directed_acyclic_graph, file_name)
        print self.cpt.get_cpt()
        self.order = topological_order
        self.no_of_samples = no_of_samples
        self.weight = 0

        # small letter node + a string of assigned parents

    def assign_randomly_given_parents(self, node, parents):
        ne_ve = parents + '-' + node
        x = random.uniform(0, 1)
        # print 'x', x
        # print ne_ve, self.cpt.get_cpt_node(node.upper()).get(ne_ve)
        if x > self.cpt.get_cpt_node(node.upper()).get(ne_ve):
            return '+'
        else:
            return '-'

    def weight_evidence(self, e, parents, evidence):
        ve = parents + evidence.get(e) + e
        w = self.cpt.get_cpt_node(e.upper()).get(ve)

        return evidence.get(e), w

    def sample_once(self, evidence):
        signs = dict()
        weight = 1
        for node in self.order:
            string = ""
            is_evidence = False
            # print self.cpt.generate_node_parents().get(node)
            for parent in self.cpt.generate_node_parents().get(node):
                string += signs.get(parent.lower()) + parent.lower()
                # print string
            if evidence is not None:
                if evidence.get(node.lower()):
                    is_evidence = True
                    s, w = self.weight_evidence(node.lower(), string, evidence)
                    weight *= w
                    signs[node.lower()] = s
            if not is_evidence:
                assigned_value = self.assign_randomly_given_parents(node.lower(), string)
                # print 'node:  ', node.lower()
                # print 'assigned value:  ', assigned_value
                signs[node.lower()] = assigned_value
                # print 'signs', signs
        self.assignments.append((signs, weight))
        # print 'assignments ',self.assignments
        return weight

    def sample_all(self, evidence=None):
        for i in range(0, self.no_of_samples):
            self.weight += self.sample_once(evidence)
        for sample in self.assignments:
            print sample
        print self.weight

    def probability_of(self, events, evidence=None):
        n = 0.0
        self.sample_all(evidence)
        for ass in self.assignments:
            # print ass
            flag = True
            for event, happen in events.items():
                if happen != ass[0].get(event):
                    flag = False
                    break
            if flag:
                n += ass[1]
        return n / self.weight


weighted = WeightedSampling(graph, f_name, topological, no)
print weighted.probability_of({'c': '+'}, {'r': '+', 'w': '+'})



