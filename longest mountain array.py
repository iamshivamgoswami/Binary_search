class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = ans = 0
        while i < len(arr):
            base = i
            while i + 1 < len(arr) and arr[i] < arr[i + 1]:
                i += 1
            if i == base:
                i += 1
                continue
            peak = i
            while i + 1 < len(arr) and arr[i] > arr[i + 1]:
                i += 1
            if i == peak:
                i += 1
                continue
            ans = max(ans, i - base + 1)

        return ans

