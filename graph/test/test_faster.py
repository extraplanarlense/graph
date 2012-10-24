import unittest

from graph.faster import FasterGraph

from .test_base import AbstractGraphTest


class FasterGraphTest(AbstractGraphTest, unittest.TestCase):

    def setUp(self):
        self.graph = FasterGraph()
        self.a = self.graph.add_node()
        self.b = self.graph.add_node()
        self.ab = self.graph.add_edge(self.a, self.b)
