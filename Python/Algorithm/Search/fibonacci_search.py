fib_indexs = [0,1,1,2,3,5,8,13,21,34,55]

def fibonacci_search(list,target):

    length = len(list)
    low = 0
    high = length - 1

    #find index value more than target list length 
    fib_i = 0
    while fib_indexs[fib_i] < length:
        fib_i += 1

    #fill the last item with tail item
    for index in range(0,fib_indexs[fib_i] - length):
        list.append(list[length - 1])
    
    while low <= high:
        mid = low + fib_indexs[fib_i - 1] - 1
        if target < list[mid]:
            high = mid - 1
            fib_i = fib_i - 1;
        elif target > list[mid]:
            low = mid + 1
            fib_i = fib_i - 2
        else:
            if mid > length:
                return length - 1
            else:
                return mid

if __name__ == "__main__":
    print(fibonacci_search([0,1,16,24,35,47,59,62,73,88,99],59))