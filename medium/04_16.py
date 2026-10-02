class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        i = 0
        while i < n - 2:
            j = i + 1
            k = n -1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s == target:
                    return s
                elif s < target:
                    j+=1
                else:
                    k-=1
            i+=1
        return ans
