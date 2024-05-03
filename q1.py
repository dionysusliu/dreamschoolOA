
def findMinSequenceCount(source: str, target: str):
    m, n = len(source), len(target)
    dp = [[float('inf') * (n + 1) for _ in range(m + 1)]]

    # base cases
    for i in range(m + 1): # empty target
        dp[i][0] = 0 
    for j in range(1, n + 1): # empty source
        dp[0][j] = float('inf')
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i-1] == target[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    return dp[m][n] if dp[m][n] != float('inf') else -1


def main():
    print(findMinSequenceCount("abc", "abcbc"))
    print(findMinSequenceCount("abc", "acdbc"))
    print(findMinSequenceCount("xyz", "xyzxz"))
