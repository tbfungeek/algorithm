def quick_search(list):
    #if len = 0 || len == 1 just return list as result
    if(len(list) < 2):
        return list
    #set a initial pivot
    pivot = list[0]
    #fine element which is less than pivot and great then the pivot 
    less = []
    greater = []
    for element in list[1:]:
        if element <= pivot:
            less.append(element)
        else:
            greater.append(element)
    return quick_search(less) + [pivot] + quick_search(greater)
            

if __name__ == "__main__":
    print(quick_search([2,3,4,1,3,4,5,68,3,4,5,3]))