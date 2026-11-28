class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_index = dict()
        for i in range(len(nums)):
            if target - nums[i] not in hash_index:
                hash_index[nums[i]] = {i}
            else:
                j = hash_index[target-nums[i]].pop()
                return [i, j] if i < j else [j, i]
        return []