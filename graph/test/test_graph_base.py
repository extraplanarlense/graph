from collections import Set, Mapping

from graph import Edge, Node, Graph


class AbstractGraphTest:
    """Setup must create a graph self.graph with two nodes self.a and self.b,
    connected by an loop self.ab from a to b."""

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

    def test_node_edges(self):
        self.assertIsInstance(self.a.edges(), Set)
        self.assertIn(self.ab, self.a.edges())
        self.assertIn(self.ab, self.b.edges())
        self.assertSetEqual(self.a.edges(), self.b.edges())
        self.assertSetEqual(self.a.edges(), set((self.ab, )))

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
        self.assertNotIn(self.ab, self.graph.edges())
        self.assertNotIn(self.ab, self.b.inbound())
        self.assertSetEqual(self.graph.edges(), set())
        self.assertSetEqual(self.graph.nodes(), set((self.b,)))

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

    def test_add_edge_loop(self):
        loop = self.graph.add_edge(self.a, self.a)
        self.assertIsInstance(loop, Edge)
        self.assertEqual(loop.source, self.a)
        self.assertEqual(loop.target, self.a)
        self.assertIn(loop, self.graph.edges())
        self.assertIn(loop, self.a.inbound())
        self.assertIn(loop, self.a.outbound())

    def test_remove_edge_loop(self):
        loop = self.graph.add_edge(self.a, self.a)
        self.graph.remove_edge(loop)
        self.assertNotIn(loop, self.a.inbound())
        self.assertNotIn(loop, self.a.outbound())
        self.assertNotIn(loop, self.graph.edges())

    def test_add_edge_duplicate(self):
        dup = self.graph.add_edge(self.a, self.b)
        self.assertIsInstance(dup, Edge)
        self.assertEqual(dup.source, self.a)
        self.assertEqual(dup.target, self.b)
        self.assertIn(dup, self.graph.edges())
        self.assertIn(dup, self.b.inbound())
        self.assertIn(dup, self.a.outbound())
        self.assertNotEqual(dup, self.ab)

    def test_remove_edge_duplicate(self):
        dup = self.graph.add_edge(self.a, self.b)
        self.graph.remove_edge(dup)
        self.assertNotIn(dup, self.graph.edges())
        self.assertNotIn(dup, self.a.outbound())
        self.assertNotIn(dup, self.b.inbound())
        self.assertIn(self.ab, self.graph.edges())
        self.assertIn(self.ab, self.a.outbound())
        self.assertIn(self.ab, self.b.inbound())

    def test_graph_properties_mapping(self):
        self.assertIsInstance(self.graph.properties, Mapping)

    def test_node_properties_mapping(self):
        self.assertIsInstance(self.a.properties, Mapping)
        self.assertIsInstance(self.b.properties, Mapping)

    def test_edge_properties_mapping(self):
        self.assertIsInstance(self.ab.properties, Mapping)

    def test_graph_set_property(self):
        self.graph.properties["foo"] = "bar"
        self.assertEqual(self.graph.properties["foo"], "bar")

    def test_node_set_property(self):
        self.a.properties["foo"] = "bar"
        self.assertEqual(self.a.properties["foo"], "bar")

    def test_edge_set_property(self):
        self.ab.properties["foo"] = "bar"
        self.assertEqual(self.ab.properties["foo"], "bar")

    def test_add_node_with_properties(self):
        c = self.graph.add_node({"foo": "bar"}, bar="foo")
        self.assertEqual(c.properties["foo"], "bar")
        self.assertEqual(c.properties["bar"], "foo")
        self.assertSetEqual(set(c.properties.items()),
                            set({"foo": "bar", "bar": "foo"}.items()))

    def test_add_edge_with_properties(self):
        c = self.graph.add_edge(self.b, self.a, {"foo": "bar"}, bar="foo")
        self.assertEqual(c.properties["foo"], "bar")
        self.assertEqual(c.properties["bar"], "foo")
        self.assertSetEqual(set(c.properties.items()),
                            set({"foo": "bar", "bar": "foo"}.items()))
