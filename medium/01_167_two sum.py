class Solution:
    def twoSum(self, numbers: list[int], target: int):
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i + 1, j + 1]
            elif total < target:
                i += 1
            else:
                j -= 1


numbers = [2, 7, 11, 15]
target = 9


answer = Solution().twoSum(numbers, target)

print(answer)
