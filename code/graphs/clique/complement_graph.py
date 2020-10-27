from plot_graph import plot_graph
import pickle

with open(f"data/edges", "rb") as f:
    edges = pickle.load(f)

# reformat edges as a list of tuples
edges = [set(edge) for edge in edges]

# plot initial graph
plot_graph(edges, "initial graph")

"""
    build complement graph
"""

# build the list of all nodes
# we assume there are no isolated nodes
nodes=list()
for edge in edges:
    for edge_node in edge:
        if edge_node not in nodes:
            nodes.append(edge_node)


"""
    ADD LINES HERE
"""
# build all edges

# choose complement edges

# plot complement graph
