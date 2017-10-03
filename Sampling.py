from Inference import  CPT
import random
graph = {'C': ['R', 'S'],
         'R': ['W'],
         'S': ['W'],
         'W': []}

f_name = "Rain.txt"
topological = ['C', 'S', 'R', 'W']
no = 1000

class PriorSampling:
    def __init__(self, directed_acyclic_graph, file_name, topological_order, no_of_samples ):
        self.assignments = list()
        self.cpt = CPT(directed_acyclic_graph, file_name)
        print self.cpt.get_cpt()
        self.order = topological_order
        self.no_of_samples = no_of_samples
        self.sample_all()

    def sample_all(self):
        for i in range(0, self.no_of_samples):
            self.sample_once()
        # for sample in self.assignments:
        #     print sample

    def sample_once(self):
        signs = dict()
        # for node in self.order:
        for node in self.order:
            string = ""
            # print self.cpt.generate_node_parents().get(node)
            for parent in self.cpt.generate_node_parents().get(node):
                string += signs.get(parent.lower()) + parent.lower()
                # print string
                # print node.lower()
            signs[node.lower()] = self.assign_randomly_given_parents(node.lower(), string)
            # print 'signs', signs
        self.assignments.append(signs)

    def probability_of (self,events):
        n = 0.0
        for ass in self.assignments:
            # print ass
            flag = True
            for event, happen in events.items():
                if happen != ass.get(event):
                    flag = False
                    break
            if flag:
                n += 1
        return n / self.no_of_samples



# small letter node + a string of assigned parents
    def assign_randomly_given_parents(self,node, parents):
        ne_ve = parents + '-' + node
        x = random.uniform(0, 1)
        # print 'x', x
        # print ne_ve, self.cpt.get_cpt_node(node.upper()).get(ne_ve)
        if x > self.cpt.get_cpt_node(node.upper()).get(ne_ve):
            return '+'
        else:
            return '-'

prior = PriorSampling(graph, f_name, topological, no)
print prior.probability_of({ 'w': '+'})
# print prior.assign_randomly_given_parents('w','+r+s')