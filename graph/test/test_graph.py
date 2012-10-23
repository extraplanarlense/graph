import unittest

from graph import Edge, Node, Graph


class GraphTest(unittest.TestCase):

    def test_add_node(self):
        self.graph.add_node()

    def test_remove_node(self):
        self.graph.remove_node(self.a)

    def test_add_edge(self):
        edge = self.graph.add_edge(self.a, self.b)
        self.assertIsInstance(edge, Edge)
        self.assertEqual(edge.source, self.a)
        self.assertEqual(edge.target, self.b)

    def test_remove_edge(self):
        pass