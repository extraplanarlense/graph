from abc import ABCMeta, abstractmethod


class Graph(metaclass=ABCMeta):

    @property
    @abstractmethod
    def properties(self):
        """Mapping of properties assigned to the graph."""
        raise NotImplementedError

    @abstractmethod
    def nodes(self):
        """Make a set of all nodes in the graph."""
        raise NotImplementedError

    @abstractmethod
    def edges(self):
        """Make a set of all edges in the graph."""
        raise NotImplementedError

    @abstractmethod
    def add_node(self, properties=None, **kwargs):
        """Add a node to the graph.

        The new node can be assigned properties via the mapping *properties* or
        keyword arguments.

        Returns the newly created node.
        """
        raise NotImplementedError

    @abstractmethod
    def remove_node(self, node):
        """Remove a given node from the graph."""
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, source, target, properties=None, **kwargs):
        """Add an edge between two nodes.

        The new edge can be assigned properties via the mapping *properties* or
        keyword arguments.

        Returns the newly created edge.
        """
        raise NotImplementedError

    @abstractmethod
    def remove_edge(self, edge):
        """Remove an edge from the graph."""
        raise NotImplementedError


class Node(metaclass=ABCMeta):

    @property
    @abstractmethod
    def properties(self):
        """Mapping of properties assigned to the node."""
        raise NotImplementedError

    @abstractmethod
    def inbound(self):
        """Make a set of all edges that end at the node."""
        raise NotImplementedError

    @abstractmethod
    def outbound(self):
        """Make a set of all edges that start at the node."""
        raise NotImplementedError

    @abstractmethod
    def edges(self):
        """Make a set of all edges that start or end at the node."""
        raise NotImplementedError


class Edge(metaclass=ABCMeta):
    """Connection between two nodes."""

    @property
    @abstractmethod
    def properties(self):
        """Mapping of properties assigned to the edge."""
        raise NotImplementedError

    @property
    @abstractmethod
    def target(self):
        """Return the node at which the edge ends."""
        raise NotImplementedError

    @property
    @abstractmethod
    def source(self):
        """Return the node at which the edge starts."""
        raise NotImplementedError
