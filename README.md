# Algos-HW-3

Asha Miller
UFID: 2619-5990

# Instructions

Copy the link to clone the repository into an IDE 
Or 
Run git clone https://github.com/ashamiller04/Algos-HW-3.git 

Sample input and output files are provided under \data

- To run HVLCS with the example input, cd to \src and run `python HVLCS.py 16 j32`
- To create new input files, cd to \data and run `python generator.py K` where K is the alphabet size
- To run HVLCS with the new input, cd to \src and run `python HVLCS.py {k} {letterVALUE}` as seen in the filename `{k}_{letterVALUE}`

Output files will be sent to the \data directory


# Written Component Questions

**Question 1:** Graphed runtime of 10 nontrivial files with string lengths >= 25

<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/94133f9d-0870-4705-a120-d50fc83ce544" />




**Question 2:** 

OPT[i][j] is defined as the max value of a common subsequence between the the first i chars of string A and j chars of string B.

Case 1: OPT[0][j] = 0
-> OPT[i][j] = 0

Case 2: A[i - 1] == B[j - 1]
-> OPT[i][j] = OPT[i - 1][j - 1] + value[A[i - 1]]

Case 3: A[i - 1] != B[j - 1]
-> OPT[i][j] = max{OPT[i - 1][j], OPT[i][j - 1]}

This recurrence equation works because each iteration builds on previously calculated solutions, until every subproblem has been computed
and the final result has been stored in the matrix.




**Question 3:** 
```
for i = 0 to n:
  matrix[i][0] = 0
for j = 0 to m:
  matrix[0][j] = 0

for i = 0 to n:
  for j = 0 to m:
    if i == 0 or j == 0:
      matrix[i][j] = 0
    else if A[i - 1] == B[j - 1]:
      matrix[i][j] = matrixT[i - 1][j - 1] + value[A[i - 1]]
    else:
      matrix[i][j] = max{matrix[i - 1][j], matrix[i][j - 1]}
```
The runtime complexity of this psuedocode is O(n * m). 
