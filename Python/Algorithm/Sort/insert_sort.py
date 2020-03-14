from random import randrange,shuffle

def generate_test_list(start,end,count):
    test_list = []
    for _ in range(0,count):
        test_list.append(randrange(start,end))
    return test_list

def insert_sort(list):
    if list is None or len(list) < 2:
        return
    list_length = len(list)
    print("list for sort : {}".format(list))

    for i in range(1, list_length):
        #step one temp store current item
        temp = list[i]

        #find place to insert
        pos_front_insert_place = i - 1
        while (pos_front_insert_place >= 0) and (list[pos_front_insert_place] > temp):
            pos_front_insert_place -= 1

        #prepare space for insert
        k = i - 1
        while k > pos_front_insert_place:
            list[k+1] = list[k]
            k -= 1
        
        #inset current item to right place
        list[pos_front_insert_place + 1] = temp
        print("temp item = list[{0}] = {1} and result of sort: {2}".format(i,temp,list))
    
    print("final result of sort: {}".format(list))

if __name__ == '__main__':
    insert_sort(generate_test_list(0,1000,10))