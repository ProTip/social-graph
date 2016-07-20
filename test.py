import unittest
import social

class TestArrayDiff(unittest.TestCase):

  def test_reference_input(self):
    graph = social.GraphFactory.FromCsv('graph.csv')
    oneFollowers = graph.viewer_total(1)
    self.assertEqual(oneFollowers, 350)
    sevenFollowers = graph.viewer_total(7)
    self.assertEqual(sevenFollowers, 480)

  def test_duplicate_post_id_throws(self):
    graph = social.Graph()
    graph.add_node(1,-1,0)
    self.assertRaises(social.NodeExists, graph.add_node, 1, 2, 0)

  def test_lookup_missing_node_throws(self):
    graph = social.Graph()
    graph.add_node(1,-1,0)
    self.assertRaises(social.NodeDoesNotExist, graph.get_node_by_id, 100)

  def test_request_total_on_missing_node_throws(self):
    graph = social.Graph()
    graph.add_node(1,-1,0)
    self.assertRaises(social.NodeDoesNotExist, graph.viewer_total, 100)

  def test_add_node_throws_on_missing_parent(self):
    graph = social.Graph()
    graph.add_node(1,-1,0)
    self.assertRaises(social.NodeDoesNotExist, graph.add_node, 2, 5, 0)

unittest.main()