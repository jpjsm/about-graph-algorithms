class GraphMatrix:
    """Adjacency matrix representations of a graph structure.

    Note that a production version of this code should use optimized
    matrix libraries, such as NumPy.

    Attributes
    ----------
    connections : list of list
        The matrix of edge weights.
    num_nodes : int
        The total number of nodes in the graph.
    undirected : bool
        A Boolean indicating whether the graph is undirected (True) or
        directed (False).
    """

    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.connections = [[0.0] * num_nodes for _ in range(num_nodes)]

    def num_edges(self, from_node: int) -> int:
        return sum(1 if weight != 0.0 else 0 for weight in self.connections[from_node])

    def set_edge(self, from_node: int, to_node: int, weight: float):
        """Add, modify, or remove an edge in the graph.

        Parameters
        ----------
        from_node : int
            The node index of the edge's origin.
        to_node : int
            The node index to the edge's destination.
        weight : float
            The weight of the edge. If 0.0 this effectively
            removes the edge.
        """
        if not (0 <= from_node < self.num_nodes):
            raise IndexError("'from_node' out of bounds")

        if not (0 <= to_node < self.num_nodes):
            raise IndexError("'to_node' out of bounds")

        self.connections[from_node][to_node] = weight
        if self.undirected:
            self.connections[to_node][from_node] = weight

    def get_edge(self, from_node: int, to_node: int) -> float:
        """Lookup an edge in the graph.

        Parameters
        ----------
        from_node : int
            The node index of the edge's origin.
        to_node : int
            The node index to the edge's destination.

        Returns
        -------
        weight : float
            The weight of the edge (0.0 if the edge does not exist).
        """
        if not (0 <= from_node < self.num_nodes):
            raise IndexError("'from_node' out of bounds")

        if not (0 <= to_node < self.num_nodes):
            raise IndexError("'to_node' out of bounds")

        return self.connections[from_node][to_node]

    def get_edges(self, from_node) -> list:
        if not (0 <= from_node < self.num_nodes):
            raise IndexError("'from_node' out of bounds")

        return list(
            (from_node, to_node, weight)
            for to_node, weight in enumerate(self.connections[from_node])
        )

    def get_in_neighbors(self, target: int) -> set:
        """Return a list of all node indices such that those nodes
        have edges to the given target node.

        Parameters
        ----------
        target : int
            The index of the destination node.

        Returns
        -------
        neighbors : set
            The set of the in-neighbors' indices for the given node.
        """
        if not (0 <= target < self.num_nodes):
            raise IndexError("'target' out of bounds")

        neighbors: set = set()
        for from_node in range(self.num_nodes):
            if self.connections[from_node][target]:
                neighbors.add(from_node)

        return neighbors

    def get_out_neighbors(self, source: int) -> set:
        """Return a set of the indices to all neighbors source has out-neighbors.

        Returns
        -------
        neighbors : set
            The indices to all neighbors in the edge dictionary.
        """
        if not (0 <= source < self.num_nodes):
            raise IndexError("'source' out of bounds")

        neighbors: set = set()
        for to_node in range(self.num_nodes):
            if self.connections[source][to_node]:
                neighbors.add(to_node)

        return neighbors

    def print_matrix(self):
        for row in self.connections:
            print(" ".join(f"{n: 9.3f}" for n in row))


if __name__ == "__main__":
    g: GraphMatrix = GraphMatrix(5, undirected=False)
    g.set_edge(0, 1, 1.0)
    g.set_edge(0, 3, 1.0)
    g.set_edge(0, 4, 3.0)

    g.set_edge(1, 2, 2.0)
    g.set_edge(1, 4, 1.0)

    g.set_edge(3, 4, 3.0)

    g.set_edge(4, 2, 3.0)
    g.set_edge(4, 3, 3.0)

    g.print_matrix()
