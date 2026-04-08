#To Run: If you want to use input file "16_b43.in"
#       python HVLCS.py 16 b43
# must be in \src directory in terminal

from get_input import get_input
import sys


def runHVLCS(letters, values, a, b):
    # returns a tuple of max value and one common subsequence of that value

    #this currently does just lcs

    n = len(a)
    m = len(b)

    #creates a neater dict of letters and values
    alphabet = dict(zip(letters, values))

    #Initialize 2D matrix of size (m+1) * (n+1)
    matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + int(alphabet[a[i - 1]])
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[n][m], findLCS(a, b, matrix)



#finding the actual subsequence from the dp matrix
def findLCS(a, b, matrix):
    n = len(a)
    m = len(b)
    lcs = ""

    while (n > 0 and m > 0):
        if a[n - 1] == b[m - 1]:
            lcs = a[n - 1] + lcs
            n = n - 1
            m = m - 1
        elif matrix[n - 1][m] > matrix[n][m - 1]:
            n = n - 1
        else:
            m = m -1

    return lcs



#creating output
def HVLCS_output(letters, values, a, b):
    result = runHVLCS(letters, values, a, b)

    print(result[0])
    print(result[1])


#runs program
HVLCS_output(*get_input(f"{sys.argv[1]}_{sys.argv[2]}.in"))

