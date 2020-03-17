# https://leetcode-cn.com/problems/container-with-most-water/

def container_with_most_water(list):
    max_area = 0
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            area = (j - i) * min(list[i],list[j])
            max_area = max(area,max_area)
    return max_area

def container_with_most_water_s1(list):
    if list is None or len(list) < 2:
        return 0
    max_area = 0
    i = 0
    j = len(list) - 1
    minHeight = 0;
    while i < j :
        if list[i] < list[j]:
            minHeight = list[i]
            i += 1
        else:
            minHeight = list[j]
            j -= 1
        max_area = max(minHeight * (j - i + 1),max_area)

    return max_area

if __name__ == '__main__':
    test_list = [1,2,1]
    print(container_with_most_water_s1(test_list))