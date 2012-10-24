from . import Graph, Edge, Node
import string
import random
import uuid
from itertools import chain

class FasterGraph(Graph):


    @property
    def properties(self):
        """Mapping of properties assigned to the graph."""
        return self._properties

    def __init__(self):
        self._nodes = {}
        self._edges = {}
        self._properties = {}

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
        while True:
            random_id = uuid.uuid4()
            if random_id not in self._nodes:
                break
        new_node = FasterNode(random_id, properties, **kwargs)
        self._nodes[random_id] = new_node
        return new_node

    def remove_node(self, node):
        """Remove a given node from the graph."""
        if node in self.nodes():
            for inedge in node._inbound:
                print('a')
                self.remove_edge(inedge)
            for outedge in node._outbound:
                print('b')
                self.remove_edge(outedge)
            del self._nodes[node.id]
        else:
            raise RuntimeError

    def add_edge(self, source, target, properties=None, **kwargs):
        """Add an edge between two nodes."""
        while True:
                random_id = uuid.uuid4()
                if random_id not in self._nodes:
                    break
        new_edge = FasterEdge(random_id, source, target, properties, **kwargs)
        self._edges[random_id] = new_edge
        source._outbound.append(new_edge)
        target._inbound.append(new_edge)
        return new_edge

    def remove_edge(self, edge):
        """Remove an edge from the graph."""
        if edge in self.edges():
            self._nodes[edge.target.id]._inbound.remove(edge)
            self._nodes[edge.source.id]._outbound.remove(edge)
            del self._edges[edge.id]
        else:
            raise RuntimeError


class FasterNode(Node):

    def __init__(self, id, properties=None, **kwargs):
        if properties is None:
            self._properties = {}
            self._properties.update(kwargs)
        else:
            self._properties = properties.copy()
            self._properties.update(kwargs)
        self._inbound = []
        self._outbound = []
        self.id = id

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
        return chain(self._inbound, self._outbound)


class FasterEdge(Edge):
    """Connection between two nodes."""

    def __init__(self,id, source, target, properties=None, **kwargs):
        if properties is None:
            self._properties = {}
            self._properties.update(kwargs)
        else:
            self._properties = properties.copy()
            self._properties.update(kwargs)
        self._source = source
        self._target = target
        self.id = id

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
