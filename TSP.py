from networkx import get_edge_attributes, get_node_attributes, draw, draw_networkx_edge_labels, Graph, shortest_path
from matplotlib import pyplot as plt
from itertools import combinations
from haversine import haversine
from time import time

start = time()
# lines = []
# f = open("C:\\Users\\I505212\\Desktop\\Irish_cc.txt", 'r')
##f.read().rstrip()
# with open("C:\\Users\\I505212\\Desktop\\Irish_cc.txt", 'r') as temp_file:
#     for line in temp_file:
#         print(line)
# print(coordinates_list)
coordinates_list = [
    ([53.35512, -6.24922]),  # Dublin
    ([54.715139, -6.2192038]),  # Antrim
    ([54.3481977, -6.6540432]),  # Armagh
    ([52.8408344,-6.9261131]),  # Carlow
    ([53.990833, -7.360556]),  # Cavan
    ([52.857257450000006 ,-8.937435925994537]),  # Clare
    ([51.8979282, -8.4705806]),  # Cork
    ([54.9919421 ,-7.316801]),  # Derry
    ([54.92075415, -7.95238521465131]),  # Donegal
    ([54.3517857, -5.961567692639536]),  # Down
    ([54.361874650000004, -7.65671064264496]),  # Fermanagh
    ([53.343475749999996, -8.87336798602502]),  # Galway
    ([52.14540645, -9.517469022554941]),  # Kerry
    ([53.15436455, -6.8184175660976445]),  # Kildare
    ([52.6510216, -7.2484948]),  # Kilkenny
    ([52.9984575, -7.3980337750324185]),  # Laois
    ([54.140162200000006, -8.052478216276088]),  # Leitrim
    ([52.661252, -8.6301239]),  # Limerick
    ([53.7319849, -7.695351399013169]),  # Longford
    ([53.90628485, -6.532050201271116]),  # Louth
    ([53.9087056, -9.298304863654256]),  # Mayo
    ([53.649784350000004, -6.588529492009938]),  # Meath
    ([54.2475233, -6.9692664]),  # Monaghan
    ([53.1361633, -7.810301873855741]),  # Offaly
    ([53.6982695, -8.218250761296193]),  # Roscommon
    ([54.2720696, -8.4751357]),  # Sligo
    ([52.68477435, -7.898080410303971]),  # Tipperary
    ([54.63536485, -7.261142574271752]),  # Tyrone
    ([52.1509131, -7.657798180652727]),  # Waterford
    ([53.5577902, -7.3478558260097575]),  # Westmeath
    ([52.46018745, -6.606515459159162]),  # Wexford
    ([52.95814675, -6.381970708677661])  # Wicklow
]

'''
[([53.305660, -6.322023]),([53.3847197, -6.600949])]



[  # Co-ordinates
    ([53.305660, -6.322023]),
    ([53.3847197, -6.600949]),
    ([53.294168, -6.421985]),
    ([53.2866281, -6.3710803])
    ]
'''

dis_dic = {}  # dictionary for distances between points
count = 0

for i in coordinates_list:  # adds distances between co-ordinates to ddic
    for j in coordinates_list:

        dists = round(haversine(i, j), 5)
        if dists != 0.0 and dists not in dis_dic.values():
            # Ensures no duplicates (e.g. 1->2 & 2->1) and no 0 distances (e.g. 1->1, 2->2 e.t.c.)
            dis_dic[count] = dists  # Serial number = key
            count += 1

G = Graph()

count = 0
no_pts = []  # List for number of nodes in graph
for i in coordinates_list:
    no_pts.append(count)
    G.add_node(count, pos=i)  # Adds nodes to graph at co-ordinate position
    count += 1

comb = list(combinations(no_pts, 2))  # List for all combinations of points for linking each point together in graph

for i in range(len(comb)):
    for j in range(i+1):
        try:
            G.add_weighted_edges_from([(comb[i][j], comb[i][j+1], dis_dic[i])])
            # Add edges with the distance between its nodes ad weight
        except IndexError:
            pass

pos = get_node_attributes(G, 'pos')
plt.figure(3,figsize=(50, 50))
draw(G, pos)
labels = get_edge_attributes(G, 'weight')
draw_networkx_edge_labels(G, pos, edge_labels=labels)
end = time()
plt.show()
print(end - start)
print(shortest_path(G, 1, 21))
