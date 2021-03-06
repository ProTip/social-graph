import csv


class Graph:
    def __init__(self):
        self.nodes = []
        self.node_index = {}

    def add_node(self, postId, repostId, followers):
        if postId in self.node_index:
            raise NodeExists('Node already with postId [' + str(postId) + ']')

        node = Node(postId, repostId, followers)
        self.node_index[postId] = node
        # Attach to parent
        if (node.repostId > -1):
            parent = self.get_node_by_id(node.repostId)
            parent.add_child(node)

    def get_node_by_id(self, id):
        try:
            return self.node_index[id]
        except Exception:
            raise NodeDoesNotExist(
              'Node request for non-existent id [' +
              str(id) +
              ']')

    def viewer_total(self, id):
        total = [0]

        def addTotal(node):
            total[0] += node.followers

        self.traverse_from(id, addTotal)
        return total[0]

    def traverse_from(self, id, func):
        visited = set()
        startNode = self.get_node_by_id(id)
        stack = [startNode]
        while stack:
            node = stack.pop()
            stack += node.children
            func(node)


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


# Raised when trying to add duplicate nodes
class NodeExists(Exception):
    pass


# Raised when trying run aggregates or lookups on nodes that do not exist
class NodeDoesNotExist(Exception):
    pass
