class WorkBreak:
    def __init__(self) -> None:
        super().__init__()

    def can_break(self, s, d) -> bool:
        if not s:
            return False
        for i in range(1, len(s) + 1):
            if d.get(s[:i], 0) > 0:
                d[s[:i]] -= 1
                print(d[s[:i]])
                if self._can_break(s[:i], d):
                    return True
        return False

    def word_break(self, s, word_dict) -> int:
        dp = [0 for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i):
                if dp[j]:
                    if s[j+1:i+1] in word_dict:
                        dp[i] = True

            if not dp[i]:
                dp[i] = s[:i+1] in word_dict

        return dp[-1]


ws = WorkBreak()
print(ws.word_break("leetcode", ["leet", "co"]))
