# https://leetcode-cn.com/problems/two-sum/

def two_sum(nums, target):
    for i in range(0,len(nums) - 1):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
    
if __name__ == '__main__':
    test_list = [2, 7, 11, 15]
    print(two_sum(test_list,9))