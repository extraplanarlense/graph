from .base import GraphSerializer


class TGFSerializer(GraphSerializer):
    """Serializer for the Trivial Graph Format."""

    def __init__(self, node_label=None, edge_label=None):
        self.node_label = node_label
        self.edge_label = edge_label

    def iter_serialize(self, graph):
        """Serialize a graph, yielding parts of the result when available."""
        ids = dict()
        for id, node in enumerate(graph.nodes()):
            yield str(id) + " " + str(node.properties[self.node_label]) + "\n"
            ids[node] = id
        yield "#\n"
        for edge in graph.edges():
            yield (str(ids[edge.source]) + " " + str(ids[edge.target]) + " "
                   + str(edge.properties[self.edge_label]) + "\n")
