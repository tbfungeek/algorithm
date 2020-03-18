def insert_value(list,pos,value):
    if list is None or len(list) <= pos or pos < 0:
        return
    list.append(0)
    length = len(list)
    for i in reversed(range(pos,length - 1)):
        list[i+1] = list[i]
    list[pos] = value
    print(list)

def delete_item(list,pos):
    if list is None or len(list) <= pos or pos < 0:
        return
    length = len(list)
    for i in range(pos,length -1):
        list[i] = list[i+1]
    del list[length - 1]
    print(list)

def traval_all_paired(list):
    for i in range(0,len(list) - 1):
        for j in range(i+1,len(list)):
            print("{} === {}".format(list[i],list[j]))

if __name__ == '__main__':
    insert_value([0,1,2,3,4,5,6,7],5,99)
    insert_value([1,2,3,4,5,6],5,99)
    delete_item([1,2,3,4,5,6],2)
    traval_all_paired([1,2,3,4])
