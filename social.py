import csv

class Graph:
  def __init__(self):
    self.nodes = []
    self.node_index = {}

  def add_node(self, postId, repostId, followers):
    node = Node(postId, repostId, followers)
    self.node_index[postId] = node
    # Attach to parent
    if (node.repostId > -1):
      parent = self.node_index[node.repostId]
      parent.add_child(node)

  def print_nodes(self):
    print(self.node_index)
    print(self.nodes)

  def get_node_by_id(self, id):
    return self.node_index[id]

  def viewer_total(self, id):
    visited = set()
    stack = []

    startNode = self.node_index[id]
    total = startNode.followers
    stack += startNode.children
    while stack:
      node = stack.pop()
      total += node.followers
      stack += node.children
    return total

class Node:
  def __init__(self, postId, repostId, followers):
    self.children = []

    self.postId = postId
    self.repostId = repostId
    self.followers = followers

  def add_child(self, node):
    node.add_parent(self)
    self.children.append(node)

  def add_parent(self, node):
    self.parent = node


class GraphFactory:
  @staticmethod
  def FromCsv(file):
    graph = Graph()
    with open(file, 'rb') as csvfile:
      graphReader = csv.reader(csvfile)
      graphReader.next()
      for row in graphReader:
        postId = int(row[0])
        repostId = int(row[1])
        followers = int(row[2])

        graph.add_node(postId, repostId, followers)
    return graph