import pickle
import random
from graphviz import Graph


def generate_problem_instance(n_nodes, max_successors):
    """
        Function used to generate an instance of the dominating set problem.
        We use undirected graphs, edges are not directed.

        Parameters
        ----------
            n_nodes : number of nodes in the graph.

            max_successors : HALF maximum number of neighbors for each node.
            this comes from the way we build the graph. For a given node,
            say node_A,
            we pick a random number of successors, smaller than max_successors.
            But node_A might also be picked as a successor by other nodes in
            the graph. Since we are working in a undirected graph, the concept
            of successor is not perfeclty relevant. We should just see it
            as a convenient quantity when building the graph.
            But we will store the final result as
            "neighbor".

        Output:
        -------
            saves a representation of the graph.
            saves graph data (list of edges, list of successors)
            in a pickle file (binary file)
    """
    msg = (
        f"\ngenerate problem instance for {n_nodes} nodes and at most "
        f"{max_successors} successors per node"
    )
    print(msg)
    successors = {}
    for node in range(1, n_nodes + 1):
        nb_of_successors = random.randint(1, max_successors)
        # avoid node linked to itsself
        successors_of_node = random.sample(
            range(1, n_nodes + 1), nb_of_successors)
        # print(successors)
        successors[node] = successors_of_node

    # we are working with an undirected graph.
    # As q consequence,
    # if node_A is successor of node_B, then
    # node_B is also successor of node_A
    for node in successors:
        for successor in successors[node]:
            if node not in successors[successor]:
                successors[successor].append(node)
    # at this point, we have neighbors, rather than
    # successors

    # print(successors)

    edges_list = []
    # build list of edges
    # the edges will just be used for plotting.
    # so we will not keep noth edges [node_A, node_B] and
    # [node_B, node_A]
    for node in range(1, n_nodes + 1):
        for successor_of_node in successors[node]:
            if [node, successor_of_node] not in edges_list:
                # remove duplicate edges (undirected graph)
                if [successor_of_node, node] not in edges_list:
                    # remove self edge
                    if node is not successor_of_node:
                        edges_list.append([node, successor_of_node])

    print("edges")
    print(edges_list)
    # print(len(edges_list))

    dot = Graph(comment='Graph used to study the dominating set problem')
    for edge in edges_list:
        dot.edge(str(edge[0]),
                 str(edge[1]),
                 color='darkolivegreen4',
                 penwidth='1.1')

    parameters = f"n={n_nodes}_maxs={max_successors}"
    with open("data/"+parameters+"_neighbors", "wb") as f:
        pickle.dump(successors, f)

    with open(f"data/"+parameters+"_edges", "wb") as f:
        pickle.dump(edges_list, f)

    # visualize the graph
    graph_name = "generated/"+parameters
    dot.render(graph_name)


# generate_problem_instance(20, 5)
# generate_problem_instance(40, 6)
# generate_problem_instance(15, 4)
# generate_problem_instance(80, 4)
