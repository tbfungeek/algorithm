from collections import deque

def grahic_traval(grahic,start,end):
    search_queue = deque();
    search_queue += grahic[start]
    searched = []
    while search_queue.count != 0:
        target = search_queue.popleft()
        if target in searched:
            continue
        if target != end:
            search_queue += grahic[target]
            searched.append(target)
        else:
            return searched
    return searched

if __name__ == "__main__":

    graphic = {}
    graphic["O"] = ["A","B"]
    graphic["A"] = ["C"]
    graphic["B"] = ["D","E"]
    graphic["C"] = ["F"]
    graphic["D"] = ["C"]
    graphic["E"] = ["C"]
    graphic["F"] = []

    print(grahic_traval(graphic,"O","E"))