from graphviz import Graph

# simple graph with manually designed edges
edges = [{7, 2},
         {3, 4},
         {4, 5},
         {5, 6},
         {5, 7},
         {8, 3},
         {6, 3},
         {2, 4},
         {1, 8},
         {6, 1},
         {7, 4},
         {2, 5},
         {9, 8},
         {6, 2},
         {5, 7},
         {1, 5},
         {4, 11},
         {7, 11},
         {10, 5},
         {10, 4},
         {10, 11}]

all_edges = [{i, j} for i in range(12) for j in range(i+1,12)]
all_edges = [x for x in all_edges if len(x) > 1]
complementary_edges = [x for x in all_edges if x not in edges]
# complementary_edges #

# save the graph
dot = Graph(comment='Graph 3 : Clique')
for edge in complementary_edges:
    edge = list(edge)
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='forestgreen',
             penwidth='1.1')
graph_name = 'graphs/clique_transform'
dot.render(graph_name)

# clique = [3, 8]
# for node in clique:
#     dot.node(str(node),
#              color='crimson',
#              penwidth='3.5')

# visualize the graph
