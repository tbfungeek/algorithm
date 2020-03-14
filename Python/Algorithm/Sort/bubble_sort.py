from random import randrange,shuffle

def generate_list(item_num):
    test_list = []
    for _ in range(0,item_num):
        test_list.append(randrange(0,100,3))
    return test_list

def bubble_sort(list,use_optimize):
    list_length = len(list)
    if list is None or list_length < 2:
        return

    step_time = 0
    swap_time = 0
    print("Will sort the list: {}".format(list)); 
    for i in range(0, list_length):
        has_disorder_item = False
        for j in range(0, list_length - i - 1):
            step_time += 1
            if list[j] > list[j+1]:
                swap_time += 1
                has_disorder_item = True
                list[j] , list[j+1] = list[j+1], list[j]
        if has_disorder_item == False and use_optimize == True:
            break
    print("Bubble sort was ended: {}".format(list)); 
    print("Step time = {0}, Swap time = {1}".format(step_time, swap_time)); 

if __name__ == '__main__':
    bubble_sort(generate_list(100),True)
    print("=" * 60 + ">")
    bubble_sort([63,99,33,12,90,45,15,87,45,48],True)
    print("=" * 60 + ">")
    bubble_sort([63,99,33,12,90,45,15,87,45,48],False)

    

    
            