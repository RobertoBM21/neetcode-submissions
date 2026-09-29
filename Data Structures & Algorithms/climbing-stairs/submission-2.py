class Solution:
    def climbStairs(self, n: int) -> int:
        two_before, one_before = 1, 1

        for i in range(n - 1):
            curr = two_before + one_before
            two_before = one_before
            one_before = curr

        return one_before