
def delete_item(list,start,end):
    for i in range(start,len(list) - 1):
        print(i)
        list[i] = list[i + 1] 
    del list[len(list) - 1]
    print(list)

def insert_item(list,start,item):
    for i in reversed(range(start,len(list) - 1)):
        print(i)
        list[i + 1] = list[i]
    list[start] = item

if __name__ == '__main__':
    print("======>")
    delete_item([0,1,2,3,4,5,6,7,8,9,10,11,12],3,8)
    insert_item([0,1,2,3,4,5,6,7,8,9,10,11,12],3,45)