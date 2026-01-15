def max_operations(a):
    n = len(a)

    # dp[i] = length of Longest Non-Decreasing Subsequence ending at i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if a[j] <= a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    lnds_length = max(dp)
    return n - lnds_length


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    a = list(map(int, input("Enter the elements: ").split()))

    print("Maximum number of operations:", max_operations(a))
