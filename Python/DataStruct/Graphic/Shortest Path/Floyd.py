import sys

def Floyd(graph):

    #copy 出一份 graph
    dist = list(map(lambda i : list(map(lambda j : j, i)), graph))

    #计算出矩阵宽高
    nV = len(dist)

    #计算
    for k in range(nV): 
        for i in range(nV): 
            for j in range(nV): 
                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j]) 
    display_result(dist) 

def display_result(dist):
    nV = len(dist) 
    for i in range(nV): 
        for j in range(nV): 
            if(dist[i][j] == sys.maxsize): 
                print("INF", end =" ")
            else: 
                print(dist[i][j], end ="  ")  
        print(" ")

graph = [[0, 3, sys.maxsize, 5],
         [2, 0, sys.maxsize, 4],
         [sys.maxsize,1, 0, sys.maxsize,],
         [sys.maxsize,sys.maxsize,2, 0]]; 
         
Floyd(graph);