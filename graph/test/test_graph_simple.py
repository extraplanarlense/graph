import unittest

from graph.simple import SimpleGraph

from .test_graph_base import AbstractGraphTest


class SimpleGraphTest(AbstractGraphTest, unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph()
        self.a = self.graph.add_node()
        self.b = self.graph.add_node()
        self.ab = self.graph.add_edge(self.a, self.b)
