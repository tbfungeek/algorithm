class DisjointSet(object):
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add_node(self,value):
        self.parent[value] = -1
        self.rank[value] = 0

    def find_root(self,value):  
        if value not in self.parent.keys():
            self.add_node(value)
        current_value = value
        while self.parent[current_value] != -1:
            current_value = self.parent[current_value]
        return current_value

    # False 表示合并成功， True 返回合并失败
    def union_node(self,node_x,node_y):
        x_root = self.find_root(node_x)
        y_root = self.find_root(node_y)
        if x_root == y_root:
            return False
        else: 
            x_rank = self.rank[x_root]
            y_rank = self.rank[y_root]
            #将矮的树合并到高的树
            if x_rank > y_rank:
                self.parent[y_root] = x_root
            elif x_rank < y_rank:
                self.parent[x_root] = x_root
            else:
                #如果两个树同样高度那么将y挂到x 同时将
                self.rank[x_root] += 1
                self.parent[y_root] = x_root
            return True

if __name__ == "__main__":

    set = DisjointSet()
    
    graphic = [
        [0,1],
        [1,2],
        [1,3],
        [2,4],
        [2,5],
        [3,4]
    ]

    for edge_nodes in graphic:
        print("Union node {0} ---> {1}".format(edge_nodes[0],edge_nodes[1]))
        if not set.union_node(edge_nodes[0],edge_nodes[1]):
            print("Cycle Detected!")



        