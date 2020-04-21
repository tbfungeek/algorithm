class Node(object):

    def __init__(self,value,first_in,first_out):
        self.__value = value
        self.__first_in = first_in
        self.__first_out = first_out

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        self.__value = value
    
    @property
    def first_in(self):
        return self.__first_in

    @first_in.setter
    def first_in(self, first_in):
        self.__first_in = first_in

    @property
    def first_out(self):
        return self.__first_out

    @first_out.setter
    def first_out(self,first_out):
        self.__first_out = first_out

    def __str__(self):
        return self.__value

class Edge(object):
    def __init__(self,tail_vex,head_vex,hlink,tlink,info):
        self.__tail_vex = tail_vex
        self.__head_vex = head_vex
        self.__hlink    = hlink
        self.__tlink    = tlink
        self.__info     = info

    @property
    def tail_vex(self):
        return self.__tail_vex

    @tail_vex.setter
    def tail_vex(self,tail_vex):
        self.__tail_vex = tail_vex

    @property
    def head_vex(self):
        return self.__head_vex

    @head_vex.setter
    def head_vex(self,head_vex):
        self.__head_vex = head_vex
    
    @property
    def hlink(self):
        return self.__hlink

    @hlink.setter
    def hlink(self,hlink):
        self.__hlink = hlink

    @property
    def tlink(self):
        return self.__tlink

    @tlink.setter
    def tlink(self,tlink):
        self.__tlink = tlink

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self,info):
        self.__info = info


class CrossListGraphic(object):

    def __init__(self):
        self.__nodes = []
    
    def add_node(self,value):
        node = Node(value,None,None)
        self.__nodes.append(node)

    def add_edge(self,tail_vex,head_vex,info):

        #如果tail_vex大于等于结点数组则添加失败
        if  tail_vex >= len(self.__nodes) or head_vex >= len(self.__nodes):
           return

        edge:Edge = Edge(tail_vex,head_vex,None,None,info)

        #找到对应结点
        out_node:Node = self.__nodes[tail_vex]

        #如果还没有出度的边则直接添加到node上
        if out_node.first_out is None:
            out_node.first_out = edge
        else:
            #遍历已有的出度的边
            out_edge:Edge = out_node.first_out
            while out_edge.tlink != None and out_edge.head_vex != head_vex:
                out_edge = out_edge.tlink

            #如果没有找到则添加到最后
            if out_edge.tlink is None:
                out_edge.tlink = edge
            else:
            #如果找到的话更新数据
                out_edge.info = info

        #添加入度信息
        in_node:Node = self.__nodes[head_vex]

        if in_node.first_in is None:
            in_node.first_in = edge
        else:
            in_edge:Edge = in_node.first_in
            while in_edge.hlink != None and in_edge.tail_vex != tail_vex:
                in_edge = in_edge.hlink
            
            if in_edge.hlink is None:
                in_edge.hlink = edge
            else:
            #如果找到的话更新数据
                in_edge.info = info

if __name__ == "__main__":
    cross_list = CrossListGraphic()

    cross_list.add_node("V1")
    cross_list.add_node("V2")
    cross_list.add_node("V3")
    cross_list.add_node("V4")

    cross_list.add_edge(0,1,"V1->V2")
    cross_list.add_edge(0,2,"V1->V3")
    cross_list.add_edge(2,0,"V3->V1")
    cross_list.add_edge(2,3,"V3->V4")
    cross_list.add_edge(3,1,"V4->V2")
    cross_list.add_edge(3,2,"V4->V3")
    cross_list.add_edge(3,0,"V4->V1")

    