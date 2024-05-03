
def findMinSequenceCount(source: str, target: str):
    def longestSub(i, j):
        while i < n and j < m:
            if source[i] == target[j]:
                j += 1
            i += 1
        return j

    n, m = len(source), len(target)
    res = j = 0
    while j < m:
        t = longestSub(0, j)
        if t == j:
            return -1
        j = t
        res += 1
    return res


def main():
    print(findMinSequenceCount("abc", "abcbc"))
    print(findMinSequenceCount("abc", "acdbc"))
    print(findMinSequenceCount("xyz", "xzyxz"))

if __name__ == '__main__':
    main()
