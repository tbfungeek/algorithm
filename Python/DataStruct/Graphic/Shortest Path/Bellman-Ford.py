#from https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
import sys
class Graph(object):  
  
    def __init__(self):  
        self.edges = []  
        self.vertexs = []
  
    def add_edge(self, start, end, weight):  
        #添加边数据
        self.edges.append([start, end, weight]) 
        #如果还没存储过则添加到结点数组中
        if start not in self.vertexs:
            self.vertexs.append(start)
        if end not in self.vertexs:
            self.vertexs.append(end) 

    def BellmanFord(self, start_point):  

        dist = {}
        if len(self.vertexs) == 0 or start_point not in self.vertexs:
            return (False, dist)

        for v in self.vertexs:
            dist[v] = sys.maxsize
        
        dist[start_point] = 0
  
        for _ in range(len(self.vertexs) - 1):

            for start, end, weight in self.edges:  
                if dist[start] != sys.maxsize and dist[start] + weight < dist[end]:  
                        dist[end] = dist[start] + weight 
  
        for start, end, weight in self.edges:  
                if dist[start] != sys.maxsize and dist[start] + weight < dist[end]:  
                    return (True, dist)
                          
        return (False, dist)

if __name__ == "__main__":
    g = Graph()  
    g.add_edge(0, 1, -1)  
    g.add_edge(0, 2, 4)  
    g.add_edge(1, 2, 3)  
    g.add_edge(1, 3, 2)  
    g.add_edge(1, 4, 2)  
    g.add_edge(3, 2, 5)  
    g.add_edge(3, 1, 1)  
    g.add_edge(4, 3, -3)     
  
    print(g.BellmanFord(0))