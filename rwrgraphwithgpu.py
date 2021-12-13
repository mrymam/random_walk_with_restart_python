# import cupy as cp
# import numpy as np

# class RWRGraphWithGPU:

#   def __init__(self, graph):
#     super(self).__init__(graph)
#     self.A = cp.asarray(self.A)

#   def rwr(self, startNode, c, iterateCount):
#     graphLen = len(self.A)
#     v = self.genOneHotVec(graphLen, startNode)
#     v = cp.asarray(v)
#     u = v

#     for _ in range(iterateCount):
#       u = self.iterate(u, v, c)
#       return u

#   def iterate(self, u, v, c):
#     u = (1-c) * cp.dot(self.A, u) + c * v
#     return u
