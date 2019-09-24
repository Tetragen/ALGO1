"""
   greedy algorithm to try to find a minimal dominant set
   different heuristic.
"""

import pickle
from graphviz import Graph


def process_graph(graph_name):
    dot = Graph(comment='Graph used to study the dominating set problem')

    # load graph data
    with open("data/"+graph_name+"_neighbors", "rb") as f:
        neighbors = pickle.load(f)

    with open("data/"+graph_name+"_edges", "rb") as f:
        edges_list = pickle.load(f)

    # print(neighbors)
    # size of the graph (number of nodes)
    n_nodes = len(neighbors)

    """
        sort the nodes by degree
        aka the number of neighbors
    """
    sorted_dictionary = sorted(neighbors,
                               key=lambda node: len(neighbors[node]),
                               reverse=True)
    # sorted does not modify the original sequence and returns a new dico
    # it returns a list
    # print(type(sorted_dictionary))

    print('=====')
    print('sorted dictionary of neighbors by degree of the node')
    print('=====')

    for node in sorted_dictionary:
        print(f"node  {node}")
        print(f"neighbors {neighbors[node]}")

    """
        prepare graph plot
    """

    dot = Graph(comment='Graph 1 : dominating set')
    for edge in edges_list:
        dot.edge(str(edge[0]),
                 str(edge[1]),
                 color='darkolivegreen4',
                 penwidth='1.1')
    plot_name = "processed_alternative/"+graph_name+f"/greedy_0"
    dot.render(plot_name)

    def highlight_node(node, dot, step, color):
        dot.node(str(node),
                 color=color,
                 penwidth='4')
        # visualize the graph
        plot_name = "processed_alternative/"+graph_name+f"/greedy_{step}"
        dot.render(plot_name)

    """
        greedy algorithm
    """

    print('\n======')
    print('greedy algorithm')
    print('======')

    dominating_set = []
    dominated_nodes = []

    # use an step for plotting images
    step = 0
    for node in sorted_dictionary:
        step += 1
        # stop if the set is dominating
        if len(dominated_nodes) < n_nodes:
            # update our dominating set
            dominating_set.append(node)
            print(f"\nadd {node} to the dominating set")
            # update the list of dominated nodes
            if node not in dominated_nodes:
                dominated_nodes.append(node)
                print(f"add {node} to the list of dominated nodes")
            # print('neighbors : ')
            for neighbor in neighbors[node]:
                if neighbor not in dominated_nodes:
                    # update the list of not dominated nodes
                    dominated_nodes.append(neighbor)
                    print(
                        f"add {neighbor} to the list of dominated nodes")
                    # plot dominated nodes that are not in the dominant set
                    if neighbor not in dominating_set:
                        highlight_node(neighbor, dot, step,
                                       "darkslategray4")
            # see how many more nodes we have to dominate
            print(
                f"still have to dominate {n_nodes-len(dominated_nodes)} nodes")
            highlight_node(node, dot, step, "coral")
            if len(dominated_nodes) == n_nodes:
                title = (
                    f"dominated\ndominating set of size "
                    f"{len(dominating_set)}"
                )
                dot.node(title, color="darkorchid", penwidth="6", fontsize="30")
                dot.render("processed_alternative/" + graph_name+f"/greedy_final")


process_graph("exercise")

n_nodes = 30
max_successors = 5
parameters = f"n={n_nodes}_maxs={max_successors}"
process_graph(parameters)

n_nodes = 15
max_successors = 4
parameters = f"n={n_nodes}_maxs={max_successors}"
process_graph(parameters)

n_nodes = 40
max_successors = 6
parameters = f"n={n_nodes}_maxs={max_successors}"
process_graph(parameters)

n_nodes = 20
max_successors = 5
parameters = f"n={n_nodes}_maxs={max_successors}"
process_graph(parameters)

n_nodes = 80
max_successors = 4
parameters = f"n={n_nodes}_maxs={max_successors}"
process_graph(parameters)
