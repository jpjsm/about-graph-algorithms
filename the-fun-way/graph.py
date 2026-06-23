from typing import Union

import graphviz

from edge import Edge
from node import Node


class Graph:
    """Adjacency list representations of a graph structure.

    Attributes
    ----------
    nodes : list
        A list of Node objects, one for each node in the graph.
    node_indices : dict
        A dictionary mapping the a string (the node's name) to its index.
    num_nodes : int
        The total number of nodes in the graph.
    undirected : bool
        A Boolean indicating whether the graph is undirected (True) or
        directed (False).
    """

    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(j) for j in range(num_nodes)]
        self.node_indices: dict = {}

    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, None]:
        """Lookup an edge in the graph.

        Parameters
        ----------
        from_node : int
            The node index of the edge's origin.
        to_node : int
            The node index to the edge's destination.

        Returns
        -------
        edge : Edge or None
            The corresponding Edge object if an edge exists or None
            if no such edge exists.
        """
        if not (0 <= from_node < self.num_nodes):
            raise IndexError("'from_node' out of bounds")

        if not (0 <= to_node < self.num_nodes):
            raise IndexError("'to_node' out of bounds")

        return self.nodes[from_node].get_edge(to_node)

    def is_edge(self, from_node: int, to_node: int) -> bool:
        """Check if an edge is in the graph.

        Parameters
        ----------
        from_node : int
            The node index of the edge's origin.
        to_node : int
            The node index to the edge's destination.

        Returns
        -------
        result : bool
            True if the graph contains an edge from from_node to to_node
            and False otherwise.
        """
        return self.get_edge(from_node, to_node) is not None

    def make_edge_list(self) -> list:
        """Return a list containing all edges in the graph.

        Returns
        -------
        all_edges : list
            A list of Edge objects containing all edges in the graph.
        """
        all_edges: list = []
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)

        return all_edges

    def insert_edge(self, from_node: int, to_node: int, weight: float):
        if not (0 <= from_node < self.num_nodes):
            raise IndexError("'from_node' out of bounds")

        if not (0 <= to_node < self.num_nodes):
            raise IndexError("'to_node' out of bounds")

        self.nodes[from_node].add_edge(to_node, weight)
        if self.undirected:
            self.nodes[to_node].add_edge(from_node, weight)

    def remove_edge(self, from_node: int, to_node: int):
        if not (0 <= from_node < self.num_nodes):
            raise IndexError("'from_node' out of bounds")

        if not (0 <= to_node < self.num_nodes):
            raise IndexError("'to_node' out of bounds")

        self.nodes[from_node].remove_edge(to_node)
        if self.undirected:
            self.nodes[to_node].remove_edge(from_node)

    def insert_node(self, label=None) -> Node:
        new_node: Node = Node(self.num_nodes, label=label)
        self.nodes.append(new_node)
        self.num_nodes += 1
        return new_node

    def make_copy(self):
        g2: Graph = Graph(self.num_nodes, undirected=self.undirected)

        for node in self.nodes:
            g2.nodes[node.index].label = node.label
            for edge in node.edges.values():
                g2.insert_edge(edge.from_node, edge.to_node, edge.weight)

        return g2

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
        neighbors: set = set()
        for node in self.nodes:
            if target in node.edges:
                neighbors.add(node.index)

        return neighbors

    # Following definitions aren't in the book or author's book repo!

    # Having added Graphviz to visualize graphs, the following function
    # creates a graphic representation of the graph

    def make_graphviz_vizualization(self):
        edges = []
        grph = graphviz.Digraph(format="png")
        grph.attr("graph", rankdir="LR", rank="source")
        grph.attr("node", shape="doublecircle")
        for node_ in self.nodes:
            grph.node(str(node_.index), label=node_.label)
            edges += node_.edges.values()

        for edge_ in edges:
            grph.edge(str(edge_.from_node), str(edge_.to_node), label=str(edge_.weight))

        grph.view()


if __name__ == "__main__":
    g: Graph = Graph(5, undirected=False)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 3.0)

    g.insert_edge(1, 2, 2.0)
    g.insert_edge(1, 4, 1.0)

    g.insert_edge(3, 4, 3.0)

    g.insert_edge(4, 2, 3.0)
    g.insert_edge(4, 3, 3.0)

    g.make_graphviz_vizualization()

    print("Test completed !!")
