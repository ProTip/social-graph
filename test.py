import unittest
from social import GraphFactory

class TestArrayDiff(unittest.TestCase):

  def test_reference_input(self):
    graph = GraphFactory.FromCsv('graph.csv')
    oneFollowers = graph.viewer_total(1)
    self.assertEqual(oneFollowers, 350)
    sevenFollowers = graph.viewer_total(7)
    self.assertEqual(sevenFollowers, 480)

unittest.main()