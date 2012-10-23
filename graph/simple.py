from . import Graph, Node, Edge


class SimpleGraph(Graph):

    @property
    def properties(self):
        """Mapping of properties assigned to the graph."""
        raise NotImplementedError

    def nodes(self):
        """Make an iterable of all nodes in the graph."""
        raise NotImplementedError

    def edges(self):
        """Make an iterable of all edges in the graph."""
        raise NotImplementedError

    def add_node(self):
        """Add a node to the graph.

        Returns the newly created node.
        """
        raise NotImplementedError

    def remove_node(self, node):
        """Remove a given node from the graph."""
        raise NotImplementedError

    def add_edge(self, source, target):
        """Add an edge between two nodes."""
        raise NotImplementedError

    def remove_edge(self, edge):
        """Remove an edge from the graph."""
        raise NotImplementedError


class SimpleNode(Node):

    @property
    def properties(self):
        """Mapping of properties assigned to the node."""
        raise NotImplementedError

    def inbound(self):
        """Make an iterable of all edges that end at the node."""
        raise NotImplementedError

    def outbound(self):
        """Make an iterable of all edges that start at the node."""
        raise NotImplementedError

    def edges(self):
        """Make an iterable of all edges that start or end at the node."""
        raise NotImplementedError


class SimpleEdge(Edge):
    """Connection between two nodes."""

    @property
    def properties(self):
        """Mapping of properties assigned to the edge."""
        raise NotImplementedError

    @property
    def target(self):
        """Return the node at which the edge ends."""
        raise NotImplementedError

    @property
    def source(self):
        """Return the node at which the edge starts."""
        raise NotImplementedError
