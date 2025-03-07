class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False
        flag = 0
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i] and flag == 0:   # up
                continue
            if arr[i-1] > arr[i] and flag == 0:   # up
                flag = 1
            if arr[i-1] < arr[i] and flag == 1:   # down
                return False
            if arr[i-1] > arr[i] and flag == 1:   # down
                continue
        return flag == 1

test = Solution()
print(test.validMountainArray([0,3,2,1]))
