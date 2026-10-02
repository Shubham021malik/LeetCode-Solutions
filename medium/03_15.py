class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)

        nums.sort()

        i = 0

        while i < n - 2:

            # duplicate i skip
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = n - 1

            sum = -1 * nums[i]

            while j < k:
                s = nums[j] + nums[k]

                if s == sum:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # duplicate j skip
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # duplicate k skip
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < sum:
                    j += 1

                else:
                    k -= 1

            i += 1

        return ans
