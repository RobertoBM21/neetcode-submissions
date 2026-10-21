class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = Counter(s1)
        window = Counter()
        have, need = 0, len(count1)
        left = 0

        for right in range(len(s2)):
            c = s2[right]
            window[c] += 1

            if c in count1 and window[c] == count1[c]:
                have += 1

            if (right - left + 1) > len(s1):
                out = s2[left]
                if out in count1 and window[out] == count1[out]:
                    have -= 1
                window[out] -= 1
                left += 1

            if have == need:
                return True

        return False