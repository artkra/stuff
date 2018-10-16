
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.pred = None
        self.color = 'white'
        self.distance = 0

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setPred(self, pred):
        self.pred = pred

    def setDistance(self, dist):
        self.distance = dist

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return str(self.id) + 'connected to ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo.get(nbr, None)


class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertDict[key] = newVertex
        return newVertex

    def getVertex(self, key):
        return self.vertDict.get(key, None)

    def __contains__(self, key):
        return key in self.vertDict

    def addEdge(self, f, t, cost=0):
        if f not in self.vertDict:
            nv = self.addVertex(f)
        if t not in self.vertDict:
            nv = self.addVertex(t)
        self.vertDict[f].addNeighbour(self.vertDict[t], cost)

    def getVertices(self):
        return self.vertDict.keys()

    def __iter__(self):
        return iter(self.vertDict.values())

    def bfs(self, start):
        start.setDistance(0)
        start.setPred(None)

        vertQueue = []
        vertQueue.append(start)

        while len(vertQueue) > 0:
            curVert = vertQueue.pop(0)
            
            for nbr in curVert.getConnections():
                if nbr.color == 'white':
                    nbr.setColor('grey')
                    nbr.setDistance(currentVert.distance + 1)
                    nbr.setPred(currentVert)
                    vertQueue.append(nbr)
            
            curVert.setColor('black')

if __name__ == '__main__':
    graph = Graph()

    for i in range(6):
        graph.addVertex(i)

    print(graph.vertDict)

    graph.addEdge(0, 1, 2)
    graph.addEdge(0, 3, 5)
    graph.addEdge(1, 2, 1)
    graph.addEdge(2, 3, 2)
    graph.addEdge(3, 4, 5)
    graph.addEdge(3, 5, 7)
    graph.addEdge(4, 1, 2)
    graph.addEdge(5, 3, 3)
    graph.addEdge(5, 0, 7)

    for v in graph:
        for c in v.getConnections():
            print('{}, {}'.format(v.getId(), c.getId()))