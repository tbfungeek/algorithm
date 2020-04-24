class Graphic(object):

    def __init__(self):
        self.node_and_neighbors = {}
    
    def add_node(self,node):
        if node not in self.node_and_neighbors.keys():
            self.node_and_neighbors[node] = []
    
    def add_edge(self,start,end):
        if start == end:
            return
        if (start not in self.node_and_neighbors[end]) and (end not in self.node_and_neighbors[start]):
            self.node_and_neighbors[start].append(end)
            self.node_and_neighbors[end].append(start)

    def DFS(self,travel_start):
        if travel_start not in self.node_and_neighbors.keys():
            return
        stack = []
        stack.append(travel_start)
        visited = set()
        visited.add(travel_start)
        while len(stack) > 0:
            vex = stack.pop()
            nodes = self.node_and_neighbors[vex]
            for node in nodes:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)
            print(vex)

    def BFS(self,travel_start):
        if travel_start not in self.node_and_neighbors.keys():
            return
        queue = []
        queue.append(travel_start)
        visited = set()
        visited.add(travel_start)
        while len(queue) > 0:
            vex = queue.pop(0)
            nodes = self.node_and_neighbors[vex]
            for node in nodes:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
            print(vex)
    
if __name__ == '__main__':

    g = Graphic()
    for i in range(1,9):
        g.add_node(i)

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 8)
    g.add_edge(5, 8)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(6, 7)

    g.DFS(1)

    print("=====>")

    g.BFS(1)
            