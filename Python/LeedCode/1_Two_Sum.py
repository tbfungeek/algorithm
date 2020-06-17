'''

【题目】

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

【更多题解见】：https://leetcode-cn.com/submissions/detail/79586807/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

def twoSum_01(nums,target):
    sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
    head = 0
    tail = len(nums) - 1
    result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    while result != target:
        if result < target and head <= len(nums) - 1:
            head += 1
        elif result > target and tail >= 1 :
            tail -= 1
        result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    return [sorted_id[head], sorted_id[tail]]

def twoSum_02(nums, target):

    hashset = {} #key -> nums[index] value -> index
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in hashset:
            return [hashset[temp],i]
        hashset[nums[i]] = i
    return []

            
print(twoSum_02([3,2,4],6))
