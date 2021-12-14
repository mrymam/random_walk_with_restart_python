import numpy as np

class RWRGraph:

  def __init__(self, graph):
    self.graph = graph
    self.A = self.columnNormalize(graph)

  @staticmethod
  def columnNormalize(graph):
    return [column/sum(column) for column in graph]

  @staticmethod
  def genOneHotVec(length, target):
    v = np.zeros(length)
    v[target] = 1
    return v

  def rwr(self, startNode, c, iterateCount):
    graphLen = len(self.A)
    v = self.genOneHotVec(graphLen, startNode)
    u = v

    for _ in range(iterateCount):
      u = self.iterate(u, v, c)
      return u

  def iterate(self, u, v, c):
    u = (1-c) * np.dot(self.A, u) + c * v
    return u

  def rwrGeneraly(self, startNode, c):
    graphLen = len(self.A)
    v = self.genOneHotVec(graphLen, startNode)
    u = v

    E = np.eye(graphLen)

    inverse = np.linalg.inv(E + (c-1) * self.A)
    u = c * np.dot(inverse, v)
    return u
