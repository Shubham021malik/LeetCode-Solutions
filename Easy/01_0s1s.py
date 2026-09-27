class Solution():
    def zerone(self, arr):
        i = 0

        for j in range(len(arr)):
            if arr[j] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
        return arr

arr = [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0] 
answer = Solution().zerone(arr)
print(answer)

