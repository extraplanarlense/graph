from collections import Set

from graph import Edge, Node, Graph


class AbstractGraphTest:
    """Setup must create a graph self.graph with two nodes self.a and self.b,
    connected by an edge self.ab from a to b."""

    def test_init(self):
        self.assertIsInstance(self.graph, Graph)
        self.assertIsInstance(self.a, Node)
        self.assertIsInstance(self.b, Node)
        self.assertIsInstance(self.ab, Edge)

    def test_nodes(self):
        self.assertIsInstance(self.graph.edges(), Set)
        self.assertSetEqual(self.graph.nodes(), set((self.a, self.b)))

    def test_edges(self):
        self.assertIsInstance(self.graph.edges(), Set)
        self.assertSetEqual(self.graph.edges(), set((self.ab,)))

    def test_inbound(self):
        self.assertIsInstance(self.a.inbound(), Set)
        self.assertIsInstance(self.b.inbound(), Set)
        self.assertSetEqual(self.b.inbound(), set((self.ab,)))
        for item in self.a.inbound():
            self.assertIsInstance(item, Edge)

    def test_outbound(self):
        self.assertIsInstance(self.a.outbound(), Set)
        self.assertIsInstance(self.b.outbound(), Set)
        self.assertSetEqual(self.a.outbound(), set((self.ab,)))
        for item in self.a.outbound():
            self.assertIsInstance(item, Edge)

    def test_source(self):
        self.assertIsInstance(self.ab.target, Node)
        self.assertEqual(self.ab.source, self.a)

    def test_target(self):
        self.assertIsInstance(self.ab.target, Node)
        self.assertEqual(self.ab.target, self.b)

    def test_add_node(self):
        c = self.graph.add_node()
        self.assertIsInstance(c, Node)
        self.assertIn(c, self.graph.nodes())

    def test_remove_node(self):
        self.graph.remove_node(self.a)
        self.assertNotIn(self.a, self.graph.nodes())

    def test_add_edge(self):
        edge = self.graph.add_edge(self.b, self.a)
        self.assertIsInstance(edge, Edge)
        self.assertEqual(edge.source, self.b)
        self.assertEqual(edge.target, self.a)
        self.assertIn(edge, self.graph.edges())
        self.assertIn(edge, self.a.inbound())
        self.assertIn(edge, self.b.outbound())

    def test_remove_edge(self):
        self.graph.remove_edge(self.ab)
        self.assertNotIn(self.ab, self.graph.edges())
        self.assertNotIn(self.ab, self.a.outbound())
        self.assertNotIn(self.ab, self.b.inbound())
