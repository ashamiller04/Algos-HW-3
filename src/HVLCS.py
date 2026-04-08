#To Run: If you want to use input file "16_b43.in"
#       python HVLCS.py 16 b43
# must be in \src directory in terminal

from get_input import get_input
import sys


def runHVLCS(k, letters, values, a, b):
    # returns a tuple of max value and one common subsequence of that value

    n = len(a)
    m = len(b)

    #Initialize 2D matrix of size (n+1) * (m+1)

    matrix = [[0] * (n + 1) for _ in range(m + 1)]


#finding the actual subsequence from the dp matrix
def findLCS(a, b, matrix):



#creating output
def HVLCS_output(k, letters, values, a, b):
    result = runHVLCS(k, letters, values, a, b)

    print(result[0])
    print(result[1])


#runs program
HVLCS_output(*get_input(f"{sys.argv[1]}_{sys.argv[2]}.in"))

