from . import Graph, Edge, Node
import string
import random
from itertools import chain

class FasterGraph(Graph):

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    @property
    def properties(self):
        """Mapping of properties assigned to the graph."""
        raise NotImplementedError

    def __init__(self):
        self._nodes = {}
        self._edges = {}

    def nodes(self):
        """Make an iterable of all nodes in the graph."""
        return set(self._nodes.values())

    def edges(self):
        """Make an iterable of all edges in the graph."""
        return set(self._edges.values())

    def add_node(self, properties=None, **kwargs):
        """
        Returns the newly created node.
        """
        if properties is None:
            while True:
                random_name = self.id_generator()
                if random_name not in self._nodes:
                    break
            new_node = FasterNode(properties={'name': random_name}, **kwargs)
            self._nodes[random_name] = new_node
        else:
            new_node = FasterNode(properties, **kwargs)
            self._nodes[properties['name']] = new_node
        return new_node

    def remove_node(self, node):
        """Remove a given node from the graph."""
        if node in self.nodes():
            del self._nodes[node._properties['name']]
        else:
            raise RuntimeError

    def add_edge(self, source, target, properties=None, **kwargs):
        """Add an edge between two nodes."""
        new_edge = FasterEdge(source, target, properties={'name': source._properties['name'] + '-' + target._properties['name']})
        self._edges[source._properties['name'] + '-' + target._properties['name']] = new_edge
        source._outbound.append(new_edge)
        target._inbound.append(new_edge)
        return new_edge

    def remove_edge(self, edge):
        """Remove an edge from the graph."""
        if edge in self.edges():
            del self._edges[edge._properties['name']]
            self._nodes[edge._source._properties['name']]._outbound.remove(edge)
            self._nodes[edge._target._properties['name']]._inbound.remove(edge)
        else:
            raise RuntimeError


class FasterNode(Node):

    def __init__(self, properties=None, **kwargs):
        self._properties = properties
        self._inbound = []
        self._outbound = []

    @property
    def properties(self):
        """Mapping of properties assigned to the node."""
        return self._properties

    def inbound(self):
        """Make an iterable of all edges that end at the node."""
        return set(self._inbound)

    def outbound(self):
        """Make an iterable of all edges that start at the node."""
        return set(self._outbound)

    def edges(self):
        """Make an iterable of all edges that start or end at the node."""
        return chain(self._inbound.values(), self._outbound.values())


class FasterEdge(Edge):
    """Connection between two nodes."""

    def __init__(self, source, target, properties=None):
        self._source = source
        self._target = target
        self._properties = properties

    @property
    def properties(self):
        """Mapping of properties assigned to the edge."""
        return self._properties

    @property
    def target(self):
        """Return the node at which the edge ends."""
        return self._target

    @property
    def source(self):
        """Return the node at which the edge starts."""
        return self._source
