
def count_sort(list):

    if list is None or len(list) < 2:
        return

    # 1. prepare the count list
    max_item = max(list)
    min_item = min(list)
    count_list = [0]*(max_item - min_item + 1) 

    # 2. count
    for item in list:
        count_list[item - min_item] += 1

    # if allow unstable sort we can get result as follow
    #index = 0
    #for count in count_list:
    #    for i in range(0,count):
    #        list[index] = min_item + index
    #    index += 1
    
    # if we need stable sort we need do more
    # 3. update position
    temp_sum = 0
    for i in range(0, len(list)):
        temp_sum += count_list[i]
        count_list[i] = temp_sum
        #now count_list store the last position of session

    #4. get the result 
    result_list = [0] * len(list)
    for item in list:
        pos = count_list[item - min_item] - 1
        result_list[pos] = item
        count_list[item - min_item] -= 1

    list[:] = result_list[:]

if __name__ == "__main__":

    test_list = [95,94,91,98,99,90,99,93,91,92]
    print(test_list)
    count_sort(test_list)
    print(test_list)
    