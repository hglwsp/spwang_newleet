import time
import itertools
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.100f} seconds to execute.")
        return result

    return wrapper

class Solution:
    @timer
    def longestArithSeqLength(self, nums) -> int:
        dp = [[1] * 1001 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j] + 500
                dp[i][diff] = max(dp[i][diff],dp[j][diff]+1)
        # deal_list = list(itertools.chain(*dp))
        deal_list = [num for sublist in dp for num in sublist]
        return max(deal_list)

test = Solution()
print(test.longestArithSeqLength([3,6,9,12]))
