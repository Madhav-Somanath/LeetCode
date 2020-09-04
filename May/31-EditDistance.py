"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
    
 """
 
 # SOLUTION
 
def minDistance(word1, word2):
    
    m = len(word1)
    n = len(word2)
    
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j
        
    print(table)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
                # print("IF OCCURED\n")
                # print(table)
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                # print("ELSE OCCURED\n")
                # print(table)
    return table[-1][-1]

# all credits to user 'anderson5' on leetcode, i couldnt figure this one out (dynamic programming is HARD)

# print(minDistance('horse', 'ros'))
