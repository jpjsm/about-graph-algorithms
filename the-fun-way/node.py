from typing import Union

from edge import Edge


class Node:
    """Node objects contain information for the graph's nodes and
    methods that modify or operate on them.

    Attributes
    ----------
    edges : dict
        A dictionary mapping the destination node's index to the
        corresponding Edge object.
    index : int
        The node's unique numerical index.
    label : any
        An additional label for the node.
    """

    def __init__(self, index: int, label=None):
        self.index: int = index
        self.edges: dict = {}
        self.label = label

    def num_edges(self) -> int:
        """Returns the number of edges."""
        return len(self.edges)

    def get_edges(self, neighbor: int) -> Union[Edge, None]:
        """Returns an edge or None if no such edge exists.

        Parameters
        ----------
        neighbor : int
            The index of the destination node.

        Returns
        -------
        edge : Edge or None
            The Edge object linking the current node and the neighbor or
            None if no such edge exists.
        """
        if neighbor in self.edges:
            return self.edges[neighbor]

        return None

    def add_edge(self, neighbor: int, weight: float):
        """Add an edge to the graph.

        Parameters
        ----------
        neighbor : int
            The index of the neighboring node.
        weight : float
            The weight of the edge.
        """
        self.edges[neighbor] = Edge(self.index, neighbor, weight)

    def remove_edge(self, neighbor: int):
        """Remove an edge from the graph.

        Parameters
        ----------
        neighbor : int
            The index of the neighboring node.
        """
        if neighbor in self.edges:
            del self.edges[neighbor]

    def get_edge_list(self) -> list:
        """Return a list of all edges out of this node.

        Returns
        -------
        edges : list
            The edges in from this node.
        """
        return list(self.edges.values())

    def get_sorted_edge_list(self) -> list:
        """Return a list of all edges out of this node
        sorted by neighbor index.

        Returns
        -------
        edges : list
            The edges in from this node.
        """
        result = []
        neighbors = sorted(self.edges.keys())

        for n in neighbors:
            result.append(self.edges[n])

        return result

    def get_neighbors(self) -> set:
        """Return a set of the indices to all neighbors in the edge dictionary.
        For undirected graphs this includes all neighbors. For directed graphs,
        this only includes out-neighbors.

        Returns
        -------
        neighbors : set
            The indices to all neighbors in the edge dictionary.
        """
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)

        return neighbors

    def get_out_neighbors(self) -> set:
        """Return a set of the indices to all neighbors in the edge dictionary.
        For undirected graphs this includes all neighbors. For directed graphs,
        this only includes out-neighbors.

        Returns
        -------
        neighbors : set
            The indices to all neighbors in the edge dictionary.
        """
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)

        return neighbors
