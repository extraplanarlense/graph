class Graph:

    @property
    def properties(self):
        """Mapping of properties assigned to the graph."""
        raise NotImplementedError

    def nodes(self):
        """Make a set of all nodes in the graph."""
        raise NotImplementedError

    def edges(self):
        """Make a set of all edges in the graph."""
        raise NotImplementedError

    def add_node(self, properties=None, **kwargs):
        """Add a node to the graph.

        The new node can be assigned properties via the mapping *properties* or
        keyword arguments.

        Returns the newly created node.
        """
        raise NotImplementedError

    def remove_node(self, node):
        """Remove a given node from the graph."""
        raise NotImplementedError

    def add_edge(self, source, target, properties=None, **kwargs):
        """Add an edge between two nodes.

        The new edge can be assigned properties via the mapping *properties* or
        keyword arguments.

        Returns the newly created edge.
        """
        raise NotImplementedError

    def remove_edge(self, edge):
        """Remove an edge from the graph."""
        raise NotImplementedError


class Node:

    @property
    def properties(self):
        """Mapping of properties assigned to the node."""
        raise NotImplementedError

    def inbound(self):
        """Make a set of all edges that end at the node."""
        raise NotImplementedError

    def outbound(self):
        """Make a set of all edges that start at the node."""
        raise NotImplementedError

    def edges(self):
        """Make a set of all edges that start or end at the node."""
        raise NotImplementedError


class Edge:
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
