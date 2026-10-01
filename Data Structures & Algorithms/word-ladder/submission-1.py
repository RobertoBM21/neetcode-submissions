class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        pattern = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                word_pattern = word[:j] + "*" + word[j + 1 :]
                pattern[word_pattern].append(word)

        visit = set([beginWord])
        queue = deque([beginWord])
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    word_pattern = word[:j] + "*" + word[j + 1 :]
                    for nei in pattern[word_pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            res += 1

        return 0
