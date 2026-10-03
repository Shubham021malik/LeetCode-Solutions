class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        n = len(arr)
        count = 0

        i = 0

        while i < n - 2:
            j = i + 1
            k = n - 1

            while j < k:
                s = arr[i] + arr[j] + arr[k]

                if s < sum:
                    # j se k ke beech ke saare elements
                    # arr[i] ke saath sum < sum denge
                    count += k - j
                    j += 1
                else:
                    k -= 1

            i += 1

        return count
