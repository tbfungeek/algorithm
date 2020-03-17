
# https://leetcode-cn.com/problems/move-zeroes/

def move_zero(list):
    if list is None or len(list) == 0:
        return
    j = 0 
    for i in range(0,len(list)):
        if list[i] != 0:
            if i != j:
                list[j] = list[i]
                list[i] = 0
            j += 1

if __name__ == '__main__':
    test_list = [1,2,0,4,2,0,0,3,0,0,1,1,1,1,0,0,0,0,2,3,4]
    move_zero(test_list)
    print(test_list)
