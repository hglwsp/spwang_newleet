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
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            return a if b == 0 else gcd(b,a%b)
        if str1 + str2 != str2 + str1:
            return ""
        return str1[0:gcd(len(str1), len(str2))]

test = Solution()
print(test.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))