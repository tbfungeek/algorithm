from random import randrange,shuffle

def generate_test_list(start,end,count):
    return [randrange(start,end) for i in range(0,count)]

def shell_sort(list):
    if list is None or len(list) < 2:
        return
    list_length = len(list)
    gap = int(list_length / 2)
    while gap > 0 :
        inner_insert_sort(list,gap)
        gap = int(gap / 2)

def inner_insert_sort(list,gap):

    list_length = len(list)
    if list_length < 2:
        return 

    print("sort list with gap " + "=" * 10 + ">{0} ==> {1}".format(gap,list))
    for i in range(gap, list_length, gap):

        #current sort item
        temp = list[i]

        #find the place to insert
        pre_insert_pos = i - gap
        while (pre_insert_pos >=0) and (list[pre_insert_pos] > temp):
            pre_insert_pos -= gap

        #move the items
        k = i - gap
        while k > pre_insert_pos:
            list[k + gap] = list[k]
            k -= gap
        
        #inset to the target place
        list[pre_insert_pos + gap] = temp

    print("final result " + "=" * 10 + "> {}".format(list))


if __name__ == '__main__':

    shell_sort(generate_test_list(0,1000,10))
