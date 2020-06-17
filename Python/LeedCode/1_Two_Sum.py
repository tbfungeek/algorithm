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
            
print(twoSum_02([3,2,4],6))
