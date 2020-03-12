def interpolate_search(list,key):
    if list is None or len(list) == 0:
        return -1
    low = 0;
    hight = len(list) - 1
    while low <= hight:
        ratio = (key - list[low])/(list[hight] - list[low])
        mid = int(low + ratio * (hight - low))
        if (key < list[mid]):
            hight = mid - 1
        elif key == list[mid]:
            return mid
        else:
            low = mid + 1

if __name__ == "__main__":
     print(interpolate_search([1,2,4,5,6,7,8,78],4))
