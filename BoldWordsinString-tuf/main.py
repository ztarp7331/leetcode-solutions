class Solution:
    def boldTags(self, words: list[str], s: str) -> str:
        n = len(s)
        boldTags = [False] * n
        for word in words:
            startIndex = s.find(word)
            wl = len(word)
            endIndex = startIndex + wl
            while startIndex != -1:
                boldTags[startIndex:endIndex] = [True] * wl
                startIndex = s.find(word, startIndex + 1)
        result = []
        for i in range(n):
            if boldTags[i] and (i == 0 or not boldTags[i - 1]):
                result.append("<b>")
            result.append(s[i])
            if boldTags[i] and (i == n - 1 or not boldTags[i + 1]):
                result.append("</b>")
        return "".join(result)
