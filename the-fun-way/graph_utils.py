from graph import Graph


def clustering_coefficient(g: Graph, node_id: int) -> float:
    """Compute the clustering coefficient for a node,
       in an not-directed graph!!

    Parameters
    ----------
    g : Graph
        The input graph.
    ind : int
        The node on which to compute the clustering coefficient.

    Returns
    -------
    result : float
        The clustering coefficient.
    """
    neighbors: list = g.nodes[node_id].get_neighbors()

    num_neighbors: int = len(neighbors)
    total_possible: float = (num_neighbors * (num_neighbors - 1)) / 2.0

    if total_possible == 0.0:
        return 0.0

    count: int = 0
    for neighbor in neighbors:
        for edge in g.nodes[neighbor].get_edge_list():
            if edge.to_node > neighbor and edge.to_node in neighbors:
                count += 1

    return count / total_possible


def clustering_coefficient_mean(g: Graph) -> float:
    if g.num_nodes == 0.0:
        return 0.0

    total: float = 0.0

    for node_index in range(g.num_nodes):
        total += clustering_coefficient(g, node_index)

    return total / g.num_nodes
