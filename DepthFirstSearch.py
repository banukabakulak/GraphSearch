from Vertex import Vertex

class DFS:

    def ImplementDFS(self, vertices, s):

        n = len(vertices)
        for i in range(n):
            vertices[i].isMarked = False;

        LIST = []
        LIST.append(s);
        vertices[0].order = 1;
        vertices[0].isMarked = True;
        next = 1;

        while len(LIST) != 0:

            currVertex = LIST[-1]
            isAdmissible = False;

            for i in range(len(vertices[currVertex].adj)):
                currNeighbor = vertices[currVertex].adj[i] -1

                if not vertices[currNeighbor].isMarked:
                    vertices[currNeighbor].isMarked = True
                    vertices[currNeighbor].pred = currVertex
                    next = next + 1
                    vertices[currNeighbor].order = next
                    LIST.append(currNeighbor)
                    isAdmissible = True
                    break

            if not isAdmissible:
                del LIST[-1]

        print()
        print("The orders in DFS")
        for i in range(n):
            print(f"The (order, pred) of vertex {i + 1} is ({vertices[i].order}, {vertices[i].pred + 1})")
