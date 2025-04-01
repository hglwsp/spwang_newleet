import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
def log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

class Solution:
    @log_execution
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        res = [0 for i in range(len(candies))]
        for i in range(len(candies)):
            res[i] = True if candies[i] + extraCandies >= max_candies else False
        return res

test = Solution()
logging.info(test.kidsWithCandies([2,3,5,1,3], 3))
