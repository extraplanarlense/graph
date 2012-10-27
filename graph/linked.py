from .base import Graph, Edge, Node


class LinkedGraph(Graph):
    """Graph implementation that relies on sets of edges, kept in its nodes."""

    def __init__(self, properties=None, **kwargs):
        self._properties = dict()
        if properties:
            self._properties.update(properties)
        self._properties.update(kwargs)
        self._edges = set()
        self._nodes = set()

    @property
    def properties(self):
        return self._properties

    def edges(self):
        return self._edges

    def nodes(self):
        return self._nodes

    def add_node(self, properties=None, **kwargs):
        node = LinkedNode(properties, **kwargs)
        self._nodes.add(node)
        return node

    def remove_node(self, node):
        if node in self._nodes:
            for edge in node.edges():
                self.remove_edge(edge)
            self._nodes.remove(node)
        else:
            raise ValueError("node is not part of the graph: {0}".format(node))

    def add_edge(self, source, target, properties=None, **kwargs):
        if source in self._nodes and target in self._nodes:
            edge = LinkedEdge(source, target, properties, **kwargs)
            source._outbound.add(edge)
            target._inbound.add(edge)
            self._edges.add(edge)
            return edge
        else:
            raise ValueError("source and target are not both part of the "
                             "graph: {0}, {1}".format(source, target))

    def remove_edge(self, edge):
        if edge in self._edges:
            edge.source._outbound.remove(edge)
            edge.target._inbound.remove(edge)
            self._edges.remove(edge)
        else:
            raise ValueError("edge is not part of the graph: {0}".format(edge))


class LinkedNode(Node):

    def __init__(self, properties=None, **kwargs):
        self._properties = dict()
        if properties:
            self._properties.update(properties)
        self._properties.update(kwargs)

        self._inbound = set()
        self._outbound = set()

    @property
    def properties(self):
        return self._properties

    def inbound(self):
        return self._inbound

    def outbound(self):
        return self._outbound

    def edges(self):
        return self._inbound | self._outbound


class LinkedEdge(Edge):

    def __init__(self, source, target, properties=None, **kwargs):
        self._properties = dict()
        if properties:
            self._properties.update(properties)
        self._properties.update(kwargs)

        self._source = source
        self._target = target

    @property
    def properties(self):
        return self._properties

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target
