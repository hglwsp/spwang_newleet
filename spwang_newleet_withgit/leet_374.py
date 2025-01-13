import time

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
    def guessNumber(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            mid = (left+right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
