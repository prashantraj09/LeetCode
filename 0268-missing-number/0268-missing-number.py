class Solution:
    def missingNumber(self, arr):
        i = 0
        while(i < len(arr)):
            idx = arr[i] - 1
            if arr[i] == i + 1 or arr[i] == 0:
                i += 1
            else:
                arr[idx], arr[i] = arr[i], arr[idx]
        for i in range(len(arr)):
            if arr[i] != (i + 1):
                return (i + 1)
        if 0 not in arr:
            return 0
        return len(arr)