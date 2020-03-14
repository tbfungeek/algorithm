
from random import randrange

def generate_test_list(start,end,count):
    return [randrange(start , end) for _ in range(0,count)]

def merge_sort(list):
    sort_part(list,0,len(list)-1)

def sort_part(list,left,right):
    if left >= right:
        return
    mid = int((left + right) / 2)
    sort_part(list,left,mid)
    sort_part(list,mid+1,right)
    merge_result(list,left,mid,right)

def merge_result(list,left,mid,right):
    
    temp = []
    left_part_index = left
    right_part_index = mid + 1
    
    while (left_part_index <= mid) and (right_part_index <= right):
        if(list[left_part_index] < list[right_part_index]):
            temp.append(list[left_part_index])
            left_part_index += 1 
        else:
            temp.append(list[right_part_index])
            right_part_index += 1 
    
    while left_part_index <= mid:
        temp.append(list[left_part_index])
        left_part_index += 1

    while right_part_index <= mid:
        temp.append(list[right_part_index])
        right_part_index += 1

    for i in range(0,len(temp)):
        list[left + i] = temp[i]

if __name__ == "__main__":

    list = generate_test_list(0,100,10)
    print(list)
    merge_sort(list)
    print(list)
