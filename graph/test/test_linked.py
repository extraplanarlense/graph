import unittest

from graph.linked import LinkedGraph

from .test_base import AbstractGraphTest


class LinkedGraphTest(AbstractGraphTest, unittest.TestCase):

    def setUp(self):
        self.graph = LinkedGraph()
        self.a = self.graph.add_node()
        self.b = self.graph.add_node()
        self.ab = self.graph.add_edge(self.a, self.b)
