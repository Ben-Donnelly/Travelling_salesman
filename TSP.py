from networkx import get_node_attributes, draw, Graph, draw_networkx_labels
from matplotlib import pyplot as plt
from itertools import combinations
from haversine import haversine
from time import time
from numpy import genfromtxt
import numpy as np
from collections import OrderedDict
start = time()

x = genfromtxt(r"C:\Users\Ben Donnelly\Desktop\coordinates.txt", delimiter=',', dtype=None, usecols=np.arange(0, 2))

d1 = OrderedDict([("Dublin", (53.35512, -6.24922)), ("Antrim", (54.715139, -6.2192038)),
                  ("Armagh", (54.3481977, -6.6540432)), ("Carlow", (52.8408344, -6.9261131)),
                  ("Cavan", (53.990833, -7.360556)), ("Clare", (52.857257450000006, -8.937435925994537)),
                  ("Cork", (51.8979282, -8.4705806)), ("Derry", (54.9919421, -7.316801)),
                  ("Donegal", (54.92075415, -7.95238521465131)),
                  ("Down", (54.3517857, -5.961567692639536)), ("Fermanagh", (54.361874650000004, -7.65671064264496)),
                  ("Galway", (53.343475749999996, -8.87336798602502)), ("Kerry", (52.14540645, -9.517469022554941)),
                  ("Kildare", (53.15436455, -6.8184175660976445)), ("Kilkenny", (52.6510216, -7.2484948)),
                  ("Laois", (52.9984575, -7.3980337750324185)), ("Leitrim", (54.140162200000006, -8.052478216276088)),
                  ("Limerick", (52.661252, -8.6301239)), ("Longford", (53.7319849, -7.695351399013169)),
                  ("Louth", (53.90628485, -6.532050201271116)), ("Mayo", (53.9087056, -9.298304863654256)),
                  ("Meath", (53.649784350000004, -6.588529492009938)), ("Monaghan", (54.2475233, -6.9692664)),
                  ("Offaly", (53.1361633, -7.810301873855741)), ("Roscommon", (53.6982695, -8.218250761296193)),
                  ("Sligo", (54.2720696, -8.4751357)), ("Tipperary", (52.68477435, -7.898080410303971)),
                  ("Tyrone", (54.63536485, -7.261142574271752)), ("Waterford", (52.1509131, -7.657798180652727)),
                  ("Westmeath", (53.5577902, -7.3478558260097575)), ("Wexford", (52.46018745, -6.606515459159162)),
                  ("Wicklow", (52.95814675, -6.381970708677661))])

coordinates_list = []
for i in x:
    coordinates_list.append((tuple(i)))

dis_dic = {}  # dictionary for distances between points
count = 0
items = list(d1.items())

# Need to iterate through the ordereddict, atm line 117 is outputting the counties
for i in items:  # adds distances between co-ordinates to dis_dic
    for j in items:
        dists = round(haversine(i[1], j[1]), 5)
        if dists != 0.0 and dists not in dis_dic.values():
            # Ensures no duplicates (e.g. 1->2 & 2->1) and no 0 distances (e.g. 1->1, 2->2 e.t.c.)
            dis_dic[count] = dists  # Serial number = key
            count += 1

G = Graph()

for idx, val in enumerate(coordinates_list):
    G.add_node(idx, pos=val)

mix = list(combinations((i for i in range(G.number_of_nodes())), 2))
# List for all combinations of points for linking each point together in graph

G.add_edges_from(mix)

for ind, i in enumerate(dis_dic):
    G.add_weighted_edges_from([(mix[ind][0], mix[ind][1], dis_dic[ind])])


tour = [0] * 31
count = 0
county_nums = [0] * 31
p = 0
prev_node = 0

while 0.0 in tour:
    cost = 10000
    for i, j in G.adj[p].items():
        if j['weight'] < cost:
            cost = j['weight']
            county_nums[count] = i
            tour[count] = items[i][0]
            p = i
    count += 1
    G.remove_node(prev_node)
    prev_node = p

tour.insert(0, "Dublin")
tour.append("Dublin")
print(tour)
f = {v: k for v, k in enumerate(tour)}
print(f)
# quit()
for i in tour:
    print(str(d1[i])[1:-1])
newl = []
for i in tour:
    newl.append(d1[i])

G1 = Graph()
print(time() - start)
for idx, val in enumerate(newl):
    print(idx, val)
    G1.add_node(idx, pos=val)
pos = get_node_attributes(G1, 'pos')

plt.figure("Road trip 2.0", figsize=(50, 50))
x = []
i = 0
j = 1
while len(x) < 32:
    x.append((i, j))
    i += 1
    j += 1
G1.add_edges_from(x)
draw_networkx_labels(G1, pos, f)
draw(G1, pos)
print(newl)

plt.show()
