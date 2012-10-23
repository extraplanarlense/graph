from collections import defaultdict
import uuid, random
import logging

from . import Graph, Node, Edge


class SimpleGraph(Graph):

    def __init__(self):
        self._properties = dict()

        self._edges = dict()
        self._edge_properties = defaultdict(dict)

        self._nodes = set()
        self._node_properties = defaultdict(dict)

        self._edges_inbound = defaultdict(set)
        self._edges_outbound = defaultdict(set)

    @property
    def properties(self):
        return self._properties

    def nodes(self):
        return set(SimpleNode(self, id) for id in self._nodes)

    def edges(self):
        return set(SimpleEdge(self, id) for id in self._edges)

    def add_node(self, properties=None, **kwargs):
        while True:
            newid = random.randrange(1000)
            if newid not in self._nodes:
                break
        self._nodes.add(newid)
        return SimpleNode(self, newid)

    def remove_node(self, node):
        id = node._id

        for edge_id in self._edges_inbound[id]:
            del self._edges[edge_id]
        try:
            del self._edges_inbound[id]
        except KeyError:
            pass

        for edge_id in self._edges_outbound[id]:
            try:
                # Might have been removed in first loop.
                del self._edges[edge_id]
            except KeyError:
                pass
        try:
            del self._edges_outbound[id]
        except KeyError:
            pass

        self._nodes.remove(id)

    def add_edge(self, source, target, properties=None, **kwargs):
        source_id = source._id
        target_id = target._id
        while True:
            newid = random.randrange(1000)
            if newid not in self._edges:
                break
        self._edges[newid] = source_id, target_id
        self._edges_inbound[target_id].add(newid)
        self._edges_outbound[source_id].add(newid)
        return SimpleEdge(self, newid)

    def remove_edge(self, edge):
        oldid = edge._id
        source, target = self._edges[oldid]
        self._edges_inbound[target].remove(oldid)
        self._edges_outbound[source].remove(oldid)
        del self._edges[oldid]


class SimpleNode(Node):

    def __init__(self, graph, id):
        self._graph = graph
        self._id = id

    @property
    def properties(self):
        """Mapping of properties assigned to the node."""
        return {}

    def inbound(self):
        """Make an iterable of all edges that end at the node."""
        return set(SimpleEdge(self._graph, id)
                   for id in self._graph._edges_inbound[self._id])

    def outbound(self):
        """Make an iterable of all edges that start at the node."""
        return set(SimpleEdge(self._graph, id)
                   for id in self._graph._edges_outbound[self._id])

    def edges(self):
        """Make an iterable of all edges that start or end at the node."""
        return self.inbound() | self.outbound()

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return other._graph == self._graph and other._id == self._id

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "<SimpleNode id={0!r}>".format(self._id)


class SimpleEdge(Edge):
    """Connection between two nodes."""

    def __init__(self, graph, id):
        self._graph = graph
        self._id = id

    @property
    def properties(self):
        """Mapping of properties assigned to the edge."""
        return {}

    @property
    def target(self):
        """Return the node at which the edge ends."""
        return SimpleNode(self._graph, self._graph._edges[self._id][1])

    @property
    def source(self):
        """Return the node at which the edge starts."""
        return SimpleNode(self._graph, self._graph._edges[self._id][0])

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return other._graph == self._graph and other._id == self._id

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "<SimpleEdge id={0!r}>".format(self._id)
