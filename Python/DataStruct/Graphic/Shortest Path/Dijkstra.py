import sys
#优先队列
import heapq

class Vertex(object):
    
    def __init__(self, value):
        #当前结点的值
        self.value = value
        #当前结点的邻结点
        self.adjacent = {}
        #当前结点距离起始点的距离
        self.distance = sys.maxsize
        #当前结点是否已经访问过
        self.visited = False
        #在最短路径中当前结点路过的前一个结点
        self.previous = None
    
    def add_neighbor(self,neghbor,weight = 0):
        self.adjacent[neghbor] = weight
    
    def weight_of_neighbor(self,neighbor):
        return self.adjacent[neighbor]

    def __lt__(self,other):
        return self.distance < other.distance

    def __gt__(self,other):
        return self.distance > other.distance
    
    def __str__(self):
        return str(self.value) + ' adjacent: ' + str([x.value for x in self.adjacent])
    

class Graphic(object):
    def __init__(self):

        #vex_dict {key:node_value value: node}
        self.vex_dict = {}
        self.previous = None
    
    def __iter__(self):
        return iter(self.vex_dict.values())
    
    def add_vertex(self,value):
        new_vex = Vertex(value)
        self.vex_dict[value] = new_vex
        return new_vex
    
    def add_edge(self,start,end,weight):

        if start not in self.vex_dict.keys():
            self.add_vertex(start)

        if end not in self.vex_dict.keys():
            self.add_vertex(end)
        
        self.vex_dict[start].add_neighbor(self.vex_dict[end],weight)
        self.vex_dict[end].add_neighbor(self.vex_dict[start],weight)

    def vertexs(self):
        return self.vex_dict.values()


    def dijkstra(self,start_value,target_value):

        #如果起点和终点没有在该图中则直接返回
        if start_value not in self.vex_dict.keys() or target_value not in self.vex_dict.keys():
            return []
        
        #获取起点
        start_vex = self.vex_dict[start_value]
        #设置起点的距离为0
        start_vex.distance = 0
        #将未访问的结点添加到队列中
        unvisited_vex_queue = list(self.vertexs())
        #通过 heapify() ，来把unvisited_vex_queue转换成堆
        heapq.heapify(unvisited_vex_queue)

        #遍历所有未访问的点
        while len(unvisited_vex_queue):
            #取出一个未访问的点中distance最小的vex
            current = heapq.heappop(unvisited_vex_queue)
            #将结点标记为已访问
            current.visited = True

            #到达终点，构建最短路径，并返回
            if current.value == target_value:
                shortest_path = [current]
                while current.previous.value != start_value:
                    shortest_path.insert(0,current.previous)
                    current = current.previous
                
                shortest_path.insert(0,start_vex)
                return shortest_path

            #计算和当前结点邻接结点的距离值
            for adjacent_vex in current.adjacent:
                if adjacent_vex.visited:
                    continue
                #每个结点的新距离值
                distance = current.distance + current.weight_of_neighbor(adjacent_vex)
                
                #如果获得的距离值小于结点原来的距离则更新结点的距离
                if distance < adjacent_vex.distance:
                    adjacent_vex.distance = distance
                    #用于记录上一个结点位置
                    adjacent_vex.previous = current

            #重新构建堆，首先先将堆中的所有item pop出来
            while len(unvisited_vex_queue):
                heapq.heappop(unvisited_vex_queue)
            
            #将所有未访问的item添加到堆中
            unvisited_vex_queue = [vex for vex in self if not vex.visited]    
            heapq.heapify(unvisited_vex_queue)

        return []


if __name__ == "__main__":

    g = Graphic()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    print(g.dijkstra('a','d'))
    