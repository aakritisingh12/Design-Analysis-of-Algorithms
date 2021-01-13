# Returns length of LCS for X[0..m-1], Y[0..n-1]
def LCS(A, B, x, y):
    L = [[0 for c in range(y + 1)] for c in range(x + 1)]

    # Following steps build L[m+1][n+1] in bottom up fashion.
    # Note that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following code is used to print LCS
    index = L[x][y]

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and one by one store characters in lcs[]
    i = x
    j = y
    while i > 0 and j > 0:
    # for i, j in zip(range(x, 0, -1), range(y, 0, -1)):
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if A[i - 1] == B[j - 1]:
            lcs[index - 1] = A[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS of " + A + " and " + B + " is " + "".join(lcs))


# Driver program
# str1 = input("Enter string A: ")
# str2 = input("Enter string B: ")
str1 = "AGGTAB"
str2 = "GXTXAYB"
# print("LCS is ", LCS(str1, str2, len(str1), len(str2)))
LCS(str1, str2, len(str1), len(str2))