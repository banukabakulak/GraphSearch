from Vertex import Vertex
from BreadthFirstSearch import BFS
from DepthFirstSearch import DFS

print("IE 436 Graph Search Algorithms...")

SIZE = 6
vertices = []

vertices.append(Vertex(1, [2, 3]))
vertices.append(Vertex(2, [3, 4, 5]))
vertices.append(Vertex(3, [4]))
vertices.append(Vertex(4, [6]))
vertices.append(Vertex(5, [4, 6]))
vertices.append(Vertex(6, []))

myBFS = BFS()
myBFS.ImplementBFS(vertices, 0)

myDFS = DFS()
myDFS.ImplementDFS(vertices, 0)
