# l = ['a','b']
# l.insert(1,'c')
# l.insert(3, 'd')
# print l
# d = {'a': 2,
#      'b': 1,
#      'c': 3}
# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# d_list = list(d)
# print 'd_list',  d_list
# sorted_x = sorted(x.items(), key=operator.itemgetter(1))
# print sorted_x
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# print sorted_d
# el = 'A'
# l = ['-a+e+f','+a+e+f','+a-e+f','+a-e-f','+a+e-f','-a-e+f','-a-e-f','-a+e-f']
# m = ['+d+a','-d-a','-d+a','+d-a']
#
# ls = sorted(l)
# ms = sorted(m)
#
# print ls
# print ms
# el_po = '+' + el.lower()
# el_ne = '-' + el.lower()
# l_po = list()
# l_ne = list()
# m_po = list()
# m_ne = list()
# # creating the tables(dictionaries) for the two lists
# table_l = dict()
# table_m = dict()
# for i in range(0, len(ls)):
#     table_l[ls[i]] = (i+1)
# for i in range(0 , len(ms)):
#     table_m[ms[i]] = (i+1)
# print table_l
# print table_m
#
# # creating the positive lists
# for x in ls:
#     if el_po in x:
#         l_po.append(x)
# for x in ms:
#     if el_po in x:
#         m_po.append(x)
# # creating the negative lists
# for y in ls:
#     if el_ne in y:
#         l_ne.append(y)
# for y in ms:
#     if el_ne in y:
#         m_ne.append(y)
# print l_po, l_ne
# print m_po, m_ne
#
# # calculating the multiplication by extracting the value of each element from the two table multiply them
# # form a new entry with the summing element at the beginning of this entry then associate this entry with the calculated
# # value
# result_table = dict()
# for positive_entry_l in l_po:
#     for positive_entry_m in m_po:
#         value = table_l.get(positive_entry_l) * table_m.get(positive_entry_m)
#         new_positive_entry_l = positive_entry_l.replace(el_po, '')
#         new_positive_entry_m = positive_entry_m.replace(el_po, '')
#         entry = el_po + new_positive_entry_l + new_positive_entry_m
#         result_table[entry] = value
# for negative_entry_l in l_ne:
#     for negative_entry_m in m_ne:
#         value = table_l.get(negative_entry_l) * table_m.get(negative_entry_m)
#         new_negative_entry_l = negative_entry_l.replace(el_ne, '')
#         new_negative_entry_m = negative_entry_m.replace(el_ne, '')
#         entry = el_ne + new_negative_entry_l + new_negative_entry_m
#         result_table[entry] = value
# print 'result', result_table
#
# o = ['+a-e+f', '-a-e+f','-a-e-f','+a-e-f']
# w = ['+a+e-f','+a+e+f', '-a+e+f','-a+e-f']
# print sorted(o)
# print sorted(w)
#
#
#
table_2 = {'-c-d+e': 0.5, '-c+d+e': 0.7, '+c+d+e': 0.3, '+c-d+e': 0.1}
table_1 = {'+c-d': 0.5810000000000001, '-c-d': 0.069, '-c+d': 0.051, '+c+d': 0.299}
def extract_co_elements(table_1, table_2):
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
def generate_signed_co_elements(common):
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


def extract_co_keys(table_1, table_2, entry):
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


def sub_string(string, start, end):
    sub = ""
    for i in range(start, end):
        sub += string[i]
    return sub

def generate_new_name(key_1, key_2):
    name = key_1
    i = 0
    while i < len(key_2):
        el = sub_string(key_2, i, i+2)
        if el not in name:
            name += el
        i += 2
    return name


def multiply(table_1, table_2):
    common = extract_co_elements(table_1, table_2)
    common_entries = generate_signed_co_elements(common)
    result_table = dict()
    for entry in common_entries:
        co_keys_1, co_keys_2 = extract_co_keys(table_1, table_2, entry)
        for key_1 in co_keys_1:
            for key_2 in co_keys_2:
                new_entry = generate_new_name(key_1, key_2)
                value = table_1.get(key_1) * table_2.get(key_2)
                result_table[new_entry] = value

    return result_table

print multiply(table_1, table_2)
# getting the name of the new table entry





