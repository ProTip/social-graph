import csv
import sys
from social import Graph, GraphFactory

def main():
  graph = GraphFactory.FromCsv('graph.csv')

  postId = int(sys.stdin.readline().rstrip())
  total = graph.viewer_total(postId)
  print "%s: %s" % (postId,total)

main()