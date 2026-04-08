from get_input import get_input
import sys


def runHVLCS(k, letters, values, a, b):
    # returns a tuple of max value and one common subsequence of that value

    #testing
    return 10, "abcde"






#creating output
def HVLCS_output(k, letters, values, a, b):
    result = runHVLCS(k, letters, values, a, b)

    print(result[0])
    print(result[1])


#runs program
HVLCS_output(*get_input(f"{sys.argv[1]}_{sys.argv[2]}.in"))

