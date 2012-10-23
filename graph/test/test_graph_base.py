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
        self.assertSetEqual(set(self.graph.nodes()), set((self.a, self.b)))

    def test_edges(self):
        self.assertSetEqual(set(self.graph.edges()), set((self.ab,)))

    def test_inbound(self):
        self.assertSetEqual(set(self.b.inbound()), set(self.ab))

    def test_outbound(self):
        self.assertSetEqual(set(self.a.outbound()), set(self.ab))

    def test_source(self):
        self.assertEqual(self.ab.source, self.a)

    def test_target(self):
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
        self.assertEqual(edge.source, self.a)
        self.assertEqual(edge.target, self.b)
        self.assertIn(edge, self.graph.edges())
        self.assertIn(edge, self.a.inbound())
        self.assertIn(edge, self.b.outbound())

    def test_remove_edge(self):
        self.graph.remove_edge(self.ab)
        self.assertNotIn(self.ab, self.graph.edges())
        self.assertNotIn(self.ab, self.a.outbound())
        self.assertNotIn(self.ab, self.b.inbound())
