class Edge:
    """Edge objects are containers to store information about graph edges.

    Attributes
    ----------
    from_node : int
        The node index of the edge's origin.
    to_node : int
        The node index to the edge's destination.
    weight : float
        The weight of the edge.
    """

    def __init__(self, from_node: int, to_node: int, weight: float = 0.0) -> None:
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight

    def print_edge(self):
        """Display the edge information in a human readable form."""
        print(f"{self.from_node} -> {self.to_node} = {self.weight}")

    # Following definitions aren't in the book or author's book repo!
    # Added to make Edges comparable and Hashables

    def __eq__(self, other) -> bool:
        if not isinstance(other, Edge):
            return False

        return self.to_node == other.to_node and self.from_node == other.from_node

    def __hash__(self) -> int:
        return hash((self.from_node, self.to_node))

    @property
    def edge_id(self) -> tuple:
        return (self.from_node, self.to_node)
