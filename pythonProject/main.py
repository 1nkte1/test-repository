class Solution(object):
    def divide(self, dividend, divisor):
        negative = False
        if dividend < 0:
            dividend*=-1
            negative = not negative
        if divisor < 0:
            divisor*=-1
            negative = not negative

        print(not -2**31 <= dividend <= 2**31 - 1)
        if not -2**31 <= dividend <= 2**31 - 1 or not -2**31 <= divisor <= 2**31 - 1:
            if negative:
                return -2**31
            else:
                return 2**31 - 1

        howManyTimes = 0
        total = dividend-divisor
        while total >= 0:
            total -= divisor
            howManyTimes += 1

        if negative:
            return -howManyTimes
        return howManyTimes

a = Solution()
print(a.divide(2147483647, 1))