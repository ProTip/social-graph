import csv
import sys
from social import Graph, GraphFactory, NodeDoesNotExist


def main():
    graph = GraphFactory.FromCsv('graph.csv')

    postId = int(sys.stdin.readline().rstrip())
    try:
        total = graph.viewer_total(postId)
    except NodeDoesNotExist:
        sys.stderr.write(
          'Post with id of [' +
          str(postId) +
          '] was not found in the graph!\n')
        exit(1)
    print "%s: %s" % (postId, total)

main()
